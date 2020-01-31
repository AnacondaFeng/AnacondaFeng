# 定义函数
# 函数用于代码的重用

def print_verse(verse_name, is_show_tiile, is_show_dynasty):
    # 函数体
    if verse_name == "静夜思":
        if is_show_tiile == True:
            print("静夜思-李白")
        if is_show_dynasty == True:
            print("唐朝")
        print("床前明月光")
    elif verse_name == "再别康桥":
        if is_show_tiile == True:
            print("再别康桥-徐志摩")
        if is_show_dynasty == True:
            print("民国")
        print("轻轻地我走了")


print_verse("静夜思", True, True)

print_verse("再别康桥", False, False)
