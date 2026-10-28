from flask import Flask
from controller.auth_controller import auth_bp

app = Flask (__name__)
app.register_blueprint(auth_bp)
app.secret_key = "poder-ser-qualquer-coisa"
app.run(debug=True)