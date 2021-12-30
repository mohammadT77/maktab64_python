from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['get'])
def home_view():
    name = request.args['name']
    return f"Hello {name}!"


if __name__ == '__main__':
    app.run()
