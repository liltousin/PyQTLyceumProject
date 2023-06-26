import os
from sqlite3 import Connection

from telethon.errors.rpcerrorlist import PhoneNumberBannedError, PhoneNumberInvalidError
from telethon.sync import TelegramClient

from sql_functions import set_akk_status
from tg_auth_funcions import get_api_id_api_hash


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


def check_ban_status(phone: str, return_client=False):
    status = check_akk_status(phone)
    client = None
    if status == 'notauth':
        api_id, api_hash = get_api_id_api_hash()
        client = TelegramClient(phone, api_id, api_hash)
        client.connect()
        try:
            client.send_code_request(phone)
        # TODO: разобраться почему нельзя удалить если неправильный номер
        # del_akk_in_db
        except (PhoneNumberBannedError, TypeError, PhoneNumberInvalidError):
            client.disconnect()
            return 'banned'
    if return_client:
        return status, client
    if client:
        client.disconnect()
    return status


def check_akk_and_update(phone: str, db_status: str, connection: Connection):
    phone = str(phone)
    if db_status == 'banned':
        status = check_ban_status(phone)
    else:
        status = check_akk_status(phone)
    set_akk_status(connection, status, phone)
    return status


# if __name__ == '__main__':
#     phone = '6283134468453'
#     print(check_akk_status(phone))
