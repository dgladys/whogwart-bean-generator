
from lib.Person import Person
from lib.BeanGenerator import BeanGenerator
import json

whogwart_url = 'http://whogwart.pl/'

file = open('input.txt', 'r')
lines = file.readlines()
file.close()

generator = BeanGenerator(whogwart_url)
for line in lines:

    person_data = json.loads(line)

    print("Process person %s" % person_data['login'])

    person = Person(person_data['login'], person_data['password'])
    generator.generate(person, 5)
