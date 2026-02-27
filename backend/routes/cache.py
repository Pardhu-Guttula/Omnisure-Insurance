# Epic Title: As a system architect, I want to implement caching strategies in both frontend and backend, so that the system can handle a larger number of requests efficiently.

from flask import Blueprint, request, jsonify
import redis

cache_bp = Blueprint('cache', __name__)

# Create a connection to Redis (Ensure Redis is running and accessible)
redis_client = redis.Redis(host='localhost', port=6379, db=0)

@cache_bp.route('/cache', methods=['GET'])
def get_cached_data():
    key = request.args.get('key')

    if not key:
        return jsonify({'error': 'Key is required'}), 400

    value = redis_client.get(key)

    if not value:
        return jsonify({'message': 'Cache miss'}), 200

    return jsonify({'value': value.decode('utf-8')}), 200

@cache_bp.route('/cache', methods=['POST'])
def set_cached_data():
    data = request.get_json()

    key = data.get('key')
    value = data.get('value')
    ttl = data.get('ttl', 3600) # Default TTL is set to 1 hour

    if not key or not value:
        return jsonify({'error': 'Key and value are required'}), 400

    redis_client.setex(key, ttl, value)

    return jsonify({'message': 'Cache set successfully'}), 201

@cache_bp.route('/cache', methods=['DELETE'])
def delete_cached_data():
    key = request.args.get('key')

    if not key:
        return jsonify({'error': 'Key is required'}), 400

    redis_client.delete(key)

    return jsonify({'message': 'Cache deleted successfully'}), 200