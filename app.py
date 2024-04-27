from flask import Flask, render_template, request
from country import get_country_data

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    country_data = None
    capital_enabled = None
    region_enabled = None
    population_enabled = None
    area_enabled = None
    land_enabled = None
    if request.method == "POST":
        country_name = request.form.get("country_name")
        capital_enabled = request.form.get("capital")
        region_enabled = request.form.get("region")
        population_enabled = request.form.get("population")
        area_enabled = request.form.get("area")
        land_enabled = request.form.get("landlock")
        print(population_enabled)
        country_data = get_country_data(country_name)
        return render_template(
            "index.html",
            country_data=country_data,
            capital=capital_enabled,
            region=region_enabled,
            population=population_enabled,
            area=area_enabled,
            landlock=land_enabled,
        )
    else:
        return render_template(
            "index.html",
            country_data=country_data,
            capital=capital_enabled,
            region=region_enabled,
            population=population_enabled,
            area=area_enabled,
            llock=land_enabled,
        )


if __name__ == "__main__":
    app.run(debug=True)
