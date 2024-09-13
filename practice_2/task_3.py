# -*- coding: utf-8 -*-
"""
Write a program to calculate the body mass index (BMI) of a person. The user must enter their height and weight, after which you use one of the formulas below to determine the index.
BMI = weight/height**2 
"""
weight = input("Enter your weight ")
height = input("Enter your height ")


#code here
if weight.replace('.','',1).isdigit() and height.replace('.','',1).isdigit():
    BMI = float(weight) / (float(height) ** 2)
    print(f"Yours BMI is {BMI}")
else:
    print("Weight and height should be numeric value")
