def is_prime(num):
    for p in range(2,int(num/2+1)):
        remainder=num%p
        if remainder is 0:
            return False
        else:
            continue
    return True
print(is_prime(10))

prime_nums=[]
max_num=100
for num in range(2,max_num+1):
    if is_prime(num):
        prime_nums.append(num)
print(prime_nums)
print(len(prime_nums))
