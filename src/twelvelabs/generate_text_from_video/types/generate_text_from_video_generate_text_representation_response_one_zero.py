# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .generate_text_from_video_generate_text_representation_response_one_zero_metadata import (
    GenerateTextFromVideoGenerateTextRepresentationResponseOneZeroMetadata,
)
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class GenerateTextFromVideoGenerateTextRepresentationResponseOneZero(
    UniversalBaseModel
):
    """
    Indicates the beginning of the stream.
    """

    event_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    This field is always set to `stream_start` for this event.
    """

    metadata: typing.Optional[
        GenerateTextFromVideoGenerateTextRepresentationResponseOneZeroMetadata
    ] = pydantic.Field(default=None)
    """
    An object containing metadata about the stream.
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
