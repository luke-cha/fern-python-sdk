# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from ...types.index_schema import IndexSchema
import pydantic
from .indexes_list_response_page_info import IndexesListResponsePageInfo
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class IndexesListResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[IndexSchema]] = pydantic.Field(default=None)
    """
    An array that contains up to `page_limit` indexes.
    """

    page_info: typing.Optional[IndexesListResponsePageInfo] = pydantic.Field(
        default=None
    )
    """
    An object that provides information about pagination.
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
