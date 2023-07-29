import matplotlib.pyplot as plt

example2 = False
dt = 0.01


def dot_product(a, b):
    return a.real * b.real + a.imag + b.imag


class Mass:
    def __init__(self, mass=10, position=0 + 0j, fixed=False):
        self.fixed = fixed
        self.position = position
        self.mass = mass
        self.speed = 0 + 0j
        self.force = 0 + 0j
        self.drag = 0.95

    def __str__(self):
        return f"Mass at position: {self.position} with speed: {self.speed}, last force was: {self.force}"

    def update(self, dt):
        if not self.fixed:
            self.force -= self.speed * self.drag
            self.speed += (self.force / self.mass * dt)
            self.position += self.speed * dt


class Spring:
    def __init__(self, mass1: Mass, mass2: Mass):
        self.relaxed_length = 1
        self.spring_constant = 1
        self.mass1 = mass1
        self.mass2 = mass2

    def update(self):
        direction = self.mass2.position - self.mass1.position
        normalized_direction = direction / abs(direction)

        resulting_force = normalized_direction * (abs(direction) - self.relaxed_length) * self.spring_constant

        if self.mass1.fixed and self.mass2.fixed:
            return
        if self.mass1.fixed:
            self.mass2.force -= resulting_force
            return
        if self.mass2.fixed:
            self.mass1.force += resulting_force
            return

        self.mass2.force -= 0.5 * resulting_force
        self.mass1.force += 0.5 * resulting_force


# Example 1
mass1 = Mass(position=1 + 1j, fixed=True)
mass2 = Mass(position=0 + 0j, fixed=True)
mass3 = Mass(position=0 + 0.5j)

spring2 = Spring(mass2, mass3)
spring3 = Spring(mass3, mass1)

x = []
y = []

for _ in range(100000):
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

for _ in range(10000):
    m2.force = complex(0)
    s1.update()
    m2.update(dt)

    y.append(m2.position.real)

plt.plot(list(range(len(y))), y)
plt.show()

# Example 3
m1 = Mass(position=complex(), fixed=True)
m2 = Mass(position=1 + 1j, fixed=True)
m3 = Mass(position=0.25 + 0.25j)

s1 = Spring(m1, m3)
s2 = Spring(m3, m2)

x = []
y = []

z = []

for _ in range(100000):
    m3.force = complex(0)

    s1.update()
    s2.update()

    m3.update(dt)

    x.append(m3.position.real)
    y.append(m3.position.imag)

    z.append(abs(m3.position))

plt.plot(x, y)
plt.show()
