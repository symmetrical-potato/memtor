import vk
import requests


import json

import vkapi

session = vk.AuthSession(app_id='6161415', user_login='79992138965', user_password='udisab20')
api = vk.API(session)

list_of_groups_domains = ['cyberleninka']



for domain in list_of_groups_domains:
    data = vkapi.get_json_by_id(api, domain=domain, limit=2000, offset=0)
    with open(domain + '1.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)

