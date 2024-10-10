# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class ClassifyRetrieveSpecificPageResponseDataItemClassesItemDetailedScores(
    UniversalBaseModel
):
    """
    When you set the value of the `show_detailed_score` parameter to `true` in the body of the request, the platform returns detailed information that helps you determine the likelihood that this video clip matches your prompts.
    """

    max_score: typing.Optional[float] = pydantic.Field(default=None)
    """
    Represents the maximum score. It is determined by comparing the confidence scores of each clip and selecting the highest one.
    
    **Min**: 0.
    **Max**: 100.
    """

    avg_score: typing.Optional[float] = pydantic.Field(default=None)
    """
    Represents the average score of the matching video clips.
    
    **Min**: 0.
    **Max**: 100.
    """

    duration_weighted_score: typing.Optional[float] = pydantic.Field(default=None)
    """
    Represents the score of each matching video clip, weighted by its length.
    
    **Min**: 0
    **Max**: 100
    """

    normalized_score: typing.Optional[float] = pydantic.Field(default=None)
    """
    Represents the probability distribution of classes in the results, determined using the <a href="https://en.wikipedia.org/wiki/Softmax_function" target="_blank">Softmax function</a>.
    
    **Min**: 0
    **Max**: 100
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