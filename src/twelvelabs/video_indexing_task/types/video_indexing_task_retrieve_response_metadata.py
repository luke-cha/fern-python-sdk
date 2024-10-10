# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class VideoIndexingTaskRetrieveResponseMetadata(UniversalBaseModel):
    """
    An object that contains details about the video.
    """

    duration: typing.Optional[float] = None
    filename: typing.Optional[str] = None
    height: typing.Optional[int] = None
    width: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
