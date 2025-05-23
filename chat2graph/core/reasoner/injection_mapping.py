from typing import TYPE_CHECKING, Dict, cast

if TYPE_CHECKING:
    pass


injection_services_mapping: Dict = {}


def setup_injection_services_mapping():
    """Setup the injection services mapping."""
    from chat2graph.core.service.artifact_service import ArtifactService
    from chat2graph.core.service.file_service import FileService
    from chat2graph.core.service.graph_db_service import GraphDbService
    from chat2graph.core.service.knowledge_base_service import KnowledgeBaseService
    from chat2graph.core.service.message_service import MessageService

    injection_services_mapping[GraphDbService] = cast(GraphDbService, GraphDbService.instance)
    injection_services_mapping[KnowledgeBaseService] = cast(
        KnowledgeBaseService, KnowledgeBaseService.instance
    )
    injection_services_mapping[FileService] = cast(FileService, FileService.instance)
    injection_services_mapping[MessageService] = cast(MessageService, MessageService.instance)
    injection_services_mapping[ArtifactService] = cast(ArtifactService, ArtifactService.instance)
