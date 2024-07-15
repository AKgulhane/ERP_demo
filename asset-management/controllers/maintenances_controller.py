from flask import Blueprint, request, jsonify
from models.maintenance import Maintenance
from database import db_session

maintenances_blueprint = Blueprint('maintenances', __name__)

@maintenances_blueprint.route('/maintenances', methods=['GET'])
def get_maintenances():
    maintenances = Maintenance.query.all()
    return jsonify([maintenance.as_dict() for maintenance in maintenances])

@maintenances_blueprint.route('/maintenances/<int:id>', methods=['GET'])
def get_maintenance(id):
    maintenance = Maintenance.query.get(id)
    if maintenance is None:
        return jsonify({'error': 'Maintenance record not found'}), 404
    return jsonify(maintenance.as_dict())

@maintenances_blueprint.route('/maintenances', methods=['POST'])
def create_maintenance():
    data = request.json
    maintenance = Maintenance(date=data['date'], description=data['description'], asset_id=data['asset_id'])
    db_session.add(maintenance)
    db_session.commit()
    return jsonify(maintenance.as_dict()), 201

@maintenances_blueprint.route('/maintenances/<int:id>', methods=['PUT'])
def update_maintenance(id):
    maintenance = Maintenance.query.get(id)
    if maintenance is None:
        return jsonify({'error': 'Maintenance record not found'}), 404
    data = request.json
    maintenance.date = data['date']
    maintenance.description = data['description']
    db_session.commit()
    return jsonify(maintenance.as_dict())

@maintenances_blueprint.route('/maintenances/<int:id>', methods=['DELETE'])
def delete_maintenance(id):
    maintenance = Maintenance.query.get(id)
    if maintenance is None:
        return jsonify({'error': 'Maintenance record not found'}), 404
    db_session.delete(maintenance)
    db_session.commit()
    return '', 204
