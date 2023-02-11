import os

from telethon.errors.rpcerrorlist import PhoneNumberBannedError
from telethon.sync import TelegramClient
from sqlite3 import Connection

from tg_auth_funcions import get_api_id_api_hash
from sql_functions import set_akk_status


def check_nofile_status(phone: str):
    return 'nofile' if not os.path.isfile(f'{phone}.session') else False


def check_notauth_status(phone: str):
    api_id, api_hash = get_api_id_api_hash()
    client = TelegramClient(phone, api_id, api_hash)
    client.connect()
    result = client.is_user_authorized()
    client.disconnect()
    return 'notauth' if not result else False


def check_akk_status(phone: str):
    if status := check_nofile_status(phone):
        return status
    elif status := check_notauth_status(phone):
        return status
    return 'ok'


def check_ban_status(phone: str):
    status = check_akk_status(phone)
    if status == 'notauth':
        api_id, api_hash = get_api_id_api_hash()
        client = TelegramClient(phone, api_id, api_hash)
        client.connect()
        try:
            client.send_code_request(phone)
        except PhoneNumberBannedError:
            client.disconnect()
            return 'banned'
        return status
    return status


def check_akk_and_update(phone: str, db_status: str, connection: Connection):
    try:
        if db_status == 'banned':
            status = check_ban_status(phone)
        else:
            status = check_akk_status(phone)
        set_akk_status(connection, status, phone)
        return status
    except ConnectionError:
        return 'Нет подключения к интернету!'


# if __name__ == '__main__':
#     phone = '6283134468453'
#     print(check_akk_status(phone))
