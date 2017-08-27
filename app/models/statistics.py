import vk
from credentials import credentials as crd
from vkapi.posts_by_id import get_json_by_id
from stats.stats import get_all_stats as get_stats


def get_info_by_domain(domain="test"):


    print('>>>>>>>>>>>>>', domain)
    session = vk.AuthSession(**crd)
    api_obj = vk.API(session)

    posts = get_json_by_id(api_obj, domain=domain)
    stats = get_stats(posts)

    rsp = api_obj.wall.get(domain=domain, extended=1)




    group = rsp['groups'][0]

    print('>>', group)
    name = group['name']
    link = group['screen_name']
    img_link = group['photo_big']



    return stats, name, link, img_link
