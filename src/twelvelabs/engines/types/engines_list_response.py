# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from ...types.engine import Engine
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class EnginesListResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[Engine]] = pydantic.Field(default=None)
    """
    An array that contains the `engine` objects.
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
