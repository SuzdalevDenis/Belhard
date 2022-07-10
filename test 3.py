class Math:


    @staticmethod
    def addition(a, b):
        return  a + b

    @staticmethod
    def multiplication(a, b):
        return a * b

print(Math.addition(2, 7))
print(Math.multiplication(8, 9))




from random import randint

numbers = [randint(-2, 2) for _ in range(10)]
print(numbers)
numbers = list(filter(lambda x: x, numbers))
print(numbers)


from random import randint

numbers = [randint(-2, 2) for _ in range(10)]
print(numbers)
numbers
