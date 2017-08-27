from flask import Flask, render_template, send_file
import json
from app.models.statistics import get_info_by_domain
from app.caching import get_from_cache, put_in_cache

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/stuff')
def stuff():
    with open('../topics/topics.json') as json_data:
        data = json.load(json_data)

    for d in data:
        print(d)

    return '1'


@app.route('/info/<string:com_handle>')
def com_info(com_handle):
    in_cache = get_from_cache(com_handle)
    if in_cache is None:
        stats, name, link, img_link = get_info_by_domain(com_handle)
        print(stats['average_likes_per_month'])
        print(stats['average_likes_per_week'])
        print(stats['average_likes_per_day'])


        data = {
            'name': name,
            'link': link,
            'img_link': img_link,
            'median_likes': {
                'month': stats['average_likes_per_month'],
                'week': stats['average_likes_per_week'],
                'day': stats['average_likes_per_day']
            },
            'median_comments': {
                'month': stats['average_comments_per_month'],
                'week': stats['average_comments_per_week'],
                'day': stats['average_comments_per_day']
            },
            'median_reposts': {
                'month': stats['average_reposts_per_month'],
                'week': stats['average_reposts_per_week'],
                'day': stats['average_reposts_per_day']
            }
        }

        put_in_cache(com_handle, data)
    else:
        data = in_cache

    with open('images_paths.json', encoding='utf-8') as images_paths_json:
        images_paths = json.load(images_paths_json)
        for com in images_paths:
            if com_handle in com:
                data['pics'] = com[com_handle]

    return render_template('info.html', data=data)


@app.route('/test')
def test():

    clouds = []

    with open('../topics/topics.json') as json_data:
        data = json.load(json_data)

        for i in range(5, 0, -1):
            for j in range(len(data[5 - i])):
                clouds.append([i * 10, data[5 - i][j]])

    with open('test_images_paths.json') as pic_paths:
        paths = json.load(pic_paths)

    print(clouds)

    test_data = {
        'name': "Testers community",
        'description': 'Community for true tester of everything and everywhere!',
        'link': 'example',
        'median_likes': {
            'month': 30,
            'two_weeks': 39,
            'one_week': 45
        },
        'median_comments': {
            'month': 12,
            'two_weeks': '19',
            'one_week': 22
        },
        'median_reposts': {
            'month': '22',
            'two_weeks': '18',
            'one_week': '24'
        },
        'general': {
            'posts_freq': '41/week',
            'avg_post_len': '244'
        },
        'clouds': clouds,
        'pics': paths
    }

    return render_template('info.html', data=test_data)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)