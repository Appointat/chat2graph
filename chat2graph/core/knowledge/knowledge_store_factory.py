from chat2graph.core.common.system_env import SystemEnv
from chat2graph.core.common.type import KnowledgeStoreType
from chat2graph.core.knowledge.knowledge_store import KnowledgeStore


class KnowledgeStoreFactory:
    """Knowledge store factory."""

    @classmethod
    def get_or_create(cls, name: str) -> KnowledgeStore:
        """Get ore create a knowledge store."""
        from chat2graph.plugin.dbgpt.dbgpt_knowledge_store import (
            GraphKnowledgeStore,
            VectorKnowledgeStore,
        )

        if SystemEnv.KNOWLEDGE_STORE_TYPE == KnowledgeStoreType.VECTOR:
            return VectorKnowledgeStore(name)
        elif SystemEnv.KNOWLEDGE_STORE_TYPE == KnowledgeStoreType.GRAPH:
            return GraphKnowledgeStore(name)

        raise ValueError(f"Cannot create knowledge store of type {SystemEnv.NOWLEDGE_STORE_TYPE}")
