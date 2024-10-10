# This file was auto-generated by Fern from our API Definition.

from ..core.client_wrapper import SyncClientWrapper
import typing
from ..core.request_options import RequestOptions
from .types.extract_video_data_retrieve_transcription_response import (
    ExtractVideoDataRetrieveTranscriptionResponse,
)
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..errors.bad_request_error import BadRequestError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from .types.extract_video_data_retrieve_ocr_response import (
    ExtractVideoDataRetrieveOcrResponse,
)
from .types.extract_video_data_identify_logos_response import (
    ExtractVideoDataIdentifyLogosResponse,
)
from .types.extract_video_data_retrieve_thumbnail_response import (
    ExtractVideoDataRetrieveThumbnailResponse,
)
from ..core.client_wrapper import AsyncClientWrapper


class ExtractVideoDataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def retrieve_transcription(
        self,
        index_id: str,
        video_id: str,
        *,
        start: typing.Optional[float] = None,
        end: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExtractVideoDataRetrieveTranscriptionResponse:
        """
        This method retrieves a transcription of the spoken words.

        Parameters
        ----------
        index_id : str
            The unique identifier of the index to which the video has been uploaded.

        video_id : str
            The unique identifier of the video for which you want to retrieve a transcription.

        start : typing.Optional[float]
            The start of the time range (in seconds) to retrieve transcription for.

        end : typing.Optional[float]
            The end of the time range (in seconds) to retrieve transcription for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtractVideoDataRetrieveTranscriptionResponse
            Transcription has successfully been retrieved.

        Examples
        --------
        from twelvelabs import TwelveLabs

        client = TwelveLabs(
            api_key="YOUR_API_KEY",
        )
        client.extract_video_data.retrieve_transcription(
            index_id="index-id",
            video_id="video-id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"indexes/{jsonable_encoder(index_id)}/videos/{jsonable_encoder(video_id)}/transcription",
            method="GET",
            params={
                "start": start,
                "end": end,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ExtractVideoDataRetrieveTranscriptionResponse,
                    parse_obj_as(
                        type_=ExtractVideoDataRetrieveTranscriptionResponse,  # type: ignore
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

    def retrieve_ocr(
        self,
        index_id: str,
        video_id: str,
        *,
        start: typing.Optional[float] = None,
        end: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExtractVideoDataRetrieveOcrResponse:
        """
        This method retrieves text recognized in video (OCR).

        Parameters
        ----------
        index_id : str
            The unique identifier of the index to which the video has been uploaded.

        video_id : str
            The unique identifier of the video.

        start : typing.Optional[float]
            The start of the time range (in seconds) to retrieve OCRs for.

        end : typing.Optional[float]
            The end of the time range (in seconds) to retrieve OCRs for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtractVideoDataRetrieveOcrResponse
            OCRs have successfully been retrieved.

        Examples
        --------
        from twelvelabs import TwelveLabs

        client = TwelveLabs(
            api_key="YOUR_API_KEY",
        )
        client.extract_video_data.retrieve_ocr(
            index_id="index-id",
            video_id="video-id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"indexes/{jsonable_encoder(index_id)}/videos/{jsonable_encoder(video_id)}/text-in-video",
            method="GET",
            params={
                "start": start,
                "end": end,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ExtractVideoDataRetrieveOcrResponse,
                    parse_obj_as(
                        type_=ExtractVideoDataRetrieveOcrResponse,  # type: ignore
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

    def identify_logos(
        self,
        index_id: str,
        video_id: str,
        *,
        start: typing.Optional[float] = None,
        end: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExtractVideoDataIdentifyLogosResponse:
        """
        Use this method to identify the presence of brand logos within your videos.

        Parameters
        ----------
        index_id : str
            The unique identifier of the index to which the video has been uploaded.

        video_id : str
            The unique identifier of the video.

        start : typing.Optional[float]
            The start of the time range (in seconds) to retrieve logos for.

        end : typing.Optional[float]
            The end of the time range (in seconds) to retrieve logos for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtractVideoDataIdentifyLogosResponse
            The request has been completed successfully.

        Examples
        --------
        from twelvelabs import TwelveLabs

        client = TwelveLabs(
            api_key="YOUR_API_KEY",
        )
        client.extract_video_data.identify_logos(
            index_id="index-id",
            video_id="video-id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"indexes/{jsonable_encoder(index_id)}/videos/{jsonable_encoder(video_id)}/logo",
            method="GET",
            params={
                "start": start,
                "end": end,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ExtractVideoDataIdentifyLogosResponse,
                    parse_obj_as(
                        type_=ExtractVideoDataIdentifyLogosResponse,  # type: ignore
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

    def retrieve_thumbnail(
        self,
        index_id: str,
        video_id: str,
        *,
        time: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExtractVideoDataRetrieveThumbnailResponse:
        """
        To use this feature, you must enable thumbnail generation for the index to which the video has been uploaded. For details, see the [Create an index](/reference/create-index) section.

        Parameters
        ----------
        index_id : str
            The unique identifier of the index to which the video has been uploaded.

        video_id : str
            The unique identifier of the video from which you want to retrieve a thumbnail.

        time : typing.Optional[float]
            Specifies the time, in seconds, at which the platform must retrieve the thumbnail. If you don't specify this parameter, the platform retrieves a thumbnail from the middle of the video.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtractVideoDataRetrieveThumbnailResponse
            A thumbnail has successfully been retrieved.

        Examples
        --------
        from twelvelabs import TwelveLabs

        client = TwelveLabs(
            api_key="YOUR_API_KEY",
        )
        client.extract_video_data.retrieve_thumbnail(
            index_id="index_id",
            video_id="video_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"indexes/{jsonable_encoder(index_id)}/videos/{jsonable_encoder(video_id)}/thumbnail",
            method="GET",
            params={
                "time": time,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ExtractVideoDataRetrieveThumbnailResponse,
                    parse_obj_as(
                        type_=ExtractVideoDataRetrieveThumbnailResponse,  # type: ignore
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


class AsyncExtractVideoDataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def retrieve_transcription(
        self,
        index_id: str,
        video_id: str,
        *,
        start: typing.Optional[float] = None,
        end: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExtractVideoDataRetrieveTranscriptionResponse:
        """
        This method retrieves a transcription of the spoken words.

        Parameters
        ----------
        index_id : str
            The unique identifier of the index to which the video has been uploaded.

        video_id : str
            The unique identifier of the video for which you want to retrieve a transcription.

        start : typing.Optional[float]
            The start of the time range (in seconds) to retrieve transcription for.

        end : typing.Optional[float]
            The end of the time range (in seconds) to retrieve transcription for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtractVideoDataRetrieveTranscriptionResponse
            Transcription has successfully been retrieved.

        Examples
        --------
        import asyncio

        from twelvelabs import AsyncTwelveLabs

        client = AsyncTwelveLabs(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.extract_video_data.retrieve_transcription(
                index_id="index-id",
                video_id="video-id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"indexes/{jsonable_encoder(index_id)}/videos/{jsonable_encoder(video_id)}/transcription",
            method="GET",
            params={
                "start": start,
                "end": end,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ExtractVideoDataRetrieveTranscriptionResponse,
                    parse_obj_as(
                        type_=ExtractVideoDataRetrieveTranscriptionResponse,  # type: ignore
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

    async def retrieve_ocr(
        self,
        index_id: str,
        video_id: str,
        *,
        start: typing.Optional[float] = None,
        end: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExtractVideoDataRetrieveOcrResponse:
        """
        This method retrieves text recognized in video (OCR).

        Parameters
        ----------
        index_id : str
            The unique identifier of the index to which the video has been uploaded.

        video_id : str
            The unique identifier of the video.

        start : typing.Optional[float]
            The start of the time range (in seconds) to retrieve OCRs for.

        end : typing.Optional[float]
            The end of the time range (in seconds) to retrieve OCRs for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtractVideoDataRetrieveOcrResponse
            OCRs have successfully been retrieved.

        Examples
        --------
        import asyncio

        from twelvelabs import AsyncTwelveLabs

        client = AsyncTwelveLabs(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.extract_video_data.retrieve_ocr(
                index_id="index-id",
                video_id="video-id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"indexes/{jsonable_encoder(index_id)}/videos/{jsonable_encoder(video_id)}/text-in-video",
            method="GET",
            params={
                "start": start,
                "end": end,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ExtractVideoDataRetrieveOcrResponse,
                    parse_obj_as(
                        type_=ExtractVideoDataRetrieveOcrResponse,  # type: ignore
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

    async def identify_logos(
        self,
        index_id: str,
        video_id: str,
        *,
        start: typing.Optional[float] = None,
        end: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExtractVideoDataIdentifyLogosResponse:
        """
        Use this method to identify the presence of brand logos within your videos.

        Parameters
        ----------
        index_id : str
            The unique identifier of the index to which the video has been uploaded.

        video_id : str
            The unique identifier of the video.

        start : typing.Optional[float]
            The start of the time range (in seconds) to retrieve logos for.

        end : typing.Optional[float]
            The end of the time range (in seconds) to retrieve logos for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtractVideoDataIdentifyLogosResponse
            The request has been completed successfully.

        Examples
        --------
        import asyncio

        from twelvelabs import AsyncTwelveLabs

        client = AsyncTwelveLabs(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.extract_video_data.identify_logos(
                index_id="index-id",
                video_id="video-id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"indexes/{jsonable_encoder(index_id)}/videos/{jsonable_encoder(video_id)}/logo",
            method="GET",
            params={
                "start": start,
                "end": end,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ExtractVideoDataIdentifyLogosResponse,
                    parse_obj_as(
                        type_=ExtractVideoDataIdentifyLogosResponse,  # type: ignore
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

    async def retrieve_thumbnail(
        self,
        index_id: str,
        video_id: str,
        *,
        time: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExtractVideoDataRetrieveThumbnailResponse:
        """
        To use this feature, you must enable thumbnail generation for the index to which the video has been uploaded. For details, see the [Create an index](/reference/create-index) section.

        Parameters
        ----------
        index_id : str
            The unique identifier of the index to which the video has been uploaded.

        video_id : str
            The unique identifier of the video from which you want to retrieve a thumbnail.

        time : typing.Optional[float]
            Specifies the time, in seconds, at which the platform must retrieve the thumbnail. If you don't specify this parameter, the platform retrieves a thumbnail from the middle of the video.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtractVideoDataRetrieveThumbnailResponse
            A thumbnail has successfully been retrieved.

        Examples
        --------
        import asyncio

        from twelvelabs import AsyncTwelveLabs

        client = AsyncTwelveLabs(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.extract_video_data.retrieve_thumbnail(
                index_id="index_id",
                video_id="video_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"indexes/{jsonable_encoder(index_id)}/videos/{jsonable_encoder(video_id)}/thumbnail",
            method="GET",
            params={
                "time": time,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ExtractVideoDataRetrieveThumbnailResponse,
                    parse_obj_as(
                        type_=ExtractVideoDataRetrieveThumbnailResponse,  # type: ignore
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
