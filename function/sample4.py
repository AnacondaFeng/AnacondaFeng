# 函数的使用技巧

def calc_exchange_rate(amt, source, target="USD"):
    print(target)
    if source == "CNY" and target == "USD":
        # 6.7516
        result = amt / 6.7516
        # print(result)
        print("汇率计算成功")
        return result

    elif source == "CNY" and target == "EUR":
        result = amt / 7.7512
        return result


calc_exchange_rate(100, "CNY", "EUR")


# 以形参形式传参（关键字传参）
def health_check(name, age, height, weight, hr, hbp, lbp, glu):
    print("您的健康状况良好")


health_check("张三", 17, 1, 1, 1, 1, 1, 1)


def health_check1(name, age, *, height, weight, hr, hbp, lbp, glu):
    print("您的健康状况良好")


health_check1("zhang", 32, height=1, weight=2, hr=3, hbp=4, lbp=5, glu=6)
