from flask import Flask, render_template, request
from calculator import calculate_score
from data import universities

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        gpa = float(request.form["gpa"])
        ielts = float(request.form["ielts"])
        korean = int(request.form["korean"])
        projects = int(request.form["projects"])

        result = calculate_score(
            gpa,
            ielts,
            korean,
            projects
        )

    return render_template(
        "index.html",
        result=result,
        universities=universities
    )


if __name__ == "__main__":
    app.run(debug=True)