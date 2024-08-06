import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return Complex(real_part, imaginary_part)

    def __truediv__(self, other):
        denom = other.real**2 + other.imaginary**2
        real_part = (self.real * other.real + self.imaginary * other.imaginary) / denom
        imaginary_part = (self.imaginary * other.real - self.real * other.imaginary) / denom
        return Complex(real_part, imaginary_part)

    def mod(self):
        magnitude = math.sqrt(self.real**2 + self.imaginary**2)
        return Complex(magnitude, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = f"{self.real:.2f}+0.00i"
        elif self.real == 0:
            if self.imaginary >= 0:
                result = f"0.00+{self.imaginary:.2f}i"
            else:
                result = f"0.00-{abs(self.imaginary):.2f}i"
        elif self.imaginary > 0:
            result = f"{self.real:.2f}+{self.imaginary:.2f}i"
        else:
            result = f"{self.real:.2f}-{abs(self.imaginary):.2f}i"
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')