from typing import List

from fastapi import APIRouter, Depends, Response, status

from eng_courses.models.auth import User
from eng_courses.models.courses import Course, CourseCreate
from eng_courses.services.auth import get_current_user
from eng_courses.services.courses import CoursesService

router = APIRouter(
    prefix="/courses",
    tags=["courses"],
)


@router.get("/", response_model=List[Course])
def get_courses(service: CoursesService = Depends(), user: User = Depends(get_current_user)):
    return service.get_courses(user_id=user.id)


@router.get("/{course_id}", response_model=Course)
def get_course(course_id: int, service: CoursesService = Depends(), user: User = Depends(get_current_user)):
    return service.get_course(user_id=user.id, course_id=course_id)


@router.delete("/{course_id}")
def delete_course(course_id: int, service: CoursesService = Depends(), user: User = Depends(get_current_user)):
    service.delete_course(user_id=user.id, course_id=course_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post('', response_model=Course)
def create_course(course_data: CourseCreate, service: CoursesService = Depends(),
                  user: User = Depends(get_current_user)):
    return service.add_course(user_id=user.id, course_data=course_data)
