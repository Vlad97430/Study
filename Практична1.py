class Vladyslav:
    def __init__(self, first_name=None, last_name=None, birth_year=None):
        self.first_name = first_name if first_name is not None else None
        self.last_name = last_name if last_name is not None else None
        self.birth_year = birth_year if birth_year is not None else None

    def calculate_course(self, current_year=2025):

        if self.birth_year is None:
            return None
        age = current_year - self.birth_year
        university_start_age = 15
        course = age - university_start_age + 1
        return course if course >= 1 else 0

    def name_list(self):

        return [self.first_name, self.last_name]
student = Vladyslav("Владислав", "Кравчук", 2008)
print(student.name_list())
print(student.calculate_course())
