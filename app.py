from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def say_hi():
  return {'result': "hellooowwwworld"}

if __name__ == "__main__":
  app.run(debug=True)