class Rectangle:
	def __init__(self, length, width):
		self.__length = length
		self.__width = width

	def square(self):
		return self.__length * self.__width

	def perimeter(self):
		return (self.__length + self.__width) * 2

x = int(input('Enter a first side: '))
y = int(input('Enter a second side: '))
ex = Rectangle(x, y)
print(f'Square: {ex.square()} and perimeter: {ex.perimeter()}')
