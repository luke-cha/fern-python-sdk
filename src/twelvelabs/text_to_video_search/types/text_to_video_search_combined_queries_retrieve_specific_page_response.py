# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .text_to_video_search_combined_queries_retrieve_specific_page_response_data_item import (
    TextToVideoSearchCombinedQueriesRetrieveSpecificPageResponseDataItem,
)
import pydantic
from .text_to_video_search_combined_queries_retrieve_specific_page_response_page_info import (
    TextToVideoSearchCombinedQueriesRetrieveSpecificPageResponsePageInfo,
)
from ...types.search_pool import SearchPool
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class TextToVideoSearchCombinedQueriesRetrieveSpecificPageResponse(UniversalBaseModel):
    data: typing.Optional[
        typing.List[
            TextToVideoSearchCombinedQueriesRetrieveSpecificPageResponseDataItem
        ]
    ] = pydantic.Field(default=None)
    """
    An array of objects that contains your search results.
    """

    page_info: typing.Optional[
        TextToVideoSearchCombinedQueriesRetrieveSpecificPageResponsePageInfo
    ] = pydantic.Field(default=None)
    """
    An object that provides information about pagination.
    """

    search_pool: typing.Optional[SearchPool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
