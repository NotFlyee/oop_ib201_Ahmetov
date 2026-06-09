class Profile:
    def __init__(self, name: str):
        self.name = name

    def info(self) -> str:
        return ''
    
    def describe(self) -> None:
        print(self.name, self.info())

class Vacancy(Profile):
    def __init__(self, name: str, salary: int | float):
        super().__init__(name)
        self.salary = salary

    def info(self) -> str:
        return f'Предлагаемая зарплата: {self.salary}'
    
class Resume(Profile):
    def __init__(self, name: str, experience: int):
        super().__init__(name)
        self.experience = experience

    def info(self) -> str:
        return f'Стаж работы: {self.experience}'
