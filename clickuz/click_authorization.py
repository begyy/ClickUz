import hashlib
from django.conf import settings


def click_authorization(click_trans_id, amount, action, sign_time, sign_string, merchant_trans_id,
                        merchant_prepare_id=None, *args, **kwargs):
    """
    Authorization
    :param click_trans_id:
    :param amount:
    :param action:
    :param sign_time:
    :param sign_string:
    :param merchant_trans_id:
    :param merchant_prepare_id:
    :param args:
    :param kwargs:
    :return: True or False
    """
    assert settings.CLICK_SETTINGS.get('service_id') != None
    assert settings.CLICK_SETTINGS.get('secret_key') != None
    assert settings.CLICK_SETTINGS.get('merchant_id') != None

    service_id = settings.CLICK_SETTINGS['service_id']
    secret_key = settings.CLICK_SETTINGS['secret_key']

    text = f"{click_trans_id}{service_id}{secret_key}{merchant_trans_id}"
    if merchant_prepare_id != "" and merchant_prepare_id is not None:
        text += f"{merchant_prepare_id}"
    text += f"{amount}{action}{sign_time}"
    hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    if hash != sign_string:
        return False
    return True
