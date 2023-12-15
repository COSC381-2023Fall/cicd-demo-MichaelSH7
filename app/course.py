import time

class Course:
    def __init__(self, prefix, course_number, cap, instructor, name, place, meeting_times):
        self._prefix = prefix
        self._course_number = course_number
        self._cap = cap
        self._instructor = instructor
        self._name = name
        self._place = place
        self._meeting_times = meeting_times 

    def is_prefix(self, prefix):
        return self._prefix == prefix
    def request_for_changing_room(self, new_place):
        # TODO: unfinished
        self.confirmation()
        self._place = new_place
    
    def confirmation(self):
        time.sleep(10) 
courses = [ Course("Cosc", 321, 30, "Poh", "Copputer organization", "pray", "12:00pm - 12:00 am"), 
           Course("Cosc", 211, 30, "Jiang", "Alogrithm", "EMU", "12:00 - 2:00pm"),
           Course("Cosc", 111, 30, "John Doe", "Programming I", "PH 503", "TH 9:00")
           ] 
coursestwo =[ Course("Cosc", 111, 30, "John Doe", "Programming I", "PH 503", "TH 9:00")]

