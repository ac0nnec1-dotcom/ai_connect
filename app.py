from flask import Flask, render_template
import webbrowser
import threading

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/quienes")
def quienes():
    return render_template("quienes.html")

@app.route("/productos")
def productos():
    return render_template("productos.html")

@app.route("/referencias")
def referencias():
    return render_template("referencias.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

@app.route("/carrito")
def carrito():
    return render_template("carrito.html")

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == "__main__":
    threading.Timer(1.5, open_browser).start()
    app.run(debug=True)
