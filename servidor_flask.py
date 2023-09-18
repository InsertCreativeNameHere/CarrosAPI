from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_word():
    carros = []
    with open(nombre_archivo,'r') as archivo:
        for linea in archivo:
            carros.append({"Marca" : linea})
    return jsonify(carros)

@app.route('/carros', methods = ["GET","POST"])
def carros_txt():
    method = request.method
    nombre_archivo = "carros.txt"
    
    if method == "GET":
        carros = []
        with open(nombre_archivo,'r') as archivo:
            for linea in archivo:
                palabras = linea.split(",")
                carros.append({"Marca" : palabras[0], "Color": palabras[1],"Color": palabras[2]})
        return jsonify(carros)
    elif method == "POST":
        data = request.get_json()
        with open(nombre_archivo,'a+') as archivo:
            archivo.write(data.get("Marca") + ',' + data.get("Color") + ',' + data.get("Estado") + '\n')
        return f'El registro ha sido guardado'
    

if __name__ == '__main__':
    app.run(debug=True)