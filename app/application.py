from flask import Flask, render_template, send_file

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():

    data = {
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
        }
    }

    return render_template('info.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)