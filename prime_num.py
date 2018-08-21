def is_prime(num):
    for p in range(2,num):
        remainder=num%p
        if remainder is 0:
            return False
        else:
            continue
    return True
print(is_prime(10))