from sqlalchemy.orm import Session as SqlAlchemySession

from app.core.dal.dao.dao import Dao
from app.core.dal.do.knowledge_do import FileKbMappingDo, KnowledgeBaseDo


class KnowledgeBaseDao(Dao[KnowledgeBaseDo]):
    """Knowledge Base Data Access Object"""

    def __init__(self, session: SqlAlchemySession):
        super().__init__(KnowledgeBaseDo, session)


class FileKbMappingDao(Dao[FileKbMappingDo]):
    """File to Knowledge Base Data Access Object"""

    def __init__(self, session: SqlAlchemySession):
        super().__init__(FileKbMappingDo, session)
