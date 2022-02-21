#!/usr/bin/env python3
"""
Authentication system
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth():
    """
    Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        public method require auth
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return (True)

        slash = "/"
        if path[-1] != slash:
            path += slash

        for ex_path in excluded_paths:
            if ex_path[-1] == '*':
                ex_path = ex_path[0:-1]

            if ex_path in path:
                return False

        if path in excluded_paths:
            return (False)
        else:
            return (True)

    def authorization_header(self, request=None) -> str:
        """
        public method authorization header
        """
        authorize = 'Authorization'
        if request is None or request.headers.get(authorize) is None:
            return None

        return request.headers.get(authorize)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        public method current user
        """
        return (None)

    def session_cookie(self, request=None):
        """
        returns asession cookie
        """
        if request is None:
            return None
        sesh_name = getenv("SESSION_NAME")
        return request.cookies.get(sesh_name)
