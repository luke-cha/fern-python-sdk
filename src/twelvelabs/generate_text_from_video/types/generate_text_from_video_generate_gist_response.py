# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class GenerateTextFromVideoGenerateGistResponse(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier of the response.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Suggested title for the video.
    """

    topics: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    An array containing a list of topics related to the video.
    """

    hashtags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Am array containing a list of hashtags related to the video.
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