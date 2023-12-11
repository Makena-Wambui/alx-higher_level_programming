#!/usr/bin/python3
def ConvertToFahr(temp):
    return ((temp * (9 / 5)) + 32)


def ConvertToCels(temp):
    return (((temp - 32) * (5 / 9)))


temps = (36.5, 37, 37.5, 38, 39)
Fahreinheit = map(ConvertToFahr, temps)
Celsius = map(ConvertToCels, Fahreinheit)
TempsInFahr = list(map(ConvertToFahr, temps))
TempsInCels = list(map(ConvertToCels, TempsInFahr))
print(TempsInFahr)
print(TempsInCels)

# Illustrate lambda, map and list
Temperatures = [39.2, 36.5, 37.3, 38, 0]
Fahr = list(map(lambda temp: ((temp * (9 / 5)) + 32), Temperatures))
print(Fahr)

Cels = list(map(lambda a: ((a - 32) * (5 / 9)), Fahr))
print(Cels)
