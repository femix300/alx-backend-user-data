#!/usr/bin/env python3
'''Session Authentication Module'''
from .auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    '''The session authentication class'''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''Creates a Session ID for a user_id
        Its uses this sesssion_id as the key and the user_id as the value
        '''
        if not user_id:
            return None
        if not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        '''returns a User ID based on a Session ID'''
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> User:
        '''returns a User instance based on a cookie value'''
        session_id = self.session_cookie(request)

        user_id = self.user_id_for_session_id(session_id)

        user = User.get(user_id)

        return user
