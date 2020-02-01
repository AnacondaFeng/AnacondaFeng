import os
# os.system("calc")

print(os.sep)

print(os.getcwd())

# print(os.chdir(''))

print(os.listdir())

# os.mkdir('hello') 创建文件夹

# os.rename('hello','world') 重命名文件夹

# os.rmdir('world') 删除文件夹

# os.path.isdir('hello') 判断是文件

# os.path.exists('hello') 判断是否存在

'''判断文件路径及文件名'''

f = "C:\\Users\\Dell\\PycharmProjects\\AnacondaFeng\\pkgstudy\\sample1.py"

print(os.path.exists(f))

print(os.path.isfile(f))

print(os.path.dirname(f))

print(os.path.split(f)) #得到文件地址 元组类型

print(os.path.basename(f))

# 得到后缀
print(os.path.splitext(f))

# 创建文件目录，然后使用mkdir/makedirs创建
print(os.path.join('C:\\hello','a','b','c'))