# Example 1
from app import Mass, Spring
import matplotlib.pyplot as plt

dt = 0.1

mass1 = Mass(position=1 + 1j, fixed=True)
mass2 = Mass(position=0 + 0j, fixed=True)
mass3 = Mass(position=0 + 0.5j)

spring2 = Spring(mass2, mass3)
spring3 = Spring(mass3, mass1)

x = []
y = []

for _ in range(1000):
    mass3.force = complex(0)

    spring2.update()
    spring3.update()

    mass3.update(dt)

    x.append(mass3.position.real)
    y.append(mass3.position.imag)

plt.plot(x, y)
plt.show()

# Example 2

m1 = Mass(position=complex(), fixed=True)
m2 = Mass(position=0.5)

s1 = Spring(m1, m2)

y = []

for _ in range(1000):
    m2.force = complex(0)
    s1.update()
    m2.update(dt)

    y.append(m2.position.real)

plt.plot(list(range(len(y))), y)
plt.show()

# Example 3
m1 = Mass(position=0 + 0j, fixed=True)
m2 = Mass(position=1 + 1j, fixed=True)
m3 = Mass(position=1 + 0j)

s1 = Spring(m1, m3, relaxed_length=2)
s2 = Spring(m3, m2, relaxed_length=0.5)

x = []
y = []

for _ in range(100000):
    m3.force = complex(0)

    s1.update()
    s2.update()

    m3.update(dt)

    x.append(m3.position.real)
    y.append(m3.position.imag)

plt.plot(x, y)
plt.show()
