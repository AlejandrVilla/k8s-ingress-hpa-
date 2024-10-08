from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route("/backend", methods=["GET"])
@cross_origin()
def get_info():
    data = {
        "request type": request.method,
        "info": "Succesfull"
    }
    print("Get request")
    response = jsonify(data)
    response.status_code = 200
    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)