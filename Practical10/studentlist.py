class student(object):
    def __init__(self, first_name, last_name, programme):
        self.first_name = first_name
        self.last_name = last_name
        self.programme = programme
    def message(self):
        print(self.first_name, self.last_name, self.programme)

studenta = student('Maria','Maria','BMS')
studenta.message()