# структурная, процедурная и функциональная
def celcius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


temps_celc = [0, 10, 20, 30]
temps_fahr = list(map(celcius_to_fahrenheit, temps_celc))
print(temps_fahr)  # [32.0, 50.0, 68.0, 86.0]
