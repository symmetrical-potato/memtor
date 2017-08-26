from flask import Flask, render_template, send_file

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<string:file_name>')
def serve_static(file_name):
    app.logger.info(file_name)
    return send_file('static/' + file_name)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
    # print(app.url_map)