import json


def get_from_cache(handle):
    with open('cache.json', mode='r', encoding='utf-8') as cached:
        cache = json.load(cached)
        for c in cache:
            if handle in c:
                return c[handle]
        else:
            return None


def put_in_cache(handle, data):

    with open('cache.json', encoding='utf-8') as cached:
        older = json.load(cached)

    entry = dict()
    entry[handle] = data
    older.append(entry)

    print(older)

    with open('cache.json', mode='w', encoding='utf-8') as cached:
        json.dump(older, cached)