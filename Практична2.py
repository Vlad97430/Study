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

class Info(Vladyslav):
    def __init__(self, first_name=None, last_name=None, birth_year=None,
                 email=None, phone=None, city=None):
        super().__init__(first_name, last_name, birth_year)
        self.email = email if email is not None else None
        self.phone = phone if phone is not None else None
        self.city = city if city is not None else None

    def full_info(self):
        return {
            "Ім'я": self.first_name,
            "Прізвище": self.last_name,
            "Рік народження": self.birth_year,
            "Email": self.email,
            "Телефон": self.phone,
            "Місто": self.city
        }

    def _short_contact(self):
        return f"{self.first_name} ({self.phone})"

    def __private_greeting(self):
        return f"Привіт, {self.first_name} з міста {self.city}!"

    def call_private_greeting(self):
        return self.__private_greeting()

person = Info("Владислав", "Кравчук", 2008, email="vlad@gmail.com", phone="123456789", city="Луцьк")

print(person.name_list())
print(person.calculate_course())
print(person.full_info())
print(person._short_contact())
print(person.call_private_greeting())
