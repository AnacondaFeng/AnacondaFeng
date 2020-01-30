# 函数的返回值，使用return

def calc_exchange_rate(amt, source, target):
    if source == "CNY" and target == "USD":
        # 6.7516
        result = amt / 6.7516
        # print(result)
        return result


r = calc_exchange_rate(100, "CNY", "USD")
print(r)
