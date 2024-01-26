from flask import request, jsonify

from app import app
from database import db
from flask_login import login_required, current_user

from entities.meal import Meal


@app.post('/meal')
@login_required
def create_meal():
    data = request.json

    name = data.get("name")
    description = data.get("description")
    is_diet = data.get("is_diet")
    ate_at = data.get("ate_at")

    user_id = current_user.id
    meal = Meal(name, is_diet, user_id, ate_at, description)

    db.session.add(meal)
    db.session.commit()

    return jsonify({"message": "Refeição criada com sucesso"}), 201


@app.put('/meal/<int:meal_id>')
@login_required
def edit_meal(meal_id):
    data = request.json

    name = data.get('name')
    description = data.get('description')
    is_diet = data.get('is_diet')
    ate_at = data.get('ate_at')

    user_id = current_user.id

    meal = Meal.query.filter_by(id=meal_id).first()

    if not meal:
        return jsonify({"message": "Refeição não encontrada"}), 404

    if meal.owner_id != user_id:
        return jsonify({"message": "Refeição sem autorização"}), 401

    if name:
        meal.name = name

    if description:
        meal.description = description

    if is_diet:
        meal.is_diet = is_diet

    if ate_at:
        meal.ate_at = ate_at

    db.session.commit()

    return jsonify({"message": "Refeição editada com sucesso"}), 200


@app.get('/meal/<int:meal_id>')
@login_required
def get_meal(meal_id):
    user_id = current_user.id
    meal: Meal = Meal.query.filter_by(id=meal_id).first()

    if not meal:
        return jsonify({"message": "Refeição não encontrada"}), 404

    if meal.owner_id != user_id:
        return jsonify({"message": "Refeição sem autorização"}), 401

    return jsonify({"meal": meal.to_json()}), 200


@app.get('/meal')
@login_required
def fetch_meals():
    user_id = current_user.id
    meals = Meal.query.filter_by(owner_id=user_id).all()

    return jsonify({"meals": [m.to_json() for m in meals]}), 200


@app.delete('/meal/<int:meal_id>')
@login_required
def delete_meal(meal_id):
    user_id = current_user.id
    meal = Meal.query.filter_by(id=meal_id).first()

    if not meal:
        return jsonify({"message": "Refeição não encontrada"}), 404

    if meal.owner_id != user_id:
        return jsonify({"message": "Refeição sem autorização"}), 401

    db.session.delete(meal)
    db.session.commit()

    return jsonify({"message": "Refeição removida com sucesso"}), 200
