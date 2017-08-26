import vk
import requests


import json

import vkapi

session = vk.AuthSession(app_id='6161415', user_login='79992138965', user_password='udisab20')
api = vk.API(session)

list_of_groups_domains = ['pn6']



for domain in list_of_groups_domains:
    step = 5000

    for i in range(0, 100000, step):
        data = vkapi.get_json_by_id(api, domain=domain, limit=i + step, offset=i)

        with open(domain + str(i // step) + '.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)

