from pprint import pformat

from flask import Flask, render_template, request

from generador import Concatenacion, GenerarCadenas, Pertenece, Union, kleenePlus, kleeneStar

app = Flask(__name__)


OP_LABELS = {
    "generar": "Generar Cadenas",
    "pertenece": "Pertenencia",
    "union": "Union",
    "concatenacion": "Concatenacion",
    "kleene_star": "Kleene Star",
    "kleene_plus": "Kleene Plus",
    "crecimiento": "Crecimiento del Lenguaje",
}


def parse_lista(raw_value: str):
    return [item.strip() for item in raw_value.split(",") if item.strip()]


@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    titulo_resultado = None
    error = None

    if request.method == "POST":
        operacion = request.form.get("operation", "").strip()
        titulo_resultado = OP_LABELS.get(operacion, "Operacion")

        try:
            if operacion == "generar":
                alfabeto = parse_lista(request.form.get("alfabeto", ""))
                max_len = int(request.form.get("max_len", "0"))
                resultado = GenerarCadenas(alfabeto, max_len)

            elif operacion == "pertenece":
                cadena = request.form.get("cadena", "")
                lenguaje = parse_lista(request.form.get("lenguaje", ""))
                resultado = Pertenece(cadena, lenguaje)

            elif operacion == "union":
                l1 = parse_lista(request.form.get("l1_union", ""))
                l2 = parse_lista(request.form.get("l2_union", ""))
                resultado = Union(l1, l2)

            elif operacion == "concatenacion":
                l1 = parse_lista(request.form.get("l1_concat", ""))
                l2 = parse_lista(request.form.get("l2_concat", ""))
                resultado = Concatenacion(l1, l2)

            elif operacion == "kleene_star":
                lenguaje = parse_lista(request.form.get("lenguaje_ks", ""))
                max_iter = int(request.form.get("max_iter_ks", "0"))
                resultado = kleeneStar(lenguaje, max_iter)

            elif operacion == "kleene_plus":
                lenguaje = parse_lista(request.form.get("lenguaje_kp", ""))
                max_iter = int(request.form.get("max_iter_kp", "0"))
                resultado = kleenePlus(lenguaje, max_iter)

            elif operacion == "crecimiento":
                lenguaje = parse_lista(request.form.get("lenguaje_crecimiento", ""))
                filas = []
                for i in range(1, 6):
                    cantidad = len(kleeneStar(lenguaje, i))
                    filas.append({"iteracion": i, "cantidad": cantidad})
                resultado = filas

            else:
                error = "Operacion no valida."

        except ValueError:
            error = "Revisa los campos numericos."
        except Exception as exc:
            error = f"Error: {exc}"

    resultado_texto = pformat(resultado, width=100) if resultado is not None else None

    return render_template(
        "index.html",
        resultado=resultado,
        resultado_texto=resultado_texto,
        titulo_resultado=titulo_resultado,
        error=error,
        form_data=request.form,
    )


if __name__ == "__main__":
    app.run(debug=True)
