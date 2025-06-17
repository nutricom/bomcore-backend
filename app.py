from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "temporary_secret"  # Needed for session management

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    session["rfq"] = {
        "email": request.form["email"],
        "part": request.form["part"],
        "quantity": request.form["quantity"],
        "spec": request.form["spec"]
    }
    return redirect(url_for("preview"))

@app.route("/preview", methods=["GET"])
def preview():
    rfq = session.get("rfq", {
        "email": "n/a",
        "part": "n/a",
        "quantity": "n/a",
        "spec": "n/a"
    })
    return render_template("preview.html", rfq=rfq)

@app.route("/thanks")
def thanks():
    return render_template("thanks.html")

@app.route("/healthz")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)
