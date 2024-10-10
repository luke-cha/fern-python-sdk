# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..types.options_classify import OptionsClassify
from ..types.conversation_option import ConversationOption
from ..types.classes import Classes
from ..types.include_clips import IncludeClips
from .types.classify_video_request_threshold import ClassifyVideoRequestThreshold
from ..core.request_options import RequestOptions
from .types.classify_video_response import ClassifyVideoResponse
from ..core.serialization import convert_and_respect_annotation_metadata
from ..core.pydantic_utilities import parse_obj_as
from ..errors.bad_request_error import BadRequestError
from ..errors.too_many_requests_error import TooManyRequestsError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.threshold_classify_new import ThresholdClassifyNew
from .types.classify_bulk_response import ClassifyBulkResponse
from .types.classify_retrieve_specific_page_response import (
    ClassifyRetrieveSpecificPageResponse,
)
from ..core.jsonable_encoder import jsonable_encoder
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ClassifyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def video(
        self,
        *,
        video_ids: typing.Sequence[str],
        options: OptionsClassify,
        conversation_option: ConversationOption,
        classes: Classes,
        page_limit: typing.Optional[int] = OMIT,
        include_clips: typing.Optional[IncludeClips] = OMIT,
        threshold: typing.Optional[ClassifyVideoRequestThreshold] = OMIT,
        show_detailed_score: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClassifyVideoResponse:
        """
        Use this method to classify a set of videos based on the entities or actions shown in those videos. Note that this endpoint returns the first page or results. To retrieve the rest of the pages, you must call the [`GET`](/reference/classify-retrieve-specific-page) method of the `/classify/{page_token}` endpoint passing it the token that identifies the page you want to retrieve.

        **NOTES**:

        - This endpoint is rate-limited. For details, see the [Rate limits](/docs/rate-limits) page.
        - The total number of the prompts you specify in a request must not exceed 100.
        - The total duration of the videos you classify in a request must not exceed 10 hours.
        - When you use pagination, you will not be charged for retrieving subsequent pages of results.

        Parameters
        ----------
        video_ids : typing.Sequence[str]
            An array containing the unique identifiers of the videos that you want to classify.


        options : OptionsClassify

        conversation_option : ConversationOption

        classes : Classes

        page_limit : typing.Optional[int]
            The number of items to return on each page.

            **Default:** 10
            **Min:** 1
            **Max:** 50


        include_clips : typing.Optional[IncludeClips]

        threshold : typing.Optional[ClassifyVideoRequestThreshold]
            An object that allows you to filter the results.


        show_detailed_score : typing.Optional[bool]
            Set this parameter to `true` to specify that the platform should return a detailed score for each matching video clip. A detailed score contains the following information:

            - **Maximum score**: Represents the maximum score. It is determined by comparing the confidence scores of each matching clip and selecting the highest one.
            - **Average score**: Represents the average score of the matching video clips.
            - **Normalized score**: Represents the probability distribution of classes in the results, determined using the <a href="https://en.wikipedia.org/wiki/Softmax_function" target="_blank">Softmax function</a>.


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClassifyVideoResponse
            The specified videos have successfully been classified.

        Examples
        --------
        from twelvelabs import ClassesObject, TwelveLabs

        client = TwelveLabs(
            api_key="YOUR_API_KEY",
        )
        client.classify.video(
            video_ids=["video_ids"],
            options=["conversation"],
            conversation_option="semantic",
            classes=[
                ClassesObject(
                    name="name",
                    prompts=["Truck Sedan SUV Convertible"],
                )
            ],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "classify",
            method="POST",
            json={
                "video_ids": video_ids,
                "page_limit": page_limit,
                "include_clips": include_clips,
                "threshold": convert_and_respect_annotation_metadata(
                    object_=threshold,
                    annotation=ClassifyVideoRequestThreshold,
                    direction="write",
                ),
                "show_detailed_score": show_detailed_score,
                "options": options,
                "conversation_option": conversation_option,
                "classes": convert_and_respect_annotation_metadata(
                    object_=classes, annotation=Classes, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ClassifyVideoResponse,
                    parse_obj_as(
                        type_=ClassifyVideoResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def bulk(
        self,
        *,
        index_id: str,
        options: OptionsClassify,
        conversation_option: ConversationOption,
        classes: Classes,
        page_limit: typing.Optional[int] = OMIT,
        include_clips: typing.Optional[IncludeClips] = OMIT,
        threshold: typing.Optional[ThresholdClassifyNew] = OMIT,
        show_detailed_score: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClassifyBulkResponse:
        """
        Use this method to classify all the videos in the specified index based on the entities or actions shown in those videos. Note that this endpoint returns the first page or results. To retrieve the rest of the pages, you must call the [`GET`](/reference/classify-retrieve-specific-page) method of the `/classify/{page_token}` endpoint passing it the token that identifies the page you want to retrieve.

        **NOTES**:

        - This endpoint is rate-limited. For details, see the [Rate limits](/docs/rate-limits) page.
        - The total number of prompts you specify in a request must not exceed 100.
        - When you use pagination, you will not be charged for retrieving subsequent pages of results.

        Parameters
        ----------
        index_id : str
            The unique identifier of the index that you want to classify.


        options : OptionsClassify

        conversation_option : ConversationOption

        classes : Classes

        page_limit : typing.Optional[int]
            The number of items to return on each page.

            **Default:** 10
            **Min:** 1
            **Max:** 50


        include_clips : typing.Optional[IncludeClips]

        threshold : typing.Optional[ThresholdClassifyNew]

        show_detailed_score : typing.Optional[bool]
            Set this parameter to `true` to specify that the platform should return a detailed score for each matching video clip. A detailed score contains the following information:

            - **Maximum score**: Represents the maximum score. It is determined by comparing the confidence scores of each matching clip and selecting the highest one.
            - **Average score**: Represents the average score of the matching video clips.
            - **Duration weighted score**: Represents the score of each matching video clip, weighted by its length.
            - **Normalized score**: Represents the probability distribution of classes in the results, determined using the <a href="https://en.wikipedia.org/wiki/Softmax_function" target="_blank">Softmax function</a>.


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClassifyBulkResponse
            The videos in the specified index have successfully been classified.

        Examples
        --------
        from twelvelabs import ClassesObject, TwelveLabs

        client = TwelveLabs(
            api_key="YOUR_API_KEY",
        )
        client.classify.bulk(
            index_id="index_id",
            options=["conversation"],
            conversation_option="semantic",
            classes=[
                ClassesObject(
                    name="name",
                    prompts=["Truck Sedan SUV Convertible"],
                )
            ],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "classify/bulk",
            method="POST",
            json={
                "index_id": index_id,
                "page_limit": page_limit,
                "include_clips": include_clips,
                "threshold": threshold,
                "show_detailed_score": show_detailed_score,
                "options": options,
                "conversation_option": conversation_option,
                "classes": convert_and_respect_annotation_metadata(
                    object_=classes, annotation=Classes, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ClassifyBulkResponse,
                    parse_obj_as(
                        type_=ClassifyBulkResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve_specific_page(
        self,
        page_token: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClassifyRetrieveSpecificPageResponse:
        """
        The `classify` and `/classify/bulk` endpoints return the first page or results. You can use this endpoint to retrieve the rest of the pages.

        **NOTE**: When you use pagination, you will not be charged for retrieving subsequent pages of results.

        Parameters
        ----------
        page_token : str
            A token that identifies the page to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClassifyRetrieveSpecificPageResponse
            The videos in the specified index have successfully been classified.

        Examples
        --------
        from twelvelabs import TwelveLabs

        client = TwelveLabs(
            api_key="YOUR_API_KEY",
        )
        client.classify.retrieve_specific_page(
            page_token="page_token",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"classify/{jsonable_encoder(page_token)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ClassifyRetrieveSpecificPageResponse,
                    parse_obj_as(
                        type_=ClassifyRetrieveSpecificPageResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncClassifyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def video(
        self,
        *,
        video_ids: typing.Sequence[str],
        options: OptionsClassify,
        conversation_option: ConversationOption,
        classes: Classes,
        page_limit: typing.Optional[int] = OMIT,
        include_clips: typing.Optional[IncludeClips] = OMIT,
        threshold: typing.Optional[ClassifyVideoRequestThreshold] = OMIT,
        show_detailed_score: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClassifyVideoResponse:
        """
        Use this method to classify a set of videos based on the entities or actions shown in those videos. Note that this endpoint returns the first page or results. To retrieve the rest of the pages, you must call the [`GET`](/reference/classify-retrieve-specific-page) method of the `/classify/{page_token}` endpoint passing it the token that identifies the page you want to retrieve.

        **NOTES**:

        - This endpoint is rate-limited. For details, see the [Rate limits](/docs/rate-limits) page.
        - The total number of the prompts you specify in a request must not exceed 100.
        - The total duration of the videos you classify in a request must not exceed 10 hours.
        - When you use pagination, you will not be charged for retrieving subsequent pages of results.

        Parameters
        ----------
        video_ids : typing.Sequence[str]
            An array containing the unique identifiers of the videos that you want to classify.


        options : OptionsClassify

        conversation_option : ConversationOption

        classes : Classes

        page_limit : typing.Optional[int]
            The number of items to return on each page.

            **Default:** 10
            **Min:** 1
            **Max:** 50


        include_clips : typing.Optional[IncludeClips]

        threshold : typing.Optional[ClassifyVideoRequestThreshold]
            An object that allows you to filter the results.


        show_detailed_score : typing.Optional[bool]
            Set this parameter to `true` to specify that the platform should return a detailed score for each matching video clip. A detailed score contains the following information:

            - **Maximum score**: Represents the maximum score. It is determined by comparing the confidence scores of each matching clip and selecting the highest one.
            - **Average score**: Represents the average score of the matching video clips.
            - **Normalized score**: Represents the probability distribution of classes in the results, determined using the <a href="https://en.wikipedia.org/wiki/Softmax_function" target="_blank">Softmax function</a>.


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClassifyVideoResponse
            The specified videos have successfully been classified.

        Examples
        --------
        import asyncio

        from twelvelabs import AsyncTwelveLabs, ClassesObject

        client = AsyncTwelveLabs(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.classify.video(
                video_ids=["video_ids"],
                options=["conversation"],
                conversation_option="semantic",
                classes=[
                    ClassesObject(
                        name="name",
                        prompts=["Truck Sedan SUV Convertible"],
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "classify",
            method="POST",
            json={
                "video_ids": video_ids,
                "page_limit": page_limit,
                "include_clips": include_clips,
                "threshold": convert_and_respect_annotation_metadata(
                    object_=threshold,
                    annotation=ClassifyVideoRequestThreshold,
                    direction="write",
                ),
                "show_detailed_score": show_detailed_score,
                "options": options,
                "conversation_option": conversation_option,
                "classes": convert_and_respect_annotation_metadata(
                    object_=classes, annotation=Classes, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ClassifyVideoResponse,
                    parse_obj_as(
                        type_=ClassifyVideoResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def bulk(
        self,
        *,
        index_id: str,
        options: OptionsClassify,
        conversation_option: ConversationOption,
        classes: Classes,
        page_limit: typing.Optional[int] = OMIT,
        include_clips: typing.Optional[IncludeClips] = OMIT,
        threshold: typing.Optional[ThresholdClassifyNew] = OMIT,
        show_detailed_score: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClassifyBulkResponse:
        """
        Use this method to classify all the videos in the specified index based on the entities or actions shown in those videos. Note that this endpoint returns the first page or results. To retrieve the rest of the pages, you must call the [`GET`](/reference/classify-retrieve-specific-page) method of the `/classify/{page_token}` endpoint passing it the token that identifies the page you want to retrieve.

        **NOTES**:

        - This endpoint is rate-limited. For details, see the [Rate limits](/docs/rate-limits) page.
        - The total number of prompts you specify in a request must not exceed 100.
        - When you use pagination, you will not be charged for retrieving subsequent pages of results.

        Parameters
        ----------
        index_id : str
            The unique identifier of the index that you want to classify.


        options : OptionsClassify

        conversation_option : ConversationOption

        classes : Classes

        page_limit : typing.Optional[int]
            The number of items to return on each page.

            **Default:** 10
            **Min:** 1
            **Max:** 50


        include_clips : typing.Optional[IncludeClips]

        threshold : typing.Optional[ThresholdClassifyNew]

        show_detailed_score : typing.Optional[bool]
            Set this parameter to `true` to specify that the platform should return a detailed score for each matching video clip. A detailed score contains the following information:

            - **Maximum score**: Represents the maximum score. It is determined by comparing the confidence scores of each matching clip and selecting the highest one.
            - **Average score**: Represents the average score of the matching video clips.
            - **Duration weighted score**: Represents the score of each matching video clip, weighted by its length.
            - **Normalized score**: Represents the probability distribution of classes in the results, determined using the <a href="https://en.wikipedia.org/wiki/Softmax_function" target="_blank">Softmax function</a>.


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClassifyBulkResponse
            The videos in the specified index have successfully been classified.

        Examples
        --------
        import asyncio

        from twelvelabs import AsyncTwelveLabs, ClassesObject

        client = AsyncTwelveLabs(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.classify.bulk(
                index_id="index_id",
                options=["conversation"],
                conversation_option="semantic",
                classes=[
                    ClassesObject(
                        name="name",
                        prompts=["Truck Sedan SUV Convertible"],
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "classify/bulk",
            method="POST",
            json={
                "index_id": index_id,
                "page_limit": page_limit,
                "include_clips": include_clips,
                "threshold": threshold,
                "show_detailed_score": show_detailed_score,
                "options": options,
                "conversation_option": conversation_option,
                "classes": convert_and_respect_annotation_metadata(
                    object_=classes, annotation=Classes, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ClassifyBulkResponse,
                    parse_obj_as(
                        type_=ClassifyBulkResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve_specific_page(
        self,
        page_token: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClassifyRetrieveSpecificPageResponse:
        """
        The `classify` and `/classify/bulk` endpoints return the first page or results. You can use this endpoint to retrieve the rest of the pages.

        **NOTE**: When you use pagination, you will not be charged for retrieving subsequent pages of results.

        Parameters
        ----------
        page_token : str
            A token that identifies the page to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClassifyRetrieveSpecificPageResponse
            The videos in the specified index have successfully been classified.

        Examples
        --------
        import asyncio

        from twelvelabs import AsyncTwelveLabs

        client = AsyncTwelveLabs(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.classify.retrieve_specific_page(
                page_token="page_token",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"classify/{jsonable_encoder(page_token)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ClassifyRetrieveSpecificPageResponse,
                    parse_obj_as(
                        type_=ClassifyRetrieveSpecificPageResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)