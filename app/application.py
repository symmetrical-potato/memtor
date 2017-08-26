from flask import Flask, render_template, send_file

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('info.html',
                           name="Testers community",
                           description="Community for true tester of everything and everywhere!")

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)