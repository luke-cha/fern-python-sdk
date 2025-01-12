# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ...core.serialization import FieldMetadata
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class CreateVideoEmbeddingsRetrieveVideoEmbedingResponseVideoEmbeddingsItemEmbedding(
    UniversalBaseModel
):
    """
    An object that contains a field named `float` which represents the embedding.
    """

    float_: typing_extensions.Annotated[
        typing.Optional[typing.List[float]], FieldMetadata(alias="float")
    ] = pydantic.Field(default=None)
    """
    An array of floating point numbers representing the embedding. Note that the example response was truncated for brevity.
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
