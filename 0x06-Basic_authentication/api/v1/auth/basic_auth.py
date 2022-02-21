#!/usr/bin/env python3
"""
basic auth class inherits from auth
"""
from api.v1.auth.auth import Auth
from base64 import b64encode, b64decode
from models.user import User
from models.base import DATA
from typing import TypeVar


class BasicAuth(Auth):
    """
    inherits from auth
    """
    def extract_base64_authorization_header(
            self, authorization_header: str
            ) -> str:
        """
        returns the base64 part for authorization
        """
        if authorization_header is None or type(authorization_header) != str:
            return (None)
        if authorization_header[0:6] != "Basic ":
            return (None)

        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str
            ) -> str:
        """
        decoded value of base64 str
        """
        if base64_authorization_header is None or type(
                base64_authorization_header
                ) != str:
            return (None)

        try:
            return b64decode(base64_authorization_header,
                             None, False).decode('UTF-8')
        except Exception:
            return (None)

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str
            ) -> (str, str):
        """
        extracts user email and password
        """
        if decoded_base64_authorization_header is None or type(
                decoded_base64_authorization_header
                ) != str:
            return (None, None)

        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        else:
            return decoded_base64_authorization_header.split(':', 1)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str
            ) -> TypeVar('User'):
        """
        returns the user instance of email and password
        """
        if user_email is None or type(user_email) != str:
            return (None)
        if user_pwd is None or type(user_pwd) != str:
            return (None)
        if not DATA.get('User'):
            return (None)
        for user in User.search({"email": user_email}):
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        final method for basic authentication
        """
        auth_header = super().authorization_header(request)
        if auth_header is None:
            return (None)
        else:
            extract_hdr = self.extract_base64_authorization_header(auth_header)
            decod_hdr = self.decode_base64_authorization_header(extract_hdr)
            extrct_usr, passwd = self.extract_user_credentials(decod_hdr)
            user = self.user_object_from_credentials(extrct_usr, passwd)
            return (user)
