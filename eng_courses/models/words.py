from pydantic import BaseModel
from enum import Enum


class WordKind(str, Enum):
    STUDIED = 'studied'
    NEW = 'new'


class WordBase(BaseModel):
    word: str
    translation: str
    kind: WordKind


class WordCreate(WordBase):
    pass


class WordUpdate(WordBase):
    pass


class Word(WordBase):
    id: int
    course_id: int

    class Config:
        orm_mode = True
