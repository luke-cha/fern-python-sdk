# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from .video_vector_metadata import VideoVectorMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class VideoVector(UniversalBaseModel):
    id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="_id")
    ] = pydantic.Field(default=None)
    """
    A string representing the unique identifier of a video. The platform creates a new `video_vector` object and assigns it a unique identifier when the video has successfully been indexed. Note that video IDs are different from task IDs.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string indicating the date and time, in the RFC [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format ("YYYY-MM-DDTHH:mm:ssZ"), that the video indexing task was created.
    """

    updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string indicating the date and time, in the RFC [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format ("YYYY-MM-DDTHH:mm:ssZ"), that the video indexing task object was last updated. The platform updates this field every time the video indexing task transitions to a different state.
    """

    indexed_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string indicating the date and time, in the RFC [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format ("YYYY-MM-DDTHH:mm:ssZ"), that the video indexing task has been completed.
    """

    metadata: typing.Optional[VideoVectorMetadata] = pydantic.Field(default=None)
    """
    An object that contains information about the video.
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
