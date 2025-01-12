# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from ...types.limit_per_page_simple import LimitPerPageSimple
import pydantic
from ...types.total_results import TotalResults
from ...types.next_page_token import NextPageToken
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class TextToVideoSearchCombinedQueriesMakeSearchRequestResponsePageInfo(
    UniversalBaseModel
):
    """
    An object that provides information about pagination.
    """

    limit_per_page: typing.Optional[LimitPerPageSimple] = None
    page_expired_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string representing the date and time, in the <a href="https://datatracker.ietf.org/doc/html/rfc3339" target="_blank">RFC 3339</a> format ("YYYY-MM-DDTHH:mm:ssZ"), that the page expires.
    """

    total_results: typing.Optional[TotalResults] = None
    next_page_token: typing.Optional[NextPageToken] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
