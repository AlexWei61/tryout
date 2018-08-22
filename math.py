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




