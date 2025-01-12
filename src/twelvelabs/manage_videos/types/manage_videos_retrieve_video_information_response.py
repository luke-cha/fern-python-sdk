# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ...core.serialization import FieldMetadata
import pydantic
from .manage_videos_retrieve_video_information_response_metadata import (
    ManageVideosRetrieveVideoInformationResponseMetadata,
)
from .manage_videos_retrieve_video_information_response_hls import (
    ManageVideosRetrieveVideoInformationResponseHls,
)
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class ManageVideosRetrieveVideoInformationResponse(UniversalBaseModel):
    id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="_id")
    ] = pydantic.Field(default=None)
    """
    The unique identifier of the video.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string indicating the date and time, in the <a href="https://datatracker.ietf.org/doc/html/rfc3339" target="_blank">RFC 3339</a> format ("YYYY-MM-DDTHH:mm:ssZ"), that the video indexing task was created.
    """

    updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string indicating the date and time, in the <a href="https://datatracker.ietf.org/doc/html/rfc3339" target="_blank">RFC 3339</a> format ("YYYY-MM-DDTHH:mm:ssZ"), that the corresponding video indexing task was last updated. The platform updates this field every time the corresponding video indexing task transitions to a different state.
    """

    indexed_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string indicating the date and time, in the <a href="https://datatracker.ietf.org/doc/html/rfc3339" target="_blank">RFC 3339</a> format ("YYYY-MM-DDTHH:mm:ssZ"), that the video indexing task has been completed.
    """

    metadata: typing.Optional[ManageVideosRetrieveVideoInformationResponseMetadata] = (
        pydantic.Field(default=None)
    )
    """
    An object that contains the information about the video.
    """

    hls: typing.Optional[ManageVideosRetrieveVideoInformationResponseHls] = (
        pydantic.Field(default=None)
    )
    """
    The platform returns this object only for the videos that you uploaded with the `disable_video_stream` parameter set to `false`.
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
