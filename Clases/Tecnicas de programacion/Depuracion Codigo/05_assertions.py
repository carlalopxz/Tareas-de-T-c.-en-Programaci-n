edades = [26,57,92,54,22,15,17,80,47,73]
edades.sort()
print(edades)
assert edades[0] <= edades[-1]
edades = [26,57,92,54,22,15,17,80,47,73]
edades.reverse()
print(edades)
assert edades[0] <= edades[-1], 'la primera edad es mas grande que la ultima'