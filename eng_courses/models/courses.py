from pydantic import BaseModel
from datetime import date
from typing import List

from eng_courses.models.words import Word


class CourseBase(BaseModel):
    title: str
    date: date


class CourseCreate(CourseBase):
    pass


class Course(CourseBase):
    id: int
    words: List[Word] = []

    class Config:
        orm_mode = True
