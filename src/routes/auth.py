from flask import request, jsonify

from app import app, login_manager
from database import db
from flask_login import login_user, logout_user, login_required

from entities.user import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.post('/login')
def login():
    data = request.json

    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"message": "E-mail ou senha inválidos"}), 400

    if user.password != password:
        return jsonify({"message": "E-mail ou senha inválidos"}), 400

    login_user(user)

    return jsonify({"message": "Login realizado com sucesso"})


@app.post('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout realizado com sucesso"})


@app.post('/register')
def register_user():
    data = request.json

    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if user:
        return jsonify({"message": "E-mail já utilizado"}), 409

    user = User(name, email, password)

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "Usuário criado com sucesso"}), 201
