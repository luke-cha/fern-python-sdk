# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class GenerateTextFromVideoSummarizeResponseChaptersChaptersItem(UniversalBaseModel):
    """
    An object that contains details about a chapter. Each chapter has a unique number, start time, end time, title, and summary.
    """

    chapter_number: typing.Optional[int] = pydantic.Field(default=None)
    """
    Represents the sequence number of the chapter. Note that this field starts at 0. Ensure to interpret it accordingly in your application.
    """

    start: typing.Optional[int] = pydantic.Field(default=None)
    """
    The starting time of the chapter, measured in seconds from the beginning of the video.
    """

    end: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ending time of the chapter, measured in seconds from the beginning of the video.
    """

    chapter_title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The title of the chapter.
    """

    chapter_summary: typing.Optional[str] = pydantic.Field(default=None)
    """
    A brief summary describing the content of the chapter.
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
