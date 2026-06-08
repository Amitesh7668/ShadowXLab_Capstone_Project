from flask import Flask
import socket
import datetime
import os

app = Flask(__name__)

APP_NAME = "ShadowXLab Cyber Learning Portal"
APP_VERSION = os.getenv("APP_VERSION", "v1.0")
APP_ENV = os.getenv("APP_ENV", "production")

@app.route("/")
def home():
    hostname = socket.gethostname()
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return f"""
    <html>
    <head>
        <title>{APP_NAME}</title>
        <style>
            body {{
                font-family: Arial;
                background-color: #0f172a;
                color: white;
                text-align: center;
                padding-top: 80px;
            }}
            .box {{
                background-color: #1e293b;
                padding: 30px;
                border-radius: 12px;
                width: 60%;
                margin: auto;
            }}
        </style>
    </head>
    <body>
        <div class="box">
            <h1>{APP_NAME}</h1>
            <h2>Version: {APP_VERSION}</h2>
            <p><b>Hostname:</b> {hostname}</p>
            <p><b>Date/Time:</b> {current_time}</p>
            <p><b>Environment:</b> {APP_ENV}</p>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return "Application is healthy", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
