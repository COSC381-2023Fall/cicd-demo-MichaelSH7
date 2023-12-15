
from app.course import Course 
from app.course  import courses 
from app.course import coursestwo      
class Student:
    def __init__(self, EID, list, name):
        self._EID=EID
        self._list=list
        self._name=name

    def is_EID(self, EID):
        return self._EID==EID
    
    def is_name(self, name):
        return self._name==name
    
    def is_not_done(self):
        print("this should not show up")

    def confirmation(self, message):
        self.is_not_done()
        return message

    def addCourse(self, prefix, course_number):
        for i in range(len(courses)):
            if(courses[i]._prefix == prefix and courses[i]._course_number ==course_number):
                self._list.append(courses[i])
                break  
        for i in range(len(coursestwo)):
            if(coursestwo[i]._prefix == prefix and coursestwo[i]._course_number ==course_number):
                self._list.append(coursestwo[i])
                break  
students = [Student("113524", [courses[0]], "Mike"),
        Student("36643", [courses[1], courses[0]], "bob" )
        ]
            
studentstwo=[Student("1234", [coursestwo[0]], "Mike")]
    