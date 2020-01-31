
service_menu = {'1': '人民币转换美元', '2': '美元转换人民币',
                '3': '人民币转换欧元', '0': '结束程序'}

while True:

    print("**********欢迎使用货币转换服务系统**********")

    # print("1.人民币转换美元")
    # print("2.美元转换人民币")
    # print("3.人民币转换欧元")
    # print("0.结束程序")
    for k, v in service_menu.items():
        print(k, v)
    your_choice = input("请您选择需要的服务： ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    if your_choice == "1":
        print("欢迎使用人民币转换美元服务")
        your_money = float(input("请输入您需要转换的人民币金额： "))
        print("您需要转换的人民币为：{}".format(your_money))
        RMB_to_US = your_money / 6.72
        print("兑换成美元为：{:.2f}$".format(RMB_to_US))

    elif your_choice == "2":
        print("欢迎使用美元转换人民币服务")
        your_money = float(input("请输入您需要转换的美元金额： "))
        print("您需要转换的美元为：{}".format(your_money))
        US_to_RMB = your_money * 6.72
        print("兑换成人民币为：{:.2f}元".format(US_to_RMB))

    elif your_choice == "3":
        print("欢迎使用人民币转换欧元服务")
        your_money = float(input("请输入您需要转换的人民币金额： "))
        print("您需要转换的人民币为：{}".format(your_money))
        RMB_to_EUR = your_money * 0.13
        print("兑换成欧元为：{:.2f}欧元".format(RMB_to_EUR))

    elif your_choice == "0":
        print("感谢您的使用，祝您生活愉快，再见！")
        break

    else:
        print("信息有误")
