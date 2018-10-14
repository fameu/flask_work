from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World-Famu!'


@app.route("/stock-out")
def order_record():
    return "出库单-测试"


@app.route("/stock-in")
def ship_record():
    return "入库单-测试"


if __name__ == '__main__':
    app.run()