from flask import Flask, render_template, request
from model import makePrediction

app = Flask("__name__")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/output", methods=["POST"])
def output():
    tempRate = float(request.form["tempRate"])
    tempMin = float(request.form["tempMin"])
    tempMax = float(request.form["tempMax"])
    sunshine = float(request.form["sunshine"])
    humidityRate = float(request.form["humidityRate"])
    windSpeedRate = float(request.form["windSpeedRate"])
    mostWind = float(request.form["mostWind"])
    windSpeedMax = float(request.form["windSpeedMax"])
    windOnMaxSpeed = float(request.form["windOnMaxSpeed"])

    output = makePrediction([[tempMin, tempMax, tempRate, humidityRate, sunshine, windSpeedMax, windOnMaxSpeed, windSpeedRate, mostWind]])

    return render_template("output.html", output= int(output))

if __name__ == "__main__":
    app.run(debug=True)