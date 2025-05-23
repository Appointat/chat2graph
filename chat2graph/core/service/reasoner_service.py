from typing import Optional, cast

from chat2graph.core.common.singleton import Singleton
from chat2graph.core.common.type import MessageSourceType, ReasonerType
from chat2graph.core.reasoner.dual_model_reasoner import DualModelReasoner
from chat2graph.core.reasoner.mono_model_reasoner import MonoModelReasoner
from chat2graph.core.reasoner.reasoner import Reasoner


class ReasonerService(metaclass=Singleton):
    """Reasoner service"""

    def __init__(self):
        self._reasoners: Optional[Reasoner] = None

    def get_reasoner(self) -> Reasoner:
        """Get the reasoner."""
        if not self._reasoners:
            self.init_reasoner(reasoner_type=ReasonerType.DUAL)
        return cast(Reasoner, self._reasoners)

    def init_reasoner(
        self,
        reasoner_type: ReasonerType,
        actor_name: Optional[str] = None,
        thinker_name: Optional[str] = None,
    ) -> None:
        """Set the reasoner."""
        if reasoner_type == ReasonerType.DUAL:
            self._reasoners = DualModelReasoner(
                actor_name or MessageSourceType.ACTOR.value,
                thinker_name or MessageSourceType.THINKER.value,
            )
        elif reasoner_type == ReasonerType.MONO:
            self._reasoners = MonoModelReasoner(actor_name or MessageSourceType.MODEL.value)
        else:
            raise ValueError("Invalid reasoner type.")
