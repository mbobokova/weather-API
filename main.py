from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
stations_info = pd.read_csv("data_small/stations.txt",
                 skiprows=17)
stations_info = stations_info[['STAID', 'STANAME                                 ']]


@app.route("/")
def home():
    return render_template("home.html", stations_info=stations_info.to_html())


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = f"data_small/TG_STAID{str(station).zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {"station": station,
            "date": date,
            "temperature": temperature}


if __name__ == '__main__':
    app.run(debug=True, port=5001)