#!/usr/bin/env python3

import os 
import sys

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def holaPuto(self):
        print("HOLA HIJO DE SU PUTA MADRE")

def main():
     john = Person("Peter", 13)

     john.holaPuto()

     current_directory = os.getcwd()
     print(current_directory)
     print()   
     
     sling = ["iFone", "dildo", "hentai"]

     for i in sling:
        print(i)

     print()
     foreskin = [["Elitler", "bastard", "Child", 1] ,
                ["Musk", "josa", "mo", 2] ,
                ["Ler", "carillo", "les", 3]
                ]

     for row in foreskin:
         for elem in row:
             print(elem, end = " ")
         print()

main()














