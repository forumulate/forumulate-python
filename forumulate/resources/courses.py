from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class CoursesQuizzesResource:
    """``client.courses.quizzes`` (11 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def author_lesson_quiz(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> AuthorQuiz:
        """Get the quiz in a space (authoring lessons)

        ``GET /orgs/{orgId}/spaces/{spaceId}/course/authoring/lessons/{pageId}/quiz``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/authoring/lessons/{_path(page_id)}/quiz",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def save_lesson_quiz(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        passing_score: int,
        questions: List[CoursesQuizzesSaveLessonQuizParamsQuestion],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        title: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CoursesQuizzesSaveLessonQuizResponse:
        """Replace the quiz in a space (lessons)

        ``PUT /orgs/{orgId}/spaces/{spaceId}/course/authoring/lessons/{pageId}/quiz``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/authoring/lessons/{_path(page_id)}/quiz",
            query=_query({}, extra_query),
            body=_body({"title": title, "passingScore": passing_score, "questions": questions}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def author_module_quiz(
        self,
        org_id: str,
        space_id: str,
        collection_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> AuthorQuiz:
        """Get the quiz in a space (authoring modules)

        ``GET /orgs/{orgId}/spaces/{spaceId}/course/authoring/modules/{collectionId}/quiz``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/authoring/modules/{_path(collection_id)}/quiz",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def save_module_quiz(
        self,
        org_id: str,
        space_id: str,
        collection_id: str,
        *,
        passing_score: int,
        questions: List[CoursesQuizzesSaveModuleQuizParamsQuestion],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        title: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CoursesQuizzesSaveModuleQuizResponse:
        """Replace the quiz in a space (modules)

        ``PUT /orgs/{orgId}/spaces/{spaceId}/course/authoring/modules/{collectionId}/quiz``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/authoring/modules/{_path(collection_id)}/quiz",
            query=_query({}, extra_query),
            body=_body({"title": title, "passingScore": passing_score, "questions": questions}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def delete_quiz(
        self,
        org_id: str,
        space_id: str,
        quiz_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CoursesQuizzesDeleteQuizResponse:
        """Delete the quiz

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/course/authoring/quizzes/{quizId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/authoring/quizzes/{_path(quiz_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def quiz_policy(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> QuizPolicy:
        """Get the quiz policy in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/course/authoring/quiz-policy``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/authoring/quiz-policy",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_quiz_policy(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        reveal: Union[str, NotGiven] = NOT_GIVEN,
        max_attempts: Union[int, NotGiven] = NOT_GIVEN,
        cooldown_seconds: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Replace the quiz policy in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/course/authoring/quiz-policy``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/authoring/quiz-policy",
            query=_query({}, extra_query),
            body=_body({"reveal": reveal, "maxAttempts": max_attempts, "cooldownSeconds": cooldown_seconds}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def lesson_quiz(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ReaderQuiz:
        """Get the quiz in a space (lessons)

        ``GET /orgs/{orgId}/spaces/{spaceId}/course/lessons/{slug}/quiz``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/lessons/{_path(slug)}/quiz",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def quiz(
        self,
        org_id: str,
        space_id: str,
        quiz_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ReaderQuiz:
        """Get the quiz

        ``GET /orgs/{orgId}/spaces/{spaceId}/course/quizzes/{quizId}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/quizzes/{_path(quiz_id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def submit(
        self,
        org_id: str,
        space_id: str,
        quiz_id: str,
        *,
        answers: List[CoursesQuizzesSubmitParamsAnswer],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create an attempt in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/course/quizzes/{quizId}/attempts``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/quizzes/{_path(quiz_id)}/attempts",
            query=_query({}, extra_query),
            body=_body({"answers": answers}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def my_certificate(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> MyCertificate:
        """Get the certificate in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/course/certificate``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/certificate",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class CoursesResource:
    """``client.courses`` (2 operations; quizzes)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client
        self.quizzes = CoursesQuizzesResource(client)

    def outline(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CourseOutline:
        """Get the outline in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/course/outline``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/outline",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def complete(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        completed: bool,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CoursesCompleteResponse:
        """Complete the lesson

        ``PUT /orgs/{orgId}/spaces/{spaceId}/course/lessons/{slug}/complete``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/lessons/{_path(slug)}/complete",
            query=_query({}, extra_query),
            body=_body({"completed": completed}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
