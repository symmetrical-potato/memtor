from flask import Flask, render_template, send_file
import json

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

@app.route('/test')
def test():

    clouds = []

    with open('../topics/topics.json') as json_data:
        data = json.load(json_data)

        for i in range(5, 0, -1):
            for j in range(len(data[5 - i])):
                clouds.append([i * 10, data[5 - i][j]])

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
        'clouds': clouds
    }

    return render_template('info.html', data=test_data)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)