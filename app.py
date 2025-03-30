import json
import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
CONFIG_FILE = "config.json"

#functions that handle the config file
def load_config():
    if not os.path.exists(CONFIG_FILE):
        save_config({"sammlung1": "SAMMLUNG 1", "sammlung2": "SAMMLUNG 2"})
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_config(data):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


#routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/config", methods=["GET", "POST"])
def config():
    config_data = load_config()

    if request.method == "POST":
        config_data["sammlung1"] = request.form.get("sammlung1", "SAMMLUNG 1")
        config_data["sammlung2"] = request.form.get("sammlung2", "SAMMLUNG 2")
        save_config(config_data)
        return redirect("/")

    return render_template("config.html",
                           sammlung1=config_data["sammlung1"],
                           sammlung2=config_data["sammlung2"])

@app.route("/tablet1")
def tablet1():
    config_data = load_config()
    return render_template("tablet1.html", text=config_data["sammlung1"])

@app.route("/tablet2")
def tablet2():
    config_data = load_config()
    return render_template("tablet2.html", text=config_data["sammlung2"])

if __name__ == "__main__":
    app.run(debug=True)
