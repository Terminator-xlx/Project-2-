from flask import Blueprint, request, jsonify
from app.services import UserService
from app import db

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return {'message': 'Welcome to Flask API'}


@bp.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()

    if not data or not data.get('username') or not data.get('email'):
        return jsonify({'error': 'Missing username or email'}), 400

    try:
        user = UserService.create_user(
            username=data['username'],
            email=data['email']
        )
        return jsonify(user.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


@bp.route('/api/users', methods=['GET'])
def get_users():
    users = UserService.get_all_users()
    return jsonify([user.to_dict() for user in users])


@bp.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserService.get_user_by_id(user_id)
    if user:
        return jsonify(user.to_dict())
    return jsonify({'error': 'User not found'}), 404


@bp.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if UserService.delete_user(user_id):
        return jsonify({'message': 'User deleted'})
    return jsonify({'error': 'User not found'}), 404


@bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})