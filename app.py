from flask import Flask, request, jsonify

# Init app
app = Flask(__name__)

@app.route('/')
def get():
    return "Hello World"

# Run Server
if __name__ == '__main__':
    app.run(debug=True)