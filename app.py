import os
from flask import Flask
from routes import routes
import logging

def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes)

    logging.basicConfig(level=logging.INFO)  
    return app

app = create_app() 
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)