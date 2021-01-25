from flask import Flask
from flask_cors import CORS
import routes

app = Flask(__name__)
CORS(app, resources={r"*": {"origin":"*"}})

routes.route(app)

if __name__ == '__main__':
    app.run()
