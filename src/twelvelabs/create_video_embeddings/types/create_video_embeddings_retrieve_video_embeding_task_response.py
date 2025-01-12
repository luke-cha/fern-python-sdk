# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ...core.serialization import FieldMetadata
import pydantic
from .create_video_embeddings_retrieve_video_embeding_task_response_metadata import (
    CreateVideoEmbeddingsRetrieveVideoEmbedingTaskResponseMetadata,
)
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class CreateVideoEmbeddingsRetrieveVideoEmbedingTaskResponse(UniversalBaseModel):
    id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="_id")
    ] = pydantic.Field(default=None)
    """
    The unique identifier of the video embedding task.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string indicating the status of the video indexing task. It can take one of the following values: `processing`, `ready` or `failed`.
    """

    engine_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the engine the platform uses to create the embeddings.
    """

    metadata: typing.Optional[
        CreateVideoEmbeddingsRetrieveVideoEmbedingTaskResponseMetadata
    ] = pydantic.Field(default=None)
    """
    An object containing metadata about the video.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
