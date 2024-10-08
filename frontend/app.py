from flask import Flask, request, render_template, redirect, url_for
import requests
from multiprocessing import Process, Value
import time

app = Flask(__name__, template_folder="templates")

loop_flag = Value('b', True)

def make_requests(loop_flag):
    while loop_flag.value:
        url = "http://backend:5000/backend"
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            response = response.json()
            print(response)

process = None

@app.route("/", methods=["POST", "GET"])
def index():
    global process
    if request.method == "GET":
        if not process or not process.is_alive():
            state = "esperando"
        else:
            state = "enviado"
        return render_template("index.html", state=state)
    
    elif request.method == "POST":
        if not process or not process.is_alive():
            loop_flag.value = True
            process = Process(target=make_requests, args=(loop_flag,))
            process.start()
        return redirect(url_for("index"))

@app.route("/stop", methods=["POST"])
def stop():
    global process
    if process and process.is_alive():
        loop_flag.value = False
        process.terminate()
        process.join()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)