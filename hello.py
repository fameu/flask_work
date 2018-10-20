from flask import Flask, render_template, request
from db.database import *
import time
import models.user
import models.company
import models.product
import models.stockin
import models.stockout

app = Flask(__name__)

@app.teardown_appcontext
def shutdownSession(exception=None):
    dbSession.remove()

@app.route("/")
def index():
    return render_template("index.html", title="出入库管理")

@app.route("/user/add", methods=["GET", "POST"])
def userAdd():
    model = models.user.User
    postData = request.form

    if request.method == "POST":
        name = postData["name"]
        uob = model(name)
        dbSession.add(uob)
        dbSession.commit()

    context = {
        "title"     : "成员",
        "userList"  : model.query.all(),
    }
    return render_template("user.html", **context)

@app.route("/product/add", methods=["GET", "POST"])
def productAdd():
    model = models.product.Product
    postData = request.form
    if request.method == "POST":
        name = postData["name"]
        info = postData["info"]
        pob = model(name, info)
        dbSession.add(pob)
        dbSession.commit()

    context = {
        "title"         : "产品",
        "productList"   : model.query.all()
    }
    return render_template("product.html", **context)

@app.route("/company/add", methods=["GET", "POST"])
def companyAdd():
    model = models.company.Company
    postData = request.form
    if request.method == "POST":
        name = postData["name"]
        pob = model(name)
        dbSession.add(pob)
        dbSession.commit()

    context = {
        "title"         : "产品",
        "companyList"   : model.query.all()
    }
    return render_template("company.html", **context)

@app.route("/stock/in", methods=["GET", "POST"])
def stockIn():
    model = models.stockin.StockIn
    postData = request.form

    if request.method == "POST":
        uid = int(postData["user"])
        cid = int(postData["company"])
        pid = int(postData["product"])
        cnt = int(postData["cnt"])
        siob = model(uid, pid, cid, cnt)
        dbSession.add(siob)
        dbSession.commit()

    context = {
        "title": "产品",
        "stockInList": model.query.all(),
        "userList" : models.user.User.query.all(),
        "companyList": models.company.Company.query.all(),
        "productList": models.product.Product.query.all(),
    }
    return render_template("stockIn.html", **context)

@app.route("/stock/out", methods=["GET", "POST"])
def stockOut():
    model = models.stockin.StockOut
    postData = request.form


    if request.method == "POST":
        uid = int(postData["user"])
        cid = int(postData["company"])
        pid = int(postData["product"])
        cnt = int(postData["cnt"])
        soob = model(uid, pid, cid, cnt)
        dbSession.add(soob)
        dbSession.commit()

    context = {
        "title": "产品",
        "stockOutList": model.query.all(),
        "userList": models.user.User.query.all(),
        "companyList": models.company.Company.query.all(),
        "productList": models.product.Product.query.all(),
    }
    return render_template("stockOut.html", **context)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)