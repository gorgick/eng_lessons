from typing import List, Optional

from fastapi import APIRouter, Depends, Response, status

from eng_courses.models.words import Word, WordKind, WordCreate, WordUpdate
from eng_courses.services.words import WordsService

router = APIRouter(
    prefix='/words',
    tags=['words'],
)


@router.get('/{course_id}', response_model=List[Word])
def get_words(
        course_id: int,
        kind: Optional[WordKind] = None,
        service: WordsService = Depends(),
):
    return service.get_words(course_id=course_id, kind=kind)


@router.post('/{course_id}', response_model=Word)
def add_word(course_id: int, word_data: WordCreate, service: WordsService = Depends()):
    return service.add_word(course_id=course_id, word_data=word_data)


@router.get('/{course_id}/{word_id}', response_model=Word)
def get_word(course_id: int, word_id: int, service: WordsService = Depends()):
    return service.get_word(course_id=course_id, word_id=word_id)


@router.put('/{course_id}/{word_id}', response_model=Word)
def update_word(course_id: int, word_id: int, word_data: WordUpdate, service: WordsService = Depends()):
    return service.update_word(course_id=course_id, word_id=word_id, word_data=word_data)


@router.delete('/{course_id}/{word_id}')
def delete_word(course_id: int, word_id: int, service: WordsService = Depends()):
    service.delete_word(course_id=course_id, word_id=word_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
