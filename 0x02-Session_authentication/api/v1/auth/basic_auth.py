#!/usr/bin/env python3
'''Basic auth'''
from .auth import Auth
import base64
from typing import Tuple
from models.user import User


class BasicAuth(Auth):
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        '''returns the Base64 part of the Authorization
        header for a Basic Authentication
        '''
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        '''returns the decoded value of a Base64 string'''
        if not base64_authorization_header:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_header = base64.b64decode(base64_authorization_header)
            return decoded_header.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        '''returns the user email and password from the Base64 decoded value'''
        if not decoded_base64_authorization_header:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        user_credentials = decoded_base64_authorization_header.split(':')
        return user_credentials[0], user_credentials[1]

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> User:
        '''returns the User instance based on his email and password'''
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None

        users_list = User.search({'email': user_email})

        if not users_list:
            return None

        for user in users_list:
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> User:
        '''overloads Auth and retrieves the User instance for a request'''
        if request is None:
            return None

        # Extract the authorization header
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        # Extract the base64 part
        base64_auth_header = self.extract_base64_authorization_header(
            auth_header)
        if base64_auth_header is None:
            return None

        # Decode Base64 part
        decoded_base64_auth_header = self.decode_base64_authorization_header(
            base64_auth_header)
        if decoded_base64_auth_header is None:
            return None

        # Extract the user credentials
        user_email, user_pwd = self.extract_user_credentials(
            decoded_base64_auth_header)
        if not user_email or not user_pwd:
            return None

        # Get user object
        user_obj = self.user_object_from_credentials(user_email, user_pwd)

        return user_obj
