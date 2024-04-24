#!/usr/bin/env python3
'''Session Authentication Module'''
from .auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    '''The session authentication class'''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''Creates a session id
        Its uses this sesssion_id as the key and the user_id as the value
        '''
        if not user_id:
            return None
        if not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id
