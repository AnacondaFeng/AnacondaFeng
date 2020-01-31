'''
while True:

    print("**********欢迎使用货币转换服务系统**********")
    print("1.人民币转换美元")
    print("2.美元转换人民币")
    print("3.人民币转换欧元")
    print("0.结束程序")
    sel = input("请您选择需要的服务： ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    if sel == "1":
        print("欢迎使用人民币转换美元服务")
        rmb_1 = float(input("请输入您需要转换的人民币金额： "))
        print("您需要转换的人民币为：{}".format(rmb_1))
        print("兑换成美元为：{:.2f}$".format(rmb_1 / 6.72))

    elif sel == "3":
        print("欢迎使用人民币转换欧元服务")
        rmb_2 = float(input("请输入您需要转换的人民币金额： "))
        print("您需要转换的人民币为：{}".format(rmb_2))
        print("兑换成欧元为：{:.2f}欧元".format(rmb_2 * 0.13))

    elif sel == "0":
        print("感谢您的使用，祝您生活愉快，再见！")
        break

    else:
        print("请输入正确的数字")
'''

text = "Tomorrow"
print(text.find("m", 3))

print('Imooc'.rstrip())