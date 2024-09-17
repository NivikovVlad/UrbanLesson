"""
Библиотека requests позволяет упростить работу с Http запросами
Например: можно получить htnl код сайта
В дальнейшем это может пригодиться для парсинга или автоматизации каких-то задач
"""
import requests
import json
from pprint import pprint


def run():
    URL = 'https://github.com/login'
    USERNAME = ''
    PASSWORD = ''

    login_info = (USERNAME, PASSWORD)
    r = requests.get(url=URL, auth=login_info)

    print(r.status_code)
    rj = json.dumps(r.headers.__dict__['_store'])
    pprint(rj)
    # pprint(r.headers)
    print(r.url)
    print(r.request)

