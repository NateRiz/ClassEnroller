from I import I

class Enroll:

    def main_loop(self):
        I.go_to_url("https://schedule.msu.edu/")
        I.should_see("Search for Courses")
        I.select_from_dropdown("Term",self.term)
        I.select_from_dropdown("Subject",self.subject)
        I.fill_field("Course Number", self.course_number)
        I.click("Find Courses")
