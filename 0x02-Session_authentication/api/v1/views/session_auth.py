#!/usr/bin/env python3
'''New view for Session Authentication'''
from flask import Flask, request, jsonify
from models.user import User
from api.v1.views import app_views
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session_login():
    '''New view for Session Authentication'''

    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    users_list = User.search({'email': email})

    if not users_list:
        return jsonify({"error": "no user found for this email"}), 404

    user = users_list[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    response.set_cookie(getenv('SESSION_NAME', '_my_session_id'), session_id)

    return response
