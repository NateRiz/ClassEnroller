class Course:
    subject = ""
    course_number = ""
    def __init__(self, section=-1, enrolled=-1, limit=-1, link = None):
        self.section = section
        self.enrolled = enrolled
        self.limit = limit
        self.link = link        
