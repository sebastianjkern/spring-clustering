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
    def __init__(self, mass1: Mass, mass2: Mass, relaxed_length=1.0):
        self.relaxed_length = relaxed_length
        self.spring_constant = 0.05
        self.mass1 = mass1
        self.mass2 = mass2

    def update(self):
        direction = self.mass2.position - self.mass1.position
        normalized_direction = direction / abs(direction) if direction != 0 else 0

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




