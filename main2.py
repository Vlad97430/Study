firstname = "Влад"
lastname = "Кравчук"
age = 16
if type(firstname) == type(lastname):
    print("Тип даних імені та прізвища - ", type(firstname))
namelist = [firstname, lastname]
print("Список з іменем та прізвищем - ", namelist)
if isinstance(age, int):
    print("Тип даних віку - ", type(age))