from chat2graph.core.dal.database import Do, engine
from chat2graph.core.dal.do.file_descriptor_do import FileDescriptorDo  # noqa: F401
from chat2graph.core.dal.do.graph_db_do import GraphDbDo  # noqa: F401
from chat2graph.core.dal.do.job_do import JobDo  # noqa: F401
from chat2graph.core.dal.do.knowledge_do import KnowledgeBaseDo  # noqa: F401
from chat2graph.core.dal.do.message_do import MessageDo  # noqa: F401
from chat2graph.core.dal.do.session_do import SessionDo  # noqa: F401


def drop_db() -> None:
    """Drop database tables."""
    Do.metadata.drop_all(bind=engine)


if __name__ == "__main__":
    drop_db()
