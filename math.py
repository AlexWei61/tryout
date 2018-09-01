produce_coin_per_day = 10
days = 365
init_coin = 20
steal_coin_per_week = 2
DAYS_PER_WEEK = 7

def calc_coin_nums(days,init_coin=20,produce_coin_per_day=10,steal_coin_per_week=2):
    coin_nums =  init_coin+ \
                 produce_coin_per_day*days- \
                 int(days/DAYS_PER_WEEK)*steal_coin_per_week
    return coin_nums

def gen_month_coin(month_count=12):
    monthly_coin = []
    for month in range(1,month_count+1):
        if month < 6:
            coin_num = calc_coin_nums(days=30 * month, produce_coin_per_day=10 + month - 1, steal_coin_per_week=2)
        else:
            coin_num = calc_coin_nums(days=30 * month, produce_coin_per_day=10 + month - 1, steal_coin_per_week=0)
        monthly_coin.append(coin_num)
    return monthly_coin
month_coin = gen_month_coin(12)
print(month_coin)
print(len(month_coin))

age= 67
xxx = 30>=age and age>20
print(xxx)
yyy = 10

if 30>=age and age>20:
    print("you are old")
    print("another line")
elif age>30:
    print("you are too old")
else:
    print("you are young")
max_month = 1

age = 10
age1 = 5

if age is age1:
    print("they are same")
else:
    print("they are dddd")


g1 = [89,78,69,89,96,45,67,31,95,100,32]
g2 = [89,78,69,89,96,45,67,31,95,100,32,75]
def get_median_grade(grade):
    median_grade = 0
    grade.sort()
    people_num = len(grade)
    print(grade)
    half_num = int(people_num/2)
    if people_num%2==1:
        median_grade = grade[half_num]
    else:
        m1=grade[half_num-1]
        m2=grade[half_num]
        median_grade = ((m1+m2)/2)
    return (median_grade)
median_num = get_median_grade(grade=g2)
print(median_num)


def get_average_grade(grade):
    average = 0
    for g in grade:
        average = average+g
    average = average/len(grade)
    return average
average = get_average_grade(grade=g2)
print(average)

