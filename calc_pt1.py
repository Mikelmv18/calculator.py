from tkinter import *
from math import sin, cos, log10

expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("Error")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


def sine():
    try:
        global expression
        result = sin(eval(expression))
        equation.set(result)
        expression = str(result)
    except:
        equation.set("Error")
        expression = ""


def cosine():
    try:
        global expression
        result = cos(eval(expression))
        equation.set(result)
        expression = str(result)
    except:
        equation.set("Error")
        expression = ""


def log10_function():
    try:
        global expression
        result = log10(eval(expression))
        equation.set(result)
        expression = str(result)
    except:
        equation.set("Error")
        expression = ""
