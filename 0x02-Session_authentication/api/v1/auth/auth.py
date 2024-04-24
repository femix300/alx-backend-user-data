#!/usr/bin/env python3
'''Auth class'''
from flask import request
from typing import List, TypeVar


class Auth:
    '''Implements the Auth class'''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        if path is None:
            return True
        if not excluded_paths:
            return True
        
        path = path.rstrip('/')
        excluded_paths = [p.rstrip('/') for p in excluded_paths]

        return path not in excluded_paths
    
    def authorization_header(self, request=None) -> str:
        if request is None or 'Authorization' not in request.headers:
            return None
        else:
            return request.headers['Authorization']
        
    
    def current_user(self, request=None) -> TypeVar('User'):
        return None
