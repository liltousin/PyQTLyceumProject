import os

from dotenv import load_dotenv
from telethon.errors.rpcerrorlist import (
    PasswordHashInvalidError,
    PhoneCodeInvalidError,
    PhoneNumberBannedError,
    PhoneNumberInvalidError,
    SessionPasswordNeededError,
)
from telethon.sync import TelegramClient


def try_to_send_code(phone):
    load_dotenv()
    api_id = os.getenv('api_id')
    api_hash = os.getenv('api_hash')
    client = TelegramClient(phone, api_id, api_hash)
    try:
        client.connect()
    except ConnectionError:
        return 'Нет подключения к интернету!'
    if client.is_user_authorized():
        client.disconnect()
        return 'Клиент уже авторизован!'
    else:
        try:
            client.send_code_request(phone)
        except PhoneNumberBannedError:
            client.disconnect()
            return 'Номер заблокирован!'
        except (TypeError, PhoneNumberInvalidError):
            client.disconnect()
            return 'Неверный формат номера!'
    return client


def code_checker(client: TelegramClient, code: str):
    if not code.isdecimal():
        return 'Неверный формат кода!'
    try:
        client.sign_in(client._phone, code)
    except PhoneCodeInvalidError:
        client.disconnect()
        return 'Неправильный код!'
    except SessionPasswordNeededError:
        return client
    client.disconnect()
    return 'ok'


def password_checker(client: TelegramClient, pswd: str):
    try:
        client.sign_in(password=pswd)
    except (ValueError, PasswordHashInvalidError):
        return client
    client.disconnect()
    return 'ok'


if __name__ == '__main__':
    banned_phones = [
        '6283123578227',
        '6285789440688',
        '6285640517315',
        '6283138547296',
    ]
    phone = '6285728977612'

    client = try_to_send_code(phone)
    if type(client) == TelegramClient:
        code = input('code:')
        client = code_checker(client, code)
        if type(client) == TelegramClient:
            while client:
                pswd = input('password:')
                client = password_checker(client, pswd)
        else:
            print(client)
    else:
        print(client)
