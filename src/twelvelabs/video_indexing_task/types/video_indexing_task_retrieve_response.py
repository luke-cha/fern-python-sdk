# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ...core.serialization import FieldMetadata
import pydantic
from .video_indexing_task_retrieve_response_metadata import (
    VideoIndexingTaskRetrieveResponseMetadata,
)
from .video_indexing_task_retrieve_response_hls import (
    VideoIndexingTaskRetrieveResponseHls,
)
from .video_indexing_task_retrieve_response_process import (
    VideoIndexingTaskRetrieveResponseProcess,
)
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class VideoIndexingTaskRetrieveResponse(UniversalBaseModel):
    id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="_id")
    ] = pydantic.Field(default=None)
    """
    The unique identifier of the video indexing task.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string indicating the date and time, in the [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format ("YYYY-MM-DDTHH:mm:ssZ"), that the task object has been created.
    """

    updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string indicating the date and time, in the [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format ("YYYY-MM-DDTHH:mm:ssZ"), that the task object was last updated. The platform updates this field every time the video indexing task transitions to a different state.
    """

    estimated_time: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string indicating the estimated completion date and time of the video indexing process, in the <a href="https://datatracker.ietf.org/doc/html/rfc3339" target="_blank">RFC 3339</a> format ("YYYY-MM-DDTHH:mm:ssZ").
    """

    index_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string representing the unique identifier of index to which the video is uploaded.
    """

    video_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string representing the unique identifier of the video associated with the specified video indexing task. The API returns this field only when the value of the `status` field is `ready`.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string indicating the status of the video indexing task. See the [Tasks](/reference/tasks) page for a list of possible statuses.
    """

    metadata: typing.Optional[VideoIndexingTaskRetrieveResponseMetadata] = (
        pydantic.Field(default=None)
    )
    """
    An object that contains details about the video.
    """

    hls: typing.Optional[VideoIndexingTaskRetrieveResponseHls] = pydantic.Field(
        default=None
    )
    """
    The platform returns this object only for the videos that you uploaded with the `disable_video_stream` parameter set to `false`.
    """

    process: typing.Optional[VideoIndexingTaskRetrieveResponseProcess] = pydantic.Field(
        default=None
    )
    """
    If your video has not yet finished indexing, the platform returns the current progress of the indexing operation.
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
