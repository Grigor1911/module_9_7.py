def is_prime(function):
    def wrapper(*args, **kwargs):
        Null = function(*args, **kwargs)
        for i in range(2,Null):
            if Null % i == 0:
                print("Составное")
                break
        else:
            print("Простое")

        return Null
    return wrapper


@is_prime
def sum_three(a, b, c):
    summa = a + b + c
    return summa

result = sum_three(2, 3, 6)
print(result)