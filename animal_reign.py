#!/usr/bin/env python
import os
os.system('clear')

from animal import Animal
from dog import Dog
from german_shepard import GermanShepard


# I changed how it looks because looking at it made my eyes hurt

def main():
    # Behavior of a human.
    human = Animal(2, 2)
    human.summary()
    human.breathe()
    human.walk()
    print('\n\n')

    # Behavior of a dog
    dog = Dog(4,2)
    dog.summary()
    dog.breathe()
    dog.walk()
    print('\n\n')

    # Behavior of a German Shepard
    german_shepard = GermanShepard(4,2)
    german_shepard.summary()
    german_shepard.breathe()
    german_shepard.walk()

if __name__ == "__main__":
    main()

