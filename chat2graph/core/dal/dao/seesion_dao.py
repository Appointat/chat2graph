from sqlalchemy.orm import Session as SqlAlchemySession

from chat2graph.core.dal.dao.dao import Dao
from chat2graph.core.dal.do.session_do import SessionDo


class SessionDao(Dao[SessionDo]):
    """Session Data Access Object"""

    def __init__(self, session: SqlAlchemySession):
        super().__init__(SessionDo, session)
