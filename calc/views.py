from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def suma(request, num1, num2):
    respuesta = int(num1) + int(num2)
    return HttpResponse(respuesta)

def resta(request, num1, num2):
    respuesta = int(num1) - int(num2)
    return HttpResponse(respuesta)

def multiplicacion(request, num1, num2):
    respuesta = int(num1) * int(num2)
    return HttpResponse(respuesta)

def division(request, num1, num2):
    try:
        respuesta = int(num1) / int(num2)
    except ZeroDivisionError:
        respuesta = "Imposible dividir por 0"
    return HttpResponse(respuesta)

def notfound(request):
    respuesta = "<br>El formato correcto es:"
    respuesta += "<li>num1+num2"
    respuesta += "<li>num1-num2"
    respuesta += "<li>num1*num2"
    respuesta += "<li>num1/num2 donde num2 es distinto de 0</li>"
    respuesta += "<br>Los numeros pueden ser positivos o negativos, "
    respuesta += "basta con poner un signo menos delante (sin parentesis)"
    respuesta += "<br>Y solo se devuelven numeros enteros"
    return HttpResponse(respuesta)
