from flask import Flask, render_template, request
app = Flask(__name__)


record_list = []
company_dict = {1:"HUAWEI", 2:"HP", 3:"Inspur"}
product_dict = {1:"DDR4-2400",2:"DDR4-3000",3:"DDR4-3200"}

@app.route("/stock/in", methods=["GET", "POST"])
def stock_in():
    postData = request.form
    print(postData)
    getData = request.args
    print(getData)

    if request.method == "POST":
        cid = int(request.form["company"])
        pid = int(request.form["product"])
        record_list.append({"company":company_dict[cid], "product":product_dict[pid]})
    return render_template("stock_in.html", title="入库记录", record_list=record_list, company_dict=company_dict, product_dict=product_dict)


@app.route("/stock/out")
def stock_out():
    return render_template("stock_out.html", title="出库记录")


print(app.url_map)

if __name__ == '__main__':
    app.run(debug=True)