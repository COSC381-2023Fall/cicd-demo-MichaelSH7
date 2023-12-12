
import pytest
from app.student import Student
from app.course import courses
from app.course import Course
from app.test_course import courseA
@pytest.fixture
def StudentA():
    StudentA = Student("1234", [], "abhi")
    return StudentA
@pytest.fixture
def fake_courses():
    pass

def test_add_a_course(StudentA, courseA):
    StudentA._list.append(courseA)
    assert len(StudentA._list) > 0





def test_is_EID(StudentA):
    assert StudentA.is_EID("1234")
    assert not StudentA.is_EID("ABC")




def test_request_for_changing_room(StudentA, mocker):
    mocker.patch(
        'app.student.Student.is_not_done'
    )
    assert StudentA.confirmation("this is the confirmation message") == "this is the confirmation message"

def test_simple_stuff():
   x=5
   assert x==5

