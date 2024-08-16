def einstein (mass):
    energy = int(mass) * 300000000 **2
    return energy

mass = input("m: ")
energy = einstein(mass)
print(f"E: {energy}")