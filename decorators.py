def is_prime_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

        print("Простое" if is_prime(result) else "Составное")
        return result

    return wrapper

@is_prime_decorator
def sum_three(one, two, three):
    return one + two + three

result = sum_three(2, 3, 6)
print(result)