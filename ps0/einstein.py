def einstein(m):
    e = int(m) * ((3*10**8)**2)
    return e

mass = input("m: ")
energy = einstein(mass)
print(f'E: {energy}')

