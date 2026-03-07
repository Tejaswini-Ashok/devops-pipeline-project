from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "healthy",
        "message": "DevOps Pipeline is Running",
        "timestamp": str(datetime.datetime.now())
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "ok",
        "uptime": "running"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)