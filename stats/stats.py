import json
from datetime import datetime as dt
from datetime import timedelta

def average(array):
    res = 0
    for num in array:
        res += num
    return res / len(array)


def get_stat(posts, metric, days=1, date_for_start=None):
    iterator = iter(posts)
    post = next(iterator)

    array_for_stat = [post[metric]]

    if not date_for_start:
        date_for_start = dt.today()

    while date_for_start < dt.strptime(post['date'], '%Y-%m-%dT%H:%M:%SZ'):
        post = next(iterator)

    while dt.strptime(post['date'], '%Y-%m-%dT%H:%M:%SZ') > date_for_start - timedelta(days=days):
        post = next(iterator)
        array_for_stat.append(post[metric])
    return average(array_for_stat)


def get_all_stats(posts):
    result = {}

    result['average_likes_per_day'] = (get_stat(posts, 'likesCount', 1) +
                                       get_stat(posts, 'likesCount', 1, date_for_start=dt.today() - timedelta(days=1)) +
                                       get_stat(posts, 'likesCount', 1, date_for_start=dt.today() - timedelta(days=2))) / 3
    result['average_likes_per_week'] = get_stat(posts, 'likesCount', 7)
    result['average_likes_per_month'] = get_stat(posts, 'likesCount', 30)

    result['average_reposts_per_day'] = (get_stat(posts, 'repostsCount', 1) +
                                         get_stat(posts, 'repostsCount', 1, dt.today() - timedelta(days=1)) +
                                         get_stat(posts, 'repostsCount', 1, dt.today() - timedelta(days=2))) / 3
    result['average_reposts_per_week'] = get_stat(posts, 'repostsCount', 7)
    result['average_reposts_per_month'] = get_stat(posts, 'repostsCount', 30)

    result['average_comments_per_day'] = (get_stat(posts, 'commentsCount', 1) +
                                          get_stat(posts, 'commentsCount', 1, dt.today() - timedelta(days=1)) +
                                          get_stat(posts, 'commentsCount', 1, dt.today() - timedelta(days=2))) / 3
    result['average_comments_per_week'] = get_stat(posts, 'commentsCount', 7)
    result['average_comments_per_month'] = get_stat(posts, 'commentsCount', 30)

    return result