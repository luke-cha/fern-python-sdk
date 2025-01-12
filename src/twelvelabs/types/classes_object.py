# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from .classes_object_options_item import ClassesObjectOptionsItem
from .classes_object_conversation_option import ClassesObjectConversationOption
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ClassesObject(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    A string representing the name you want to give this class. Make sure you use brief and meaningful names.
    """

    prompts: typing.List[str] = pydantic.Field()
    """
    An array of strings that specifies what the class contains. The platform will classify your videos based on this array. Note that the total number of prompts you specify in a request must not exceed 100.
    """

    options: typing.Optional[typing.List[ClassesObjectOptionsItem]] = pydantic.Field(
        default=None
    )
    """
    If set, overides the options for this class.
    """

    conversation_option: typing.Optional[ClassesObjectConversationOption] = (
        pydantic.Field(default=None)
    )
    """
    If set, overides the conversation option for this class.
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
