#!/usr/bin/env python3
'''Auth class'''
from flask import request
from typing import List, TypeVar
from models.user import User


class Auth:
    '''Implements the Auth class'''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''checks if path is in excluded paths
        '''
        if path is None:
            return True
        if not excluded_paths:
            return True

        path = path.rstrip('/')
        excluded_paths = [p.rstrip('/') for p in excluded_paths]

        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        '''checks if authorization is in the request header'''
        if request is None or 'Authorization' not in request.headers:
            return None
        else:
            return request.headers['Authorization']

    def current_user(self, request=None) -> User:
        '''current user'''
        return None
