from flask import Flask, request, jsonify
import json, os, binascii

app = Flask(__name__)

@app.route('/create', methods=['PUT'])
def create():
    return jsonify({'success': 'tudo certo'}), 200

app.run(host="0.0.0.0", port=80)