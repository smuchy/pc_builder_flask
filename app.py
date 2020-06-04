from pc_builder.views import app
import os

app.secret_key = os.urandom(24)
port = int(os.environ.get("PORT", 5000))
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=True)
