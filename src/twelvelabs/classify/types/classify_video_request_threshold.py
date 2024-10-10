# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class ClassifyVideoRequestThreshold(UniversalBaseModel):
    """
    An object that allows you to filter the results.
    """

    min_video_score: typing.Optional[float] = pydantic.Field(default=None)
    """
    The video score represents the confidence level that a video matches the specified class. Use this field to specify the minimum value for the video score. The platform returns only the results for which the value of the `classes.score` field in the response is greater than or equal to `min_video_score`.
    
    **Default:** 75
    **Min:** 1
    **Max:** 100
    """

    min_clip_score: typing.Optional[float] = pydantic.Field(default=None)
    """
    The clip score represents the confidence level that a clip matches the specified class. Use this field to specify the minimum value for the clip score. The platform returns only the results for which the value of the `classes.clips.score` field is greater than or equal to `min_clip_score`.
    
    **Default:** 30
    **Min:** 1
    **Max:** 10
    """

    min_duration_ratio: typing.Optional[float] = pydantic.Field(default=None)
    """
    The duration ratio represents the sum of the lengths of the matching video clips inside a video divided by the total length of the video. Use this field to specify the minimum value for the duration ratio. The platform will return only the results for which the value of the `classes.duration_ratio` field is greater than or equal to `min_duration_ratio`.
    
    **Default:** 0.5
    **Min:** 0.01
    **Max:** 1
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