class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x_nueva = self.x + other.x
        y_nueva = self.y + other.y
        return Vector2D(x_nueva, y_nueva)
    def __sub__(self, other):
        x_nueva = self.x - other.x
        y_nueva = self.y - other.y
        return Vector2D(x_nueva, y_nueva)
    def __str__(self):
        return f"({self.x, self.y})"
    def __eq__(self, other):
        return True if self.x == other.x and self.y == other.y else False

v = Vector2D(3,5)
w = Vector2D(-2,4)
print(
    f"Vector v {v}"
    f"Vector w {w}"
      )

if v == w:
    print("Los vectores son iguales!")
else:
    print("Los vectores son diferentes!")
print("-------- SUMA ---------")
suma = v+w
print(suma)
print("-------- RESTA --------")
resta = v-w
print(resta)