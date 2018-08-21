import time

def is_prime(num, prime_num):
    for x in prime_num:
        remainder =num%x
        if remainder == 0:
            return False
        #else:
        #    continue
    return True

start = time.time()
prime_nums=[]
maxnum=1000000
for num in range(2,maxnum+1):
    if is_prime(num, prime_nums):
        prime_nums.append(num)
end=time.time()
print(prime_nums)
print(len(prime_nums))
print(end-start)


