# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class TextToVideoSearchMakeSearchRequestResponseDataItemMetadataItem(
    UniversalBaseModel
):
    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string that indicates the type of match (`visual`, `conversation`, `text_in_video`, or `logo`).
    """

    text: typing.Optional[str] = pydantic.Field(default=None)
    """
    For `conversation` and `text_in_video`, the API returns a transcription of the spoken words or the text that matches your search query.
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
