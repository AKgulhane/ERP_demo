from flask import Blueprint, request, jsonify
from models.asset import Asset
from database import db_session

assets_blueprint = Blueprint('assets', __name__)

@assets_blueprint.route('/assets', methods=['GET'])
def get_assets():
    assets = Asset.query.all()
    return jsonify([asset.as_dict() for asset in assets])

@assets_blueprint.route('/assets/<int:id>', methods=['GET'])
def get_asset(id):
    asset = Asset.query.get(id)
    if asset is None:
        return jsonify({'error': 'Asset not found'}), 404
    return jsonify(asset.as_dict())

@assets_blueprint.route('/assets', methods=['POST'])
def create_asset():
    data = request.json
    asset = Asset(name=data['name'], description=data.get('description'), acquisition_date=data['acquisition_date'])
    db_session.add(asset)
    db_session.commit()
    return jsonify(asset.as_dict()), 201

@assets_blueprint.route('/assets/<int:id>', methods=['PUT'])
def update_asset(id):
    asset = Asset.query.get(id)
    if asset is None:
        return jsonify({'error': 'Asset not found'}), 404
    data = request.json
    asset.name = data['name']
    asset.description = data.get('description')
    asset.acquisition_date = data['acquisition_date']
    db_session.commit()
    return jsonify(asset.as_dict())

@assets_blueprint.route('/assets/<int:id>', methods=['DELETE'])
def delete_asset(id):
    asset = Asset.query.get(id)
    if asset is None:
        return jsonify({'error': 'Asset not found'}), 404
    db_session.delete(asset)
    db_session.commit()
    return '', 204
