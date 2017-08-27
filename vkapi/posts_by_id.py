import vk
import time
import datetime

# ! Required to use either owner_id or domain !
def get_posts_by_id(api_obj, owner_id=None, domain=None, limit=1000, offset=0):

    count_of_posts = api_obj.wall.get(owner_id=owner_id, domain=domain, count=1)[0]

    i = offset
    posts = []
    while i < count_of_posts and i < limit:
        step = min(count_of_posts - i, 5)
        # count_of_posts = data_load.wall.get(owner_id=owner_id, domain=domain, count=1)[0]

        posts += api_obj.wall.get(owner_id=owner_id, domain=domain, offset=i, count=step)[1:]

        # print(e.keys())
        time.sleep(5)

        i += step

    return posts


# First iteration getter
def get_json_by_id(api_obj, owner_id=None, domain=None, limit=1000, offset=0):
    result = []

    posts = get_posts_by_id(api_obj, owner_id, domain, limit, offset)

    for post in posts:
        obj = {}

        obj['mediaLinks'] = []
        if 'attachment' in post.keys():
            for attach in post['attachments']:
                if attach['type'] == 'photo':
                    obj['mediaLinks'].append(attach['photo']['src_big'])

        obj['text'] = ''
        if 'text' in post.keys():
            obj['text'] = post['text']

        if 'marked_as_ads' in post.keys():
            obj['ad'] = post['marked_as_ads']

        obj['date'] = datetime.datetime.fromtimestamp(post['date']).strftime(('%Y-%m-%dT%H:%M:%SZ'))
        obj['ad'] = 0
        obj['commentsCount'] = post['comments']['count']
        obj['likesCount'] = post['likes']['count']
        obj['repostsCount'] = post['reposts']['count']

        result.append(obj)
    return result


