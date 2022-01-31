from flask import Flask, render_template, request, redirect
from usuarios import Usuarios

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/nuevoUsuario", methods=["POST"])
def agregarUsuario():
    datosUsuarios ={
        "nombre" : request.form["nombre"],
        "apellido" : request.form["apellido"],
        "email" : request.form["email"] 
    }
    Usuarios.guardar( datosUsuarios )
    return redirect('/listaUsuarios')

@app.route('/listaUsuarios', methods=['GET'])
def listaUsuario():
    usuarios = Usuarios.seleccionar()
    print(usuarios)
    return render_template("lista.html", all_usuarios = usuarios)



if __name__ == "__main__":
    app.run(debug=True)