from dotenv import load_dotenv
from telethon.errors.rpcerrorlist import (
    PasswordHashInvalidError,
    PhoneCodeInvalidError,
    PhoneNumberBannedError,
    SessionPasswordNeededError,
)
from telethon.sync import TelegramClient
import os


def try_to_send_code(phone):
    load_dotenv()
    api_id = os.getenv('api_id')
    api_hash = os.getenv('api_hash')
    client = TelegramClient(phone, api_id, api_hash)
    client.connect()
    if client.is_user_authorized():
        client.disconnect()
        return 'Клиент уже авторизован!'
    else:
        try:
            client.send_code_request(phone)
        except PhoneNumberBannedError:
            client.disconnect()
            return 'Номер заблокирован!'
        except TypeError:
            client.disconnect()
            return 'Неверный формат номера!'
    return client


def code_is_entered(client: TelegramClient, code: str):
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
    return ''


def password_is_entered(client: TelegramClient, pswd: str):
    try:
        client.sign_in(password=pswd)
    except PasswordHashInvalidError:
        return client
    client.disconnect()
    return ''


phone = '6283138547296'
banned_phone = '6285640517315'

client = try_to_send_code(phone)
if type(client) == TelegramClient:
    code = input('code:')
    client = code_is_entered(client, code)
    if type(client) == TelegramClient:
        while client:
            pswd = input('password:')
            client = password_is_entered(client, pswd)
    else:
        print(client)
else:
    print(client)
