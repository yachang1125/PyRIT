# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

import logging
from typing import Optional

from pyrit.chat_message_normalizer import ChatMessageNop, ChatMessageNormalizer
from pyrit.common import default_values
from pyrit.memory import MemoryInterface
from pyrit.prompt_target import PromptChatTarget

logger = logging.getLogger(__name__)


class CopilotChatTarget(PromptChatTarget):

    ENDPOINT_URI_ENVIRONMENT_VARIABLE = "COPILOT_ENDPOINT"
    MODEL_NAME_ENVIRONMENT_VARIABLE = "OLLAMA_MODEL_NAME"

    def __init__(
        self,
        *,
        endpoint_uri: str = None,
        model_name: str = None,
        chat_message_normalizer: ChatMessageNormalizer = ChatMessageNop(),
        memory: MemoryInterface = None,
        max_requests_per_minute: Optional[int] = None,
    ) -> None:
        PromptChatTarget.__init__(self, memory=memory, max_requests_per_minute=max_requests_per_minute)

        self.endpoint_uri = endpoint_uri or default_values.get_required_value(
            env_var_name=self.ENDPOINT_URI_ENVIRONMENT_VARIABLE, passed_value=endpoint_uri
        )
        self.model_name = model_name or default_values.get_required_value(
            env_var_name=self.MODEL_NAME_ENVIRONMENT_VARIABLE, passed_value=model_name
        )
        self.chat_message_normalizer = chat_message_normalizer
