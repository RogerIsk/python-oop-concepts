from abc import ABC, abstractmethod
from tool import Laptop


# Complete the class Worker
@abstractmethod 
class Worker(ABC):
    def __init__(self, name, minutes):
        self.name = name
        self.minutes = minutes

    @abstractmethod
    def work(self):
        print(f"\n\n{self.name} starts working:")
    
    @abstractmethod
    def take_break(self, minutes):
        print(f"\n\n{self.name} takes {minutes} minutes break:")


# Complete this class, so that it would work properly. Implement the missing methods
class Programmer(Worker):
    def __init__(self, name:str, language:str):
        super().__init__(name, language)
        self.language = language
        self.name = name

    def __str__(self):
        return f"{self.name} codes with {self.language}"

    def work(self):
        return(f"\n\n{self.name} starts working:")
    
    def take_break(self, minutes):
        return(f"\n\n{self.name} takes {minutes} minutes break:")



# Complete the class Janitor.
# Janitor is a subclass of the class Worker
# work(): Janitor fixes pipes with "tool"
# take_break(): Janitor listens to music
class Janitor(Worker):
    def __init__(self, name:str, tool:str):
        super().__init__(name,tool)
        self.name = name
        self.tool = tool

    def __str__(self):
        return f"{self.name} uses {self.tool}"

    def work(self):
        return f"Janitor fixes pipes with {self.tool}"
    
    def take_break(self, minutes):
            return(f"\n\n{self.name} takes {minutes} minutes break:")
        





