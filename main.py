import os
import json
from flask import Flask
from flask import render_template
from flask import send_from_directory
from flask import jsonify
import zip_codes
import weather
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/<zip_code>")
def forecast(zip_code):
	if not zip_codes.is_listed(zip_code):
		return render_template("wrong_zip.html", zip_code=zip_code),404
	city = " / ".join(zip_codes.city(zip_code))
	txt = weather.forecast_txt(zip_code)
	alerts,forecast,meta = weather.parse(txt)
	print(forecast)
	return render_template(
		"forecast.html",
		city=city,
		alerts=alerts,
		forecast=forecast,
		meta=meta
	)

@app.route("/curl/<zip_code>")
def curl(zip_code):
	if not zip_codes.is_listed(zip_code):
		return "Hm, I don't have zip code " + zip_code + "\n",404
	city = " / ".join(zip_codes.city(zip_code))
	txt = weather.forecast_txt(zip_code)
	alerts,forecast,meta = weather.parse(txt)
	print(forecast)
	return render_template(
		"forecast.txt",
		city=city,
		alerts=alerts,
		forecast=forecast,
		meta=meta
	)

@app.route("/api/<zip_code>")
def api(zip_code):
	if not zip_codes.is_listed(zip_code):
	    return json.dumps({"error":"Couldn't find zip code "+zip_code})+"\n",404
	city = " / ".join(zip_codes.city(zip_code))
	txt = weather.forecast_txt(zip_code)
	alerts,forecast,meta = weather.parse(txt)
	print(forecast)
	return jsonify(
	    city=city,
	    alerts=alerts,
	    forecast=[(day, "\u2014".join(text)) for day, text in forecast],
	    meta=meta
	)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html',error=error), 500

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
	    os.path.join(app.root_path, 'static/img'),
            'favicon.ico', mimetype='image/vnd.microsoft.icon'
    )

@app.route('/robots.txt')
def robots():
	return send_from_directory(
		os.path.join(app.root_path, 'static/txt'),
		'robots.txt', mimetype='text/plain'
	    )

if __name__ == "__main__":
    app.run(debug=True)
