import random
import math
asteroids = ["1 Ceres", "2 Pallas", "3 Juno", "4 Vesta", "21 Lutetia", "45 Eugenia", "140 Siwa", "243 Ida", "253 Mathilde", "433 Eros"]
n = len(asteroids)
asteroid_mass = [947000000000000000000, 214000000000000000000, 20000000000000000000, 259000000000000000000, 1700000000000000000, 6100000000000000000, 1500000000000000000, 100000000000000000, 103300000000000000, 6690000000000000]
other_objects = ["elephant", "car", "human"]
other_masses = [4000, 1500, 70]
y=len(other_objects)
b = random.randint(0,y-1)
random_other_mass = other_masses[b]
x=len(asteroids)
a = random.randint(0,x-1)
random_asteroid_mass = asteroid_mass[a]
number = random_asteroid_mass / random_other_mass
if number == 1:
    print "The asteroid", asteroids[a] , "is the mass of" , number , other_objects[b] + "."
else:
    print "The asteroid", asteroids[a] , "is the mass of" , number , other_objects[b] + "s."
