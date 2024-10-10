# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class ExtractVideoDataIdentifyLogosResponseDataItem(UniversalBaseModel):
    start: typing.Optional[float] = pydantic.Field(default=None)
    """
    The start of the time range, expressed in seconds.
    """

    end: typing.Optional[float] = pydantic.Field(default=None)
    """
    The end of the time range, expressed in seconds.
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    The logo identified within this time range.
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