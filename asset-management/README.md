# Asset Management Module

## Overview
The Asset Management module handles an organization's assets, including maintenance, repair, and lifecycle management. It ensures proper tracking and management of assets and their maintenance schedules.

## Structure
- **Models**: Define the data structure and relationships.
  - `asset.py`: Represents an asset.
  - `maintenance.py`: Represents a maintenance record for an asset.
- **Controllers**: Handle user requests and interactions.
  - `assets_controller.py`: Manages CRUD operations for assets.
  - `maintenances_controller.py`: Manages CRUD operations for maintenance records.
- **Views**: Define the user interface.
  - `assets/`: Views related to asset management.
  - `maintenances/`: Views related to maintenance management.

## Setup
1. Ensure the database is set up and migrated.
2. Populate initial data if needed.

## Usage
- **Assets**: Manage your organization's assets.
- **Maintenances**: Record and track maintenance activities for assets.

## Endpoints
- `GET /assets`: List all assets.
- `POST /assets`: Create a new asset.
- `GET /assets/<id>`: Show a specific asset.
- `PUT /assets/<id>`: Update an asset.
- `DELETE /assets/<id>`: Delete an asset.

- `GET /maintenances`: List all maintenance records.
- `POST /maintenances`: Create a new maintenance record.
- `GET /maintenances/<id>`: Show a specific maintenance record.
- `PUT /maintenances/<id>`: Update a maintenance record.
- `DELETE /maintenances/<id>`: Delete a maintenance record.
