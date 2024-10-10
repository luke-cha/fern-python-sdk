# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .video_embedding_task_video_embeddings_item_embedding import (
    VideoEmbeddingTaskVideoEmbeddingsItemEmbedding,
)
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class VideoEmbeddingTaskVideoEmbeddingsItem(UniversalBaseModel):
    """
    Each object corresponds to an embedding and has the following fields:
    """

    start_offset_sec: typing.Optional[float] = pydantic.Field(default=None)
    """
    The start time of the video segment for this embedding. If the embedding scope is `video`, this field equals `0`.
    """

    end_offset_sec: typing.Optional[float] = pydantic.Field(default=None)
    """
    The end time of the video segment for this embedding. If the embedding scope is `video`, this field equals the duration of the video.
    """

    embedding_scope: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates the scope of this embedding. It can take the following values:
    
    - `video`: Indicates that this embedding if for the entire video.
    - `clip`: Indicates that this embedding is for a specific segment.
    """

    embedding: typing.Optional[VideoEmbeddingTaskVideoEmbeddingsItemEmbedding] = (
        pydantic.Field(default=None)
    )
    """
    An object that contains a field named `float` which represents the embedding.
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
