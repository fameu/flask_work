# -*- coding: gbk -*-
# @Time    : 2019/2/22 16:32
# @Author  : famu
# @File    : hello1.py
# @Software: PyCharm

from flask import Flask, render_template, request
import model.product

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="出入库管理")

@app.route("/product/add", methods=["GET", "POST"])
def productAdd():
	postData = request.form
	if request.method == "POST":
		data = {}
		data["name"] = postData["name"]
		data["info"] = postData["info"]
		model.product.g_Products.NewProduct(data)

	context = {
		"title"         : "产品",
		"productList"   : model.product.g_Products.Products
	}
	return render_template("product.html", **context)

if __name__ == '__main__':
	app.run(debug=True)