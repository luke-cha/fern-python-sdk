# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class GenerateTextFromVideoGenerateTextRepresentationResponseData(UniversalBaseModel):
    """
    When the value of the `stream` parameter is set to `false`, the response is as follows:
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier of the response.
    """

    data: typing.Optional[str] = pydantic.Field(default=None)
    """
    The generated text based on the prompt you provided.
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
