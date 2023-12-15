from fastapi.testclient import TestClient
from app.main import app
from app.test_course import courseA
from app.course import courses
from app.test_student import StudentA
from app.student import students
from app.student import Student
from app.course import coursestwo
from app.student import studentstwo


client = TestClient(app)

def test_get_courses(courseA):
    courses.append(courseA)
    response = client.get("/courses/113524")
    print(response.text)
    assert response.status_code == 200
    assert response.json() == [
        {
            "_prefix":"Cosc",
            "_course_number":321,
            "_cap": 30,
            "_instructor":"Poh",
            "_name":"Copputer organization",
            "_place":"pray",
            "_meeting_times":"12:00pm - 12:00 am"
        }]
    courses.pop()
def test_newmethod(StudentA, courseA):
    coursestwo.append(courseA)
    studentstwo.append(StudentA)
    StudentA.addCourse("Cosc", 111)
    response2= client.get("/courses/1234")
    print(response2.text)
    assert response2.status_code == 200
    assert response2.json()==[
        {
            "_prefix":"Cosc",
            "_course_number":111,
            "_cap": 30,
            "_instructor":"John Doe",
            "_name":"Programming I",
            "_place":"PH 503",
            "_meeting_times":"TH 9:00"   
        }]
    studentstwo.pop()
    coursestwo.pop()
    StudentA._list.pop()
    assert len(studentstwo)==1

def test_simple_stuffthree():
   x=5
   assert x==5
