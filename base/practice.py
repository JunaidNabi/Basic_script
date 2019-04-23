
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))















































# Dict = {}
# Dict[0] = 'ju'
# Dict[2] = 'jun'
# Dict[3] = 'jac'
# Dict[1] = 'Welcome'
# Dict[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}}
# print("\nAdding a Nested Key: ")
# print(Dict)
# print("\nDictionary after adding 3 elements: ")
# print(Dict)
# employee = {1: {'name': 'John', 'age': '27'},
#             2: {'name': 'Kali', 'age': '22'},
#             3: {'name': 'Dev', 'age': '25'},
#             4: {'name': 'Hashim', 'age': '27'},
#             5: {'name': 'fernandez', 'age': '28'},
#             6: {'name': 'Jho', 'age': '29'},
#             7: {'name': 'Jack', 'age': '30'},
#             8: {'name': 'Jack', 'age': '30'},
#             9: {'name': 'Jack', 'age': '30'},
#             10: {'name': 'Jack', 'age': '30'}}
# salesman = {
#
#     1: {'name': 'Bali', 'age': '27'},
#     2: {'name': 'Raj', 'age': '22'},
#     3: {'name': 'Harsh', 'age': '25'},
#     4: {'name': 'Owe', 'age': '27'},
#     5: {'name': 'ferry', 'age': '28'},
#
# }
#
# print(employee[7]['name'])
# print(employee[7]['age'])


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def myfunc(self):
#         print("Hello my name is " + self.name)
#
#
# p1 = Person("Jack", 36)
# p1.myfunc()
