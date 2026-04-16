import os
from flask import Flask, redirect
from config import SECRET_KEY
from controllers.auth_controller import auth

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), 'views', 'templates'),
    static_folder=os.path.join(os.path.dirname(__file__), 'static')
)
app.secret_key = SECRET_KEY

app.register_blueprint(auth)

@app.route('/')
def home():
    return redirect('/login')

if __name__ == "__main__":
    app.run(debug=True, port=5001)