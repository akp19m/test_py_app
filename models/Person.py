from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self,firstName: str, lastName: str, age: int) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    @abstractmethod
    def calcAge():
        pass
    
    def __repr__(self) -> str:
        return f"{{name: {self.firstName} lastName: {self.lastName} age: {self.age}"
