from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def logger():
    app.logger.warning('METHOD: %s', request.method)
    app.logger.warning('HEADERS: %s', request.headers)
    app.logger.warning('QUERY_PARAMS: %s', request.args)
    app.logger.warning('POST_DATA: %s', request.data)
    return 'OK'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
