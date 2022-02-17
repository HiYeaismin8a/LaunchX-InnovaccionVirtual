
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']
nuevoPlaneta = input("Ingresa el nombre de un planeta En MAYÚSCULAS: ")
planets.append(nuevoPlaneta)
print(planets)
print(planets[-1] +" Este es el último planeta de la lista.")


planeta_index = planets.index(nuevoPlaneta)


###################################################################################
# Muestra los planetas más cercanos al sol
print('Here are the planets closer than ' + nuevoPlaneta)
print(planets[0:planeta_index])

# Muestra los planetas más lejanos al sol
print('los planetas más lejanos al sol: ' + nuevoPlaneta)
print(planets[planeta_index + 1:])