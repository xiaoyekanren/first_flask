import os.path

from flask import Flask, render_template
from function.iotdb_example import IoTDBExample

app = Flask(__name__)

iotdb = IoTDBExample()


@app.route('/')
def index():
    iotdb_version = iotdb.query('show version')[0]
    iotdb_version = '-'.join(iotdb_version[1:]) if len(iotdb_version) > 1 else iotdb_version[0]  # 有版本打版本，无版本打报错

    return render_template(
        'bootstrap.html',
        name=123,
        iotdb_version=iotdb_version
    )


@app.route('/hello')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)



