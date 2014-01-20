from flask import Flask
from flask import render_template
import zip_codes
import weather
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/<zip_code>")
def forecast(zip_code):
	if not zip_codes.is_listed(zip_code):
		return render_template("wrong_zip.html", zip_code=zip_code)
	city = "/".join(zip_codes.city(zip_code))
	txt = weather.forecast_txt(zip_code)
	forecast = weather.parse(txt)
	print(forecast)
	return render_template("forecast.html",city=city,forecast=forecast)

if __name__ == "__main__":
    app.run(debug=True)