# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ClassifyLabel(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    A string representing the name you want to give this label.
    """

    prompts: typing.List[str] = pydantic.Field()
    """
    An array of strings that specifies what the label contains.
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
