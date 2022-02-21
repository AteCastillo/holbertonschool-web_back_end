#!/usr/bin/env python3
""" Module of session_auth views
"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_auth():
    """
    handles routes for session authentication
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if email == '' or email is None:
        return jsonify({"error": "email missing"}), 400
    if password == '' or password is None:
        return jsonify({"error": "password missing"}), 400
    users = User.search({"email": email})
    if users == []:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if user.email == email and not user.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401
        else:
            from api.v1.app import auth
            sesh_id = auth.create_session(user.id)
            response = jsonify(user.to_json())
            sesh_name = getenv("SESSION_NAME")
            response.set_cookie(sesh_name, sesh_id)
            return response


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """
    logs out of user session
    """
    from api.v1.app import auth
    logout = auth.destroy_session(request)
    if not logout:
        abort(404)
    return jsonify({}), 200
