from flask import Flask, render_template,url_for,request,redirect
import controlador, controlador2

app = Flask(__name__)

@app.route('/')
def paginaPrincipal():
    return render_template("paginaPrincipal.html")


@app.route('/index')
def index():
    customers = controlador.get_clientes()
    return render_template('index.html', customers=customers)

@app.route('/form_add_cliente')
def form_add_cliente():
    return render_template('add_cliente.html')

@app.route('/edit_cliente<int:id>')
def edit_cliente(id):
    customer = controlador.get_cliente_id(id)
    return render_template('edit_cliente.html', customer=customer)

@app.route('/update_cliente', methods=['POST'])
def update_cliente():
    id = request.form['id']
    name = request.form['name']
    status = request.form['status']
    mobile = request.form['mobile']
    controlador.update_cliente(name, status, mobile, id)
    return redirect('/index')    

@app.route('/delete_cliente', methods=["POST"])
def delete_cliente():
    controlador.delete_cliente(request.form["id"])
    return redirect("/index")

@app.route("/save_cliente", methods=["POST"])
def save_cliente():
    name = request.form['name']
    status = request.form['status']
    mobile = request.form['mobile']
    controlador.add_cliente(name, status, mobile)
    return redirect("/index")  





@app.route('/index2')
def index2():
    facturas = controlador2.get_facturas()
    return render_template('index2.html', facturas=facturas)

@app.route('/form_add_factura')
def form_add_factura():
    return render_template('add_factura.html')

@app.route('/save_factura', methods=['POST'])
def save_factura():
    date = request.form["date"]
    id = request.form["id"]
    price = request.form["price"]
    balance = request.form["balance"]
    controlador2.add_factura(date, price, balance, id)
    return redirect("/index2")

@app.route('/edit_factura/<int:number>')
def edit_factura(number):
    factura = controlador2.get_facturas_number(number)
    return render_template('edit_factura.html', factura=factura)

@app.route('/update_factura', methods=['POST'])
def update_factura():
    number = request.form["number"]
    date = request.form["date"]
    price = request.form["price"]
    balance = request.form["balance"]
    controlador2.update_factura(date, price, balance, number)
    return redirect("/index2")

@app.route('/delete_factura', methods=["POST"])
def delete_factura():
    balance = request.form['balance']
    balances = int(balance)
    if balances == 0:
        controlador2.delete_factura(request.form["number"])
    else:
        return ("No se pudo eliminar la factura por el saldo")
    return redirect("/index2")


if __name__ == "__main__":
    app.run(port = 3000, debug=None)