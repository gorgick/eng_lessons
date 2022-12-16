from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from eng_courses import tables
from eng_courses.database import get_session
from eng_courses.models.courses import CourseCreate


class CoursesService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_courses(self, user_id: int) -> List[tables.Course]:
        courses = self.session.query(tables.Course).filter_by(user_id=user_id).all()
        return courses

    def get_course(self, user_id: int, course_id: int) -> tables.Course:
        course = self.session.query(tables.Course).filter(user_id, tables.Course.id == course_id).first()
        if not course:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
        return course

    def delete_course(self, user_id: int, course_id: int):
        course = self.session.query(tables.Course).filter_by(user_id=user_id, id=course_id).first()
        if not course:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        for word in course.words:
            self.session.delete(word)
        self.session.delete(course)
        self.session.commit()

    def add_course(self, user_id: int, course_data: CourseCreate) -> tables.Course:
        course = tables.Course(**course_data.dict(), user_id=user_id)
        self.session.add(course)
        self.session.commit()
        return course
