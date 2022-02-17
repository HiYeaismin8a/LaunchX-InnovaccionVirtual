

# Declara dos variables
new_planet = ""
planets = []

while (new_planet.lower() != 'done'):
    if new_planet != " " : 
        new_planet = input('<<Escribe un planet, Si termina INGRESE done>>: ')
    planets.append(new_planet)

print(new_planet)
print(planets)

for iteracionPlanetas in planets:
    print(iteracionPlanetas)