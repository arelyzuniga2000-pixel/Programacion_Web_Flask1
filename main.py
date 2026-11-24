from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    if request.method == "POST":

        try:
            nota1 = float(request.form["nota1"])
            nota2 = float(request.form["nota2"])
            nota3 = float(request.form["nota3"])
            asistencia = float(request.form["asistencia"])

        except (ValueError, KeyError):
            return render_template(
                "ejercicio1.html",
                error="Ingresa todos los datos correctamente."
            )

        if not all(10 <= nota <= 70 for nota in [nota1, nota2, nota3]):
            return render_template(
                "ejercicio1.html",
                error="Las notas deben estar entre 10 y 70."
            )

        if not 0 <= asistencia <= 100:
            return render_template(
                "ejercicio1.html",
                error="La asistencia debe estar entre 0 y 100."
            )

        promedio = (nota1 + nota2 + nota3) / 3

        if promedio >= 40 and asistencia >= 75:
            estado = "Aprobado"
        else:
            estado = "Reprobado"

        resultado = {
            "titulo": "Resultado del ejercicio 1",
            "detalle": f"Promedio: {promedio:.2f}",
            "estado": estado,
            "extra": f"Asistencia: {asistencia:.1f}%"
        }

        return render_template(
            "resultado.html",
            resultado=resultado
        )

    return render_template("ejercicio1.html")


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    if request.method == "POST":

        nombres = [
            request.form.get("nombre1", "").strip(),
            request.form.get("nombre2", "").strip(),
            request.form.get("nombre3", "").strip()
        ]

        if any(not nombre for nombre in nombres):
            return render_template(
                "ejercicio2.html",
                error="Debes ingresar los tres nombres."
            )

        if len(set(nombre.casefold() for nombre in nombres)) != 3:
            return render_template(
                "ejercicio2.html",
                error="Los tres nombres deben ser diferentes."
            )

        mayor_largo = max(len(nombre) for nombre in nombres)

        nombres_mas_largos = [
            nombre for nombre in nombres
            if len(nombre) == mayor_largo
        ]

        resultado = {
            "titulo": "Resultado del ejercicio 2",
            "detalle": (
                    "Nombre con mayor cantidad de caracteres: "
                    + ", ".join(nombres_mas_largos)
            ),
            "estado": f"Cantidad de caracteres: {mayor_largo}",
            "extra": "Se muestran todos los nombres en caso de empate."
        }

        return render_template(
            "resultado.html",
            resultado=resultado
        )

    return render_template("ejercicio2.html")


if __name__ == "__main__":
    app.run(debug=True)
