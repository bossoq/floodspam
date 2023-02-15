from typing import Tuple

import requests

from lxml.html import fromstring as html
from script import CONST
from script.logger import Logger


mylogger = Logger()


def get_csrf_cookie() -> Tuple[str, dict]:
    res = requests.get(CONST.REG_PAGE)
    body = html(res.text)
    csrf = body.xpath('//input[@name="_csrf_"]/@value')[0]
    cookie = res.cookies.get_dict()
    mylogger.info(f'csrf: {csrf}')
    mylogger.info(f'cookie: {cookie}')
    return csrf, cookie


def register(csrf: str, cookie: dict, idx: int) -> None:
    username = CONST.USERNAME.format(idx=idx)
    tel = CONST.TEL.format(idx=idx)
    data = {
        'user_name': username,
        'tel': tel,
        'pwd': CONST.PASSWORD,
        'invite_code': CONST.INVITE_CODE,
        '_csrf_': csrf,
    }
    res = requests.post(CONST.FORM_PAGE, data=data, cookies=cookie)
    mylogger.info(f'{idx}: {res.text}')


def main() -> None:
    for i in range(10000):
        csrf, cookie = get_csrf_cookie()
        register(csrf, cookie, i)
    return


if __name__ == "__main__":
    main()
    mylogger.done()
