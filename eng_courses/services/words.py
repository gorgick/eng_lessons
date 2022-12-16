from typing import List, Optional

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from eng_courses import tables
from eng_courses.database import get_session
from eng_courses.models.words import WordKind, WordCreate, WordUpdate


class WordsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, course_id: int, word_id: int) -> tables.Word:
        word = self.session.query(tables.Word).filter_by(course_id=course_id, id=word_id).first()
        if not word:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return word

    def get_words(self, course_id: int, kind: Optional[WordKind] = None) -> List[tables.Word]:
        query = self.session.query(tables.Word).filter_by(course_id=course_id)
        if kind:
            query = query.filter_by(kind=kind)
        words = query.all()
        return words

    def get_word(self, course_id, word_id: int) -> tables.Word:
        return self._get(course_id, word_id)

    def add_word(self, course_id: int, word_data: WordCreate) -> tables.Word:
        word = tables.Word(**word_data.dict(), course_id=course_id)
        self.session.add(word)
        self.session.commit()
        return word

    def update_word(self, course_id: int, word_id: int, word_data: WordUpdate) -> tables.Word:
        word = self._get(word_id, course_id)
        for field, value in word_data:
            setattr(word, field, value)
        self.session.commit()
        return word

    def delete_word(self, course_id: int, word_id: int):
        word = self._get(word_id, course_id)
        self.session.delete(word)
        self.session.commit()
