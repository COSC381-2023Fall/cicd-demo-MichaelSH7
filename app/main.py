from fastapi import FastAPI
from app.course import courses
from app.student import students
from app.test_student import StudentA
from app.student import studentstwo

app = FastAPI()

@app.get("/courses/{EID}")
def get_student_courses(EID: str):
    for i in range(len(students)):
        if students[i]._EID == EID:
            return students[i]._list
        
    for i in range(len(studentstwo)):
        if studentstwo[i]._EID== EID:
            return studentstwo[i]._list    
        
    return {"message": "no student found"}

