#!/usr/bin/env python3
'''Session Authentication Module'''
from .auth import Auth


class SessionAuth(Auth):
    '''The session authentication class'''
    user_id_by_session_id = {}
