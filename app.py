from flask import Flask, request, jsonify

# Init app
app = Flask(__name__)

@app.route('/testic')
def get():
    return jsonify({'testic' : "Hello madafaka"})

# Run Server
if __name__ == '__main__':
    app.run(debug=True)