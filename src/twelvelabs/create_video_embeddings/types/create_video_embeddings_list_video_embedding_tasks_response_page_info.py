# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from ...types.limit_per_page_simple import LimitPerPageSimple
from ...types.page import Page
from ...types.total_page import TotalPage
from ...types.total_results import TotalResults
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class CreateVideoEmbeddingsListVideoEmbeddingTasksResponsePageInfo(UniversalBaseModel):
    """
    An object that provides information about pagination.
    """

    limit_per_page: typing.Optional[LimitPerPageSimple] = None
    page: typing.Optional[Page] = None
    total_page: typing.Optional[TotalPage] = None
    total_results: typing.Optional[TotalResults] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
