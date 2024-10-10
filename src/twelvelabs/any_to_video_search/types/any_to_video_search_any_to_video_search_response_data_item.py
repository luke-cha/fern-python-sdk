# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from ...types.score_search_terms import ScoreSearchTerms
from ...types.start_time import StartTime
from ...types.end_time import EndTime
import pydantic
from .any_to_video_search_any_to_video_search_response_data_item_metadata_item import (
    AnyToVideoSearchAnyToVideoSearchResponseDataItemMetadataItem,
)
from ...types.confidence import Confidence
from ...types.thumbnail_url import ThumbnailUrl
from ...types.modules import Modules
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class AnyToVideoSearchAnyToVideoSearchResponseDataItem(UniversalBaseModel):
    score: typing.Optional[ScoreSearchTerms] = None
    start: typing.Optional[StartTime] = None
    end: typing.Optional[EndTime] = None
    video_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string representing the unique identifier of the video. Once the platform indexes a video, it assigns a unique identifier. Note that this is different from the identifier of the video indexing task.
    """

    metadata: typing.Optional[
        typing.List[AnyToVideoSearchAnyToVideoSearchResponseDataItemMetadataItem]
    ] = pydantic.Field(default=None)
    """
    An array of objects where each object contains details about a specific type of match and has the following fields:
    """

    confidence: typing.Optional[Confidence] = None
    thumbnail_url: typing.Optional[ThumbnailUrl] = None
    modules: typing.Optional[Modules] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
