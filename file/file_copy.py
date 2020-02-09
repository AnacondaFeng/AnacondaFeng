import os


# import os.path

class FileCopy(object):
    """File Backup function"""

    def __init__(self, src, dist):
        """
        初始化构造函数传入原始路径和目标路径
        :param src:
        :param dist:
        """
        self.src = src
        self.dist = dist

    def read_files(self):
        """读取src目录下的所有文件"""
        ls = os.listdir(self.src)
        print(ls)
        for i in ls:
            self.backup_file(i)

    def backup_file(self, file_name):
        """按照文件名处理备份"""
        if not os.path.exists(self.dist):
            os.makedirs(self.dist)
            print("指定目录不存在，创建完成")

        #         拼接文件的完整路径
        full_src_path = os.path.join(self.src, file_name)
        full_dist_path = os.path.join(self.dist, file_name)

        #         判断是否为文件夹
        if os.path.isfile(file_name) and os.path.splitext(file_name)[-1].lower() == '.txt':
            # print(full_path)
            with open(full_dist_path, 'w', encoding='utf-8') as f_dist, open(full_src_path, 'r',
                                                                             encoding='utf-8') as f_src:
                print(">>开始备份{0}".format(file_name))
                while True:
                    rest = f_src.read(100)
                    if not rest:
                        break
                    f_dist.write(rest)
                f_dist.flush()
            print(">>备份完成{0}".format(file_name))

        else:
            print("文件类型不符合备份要求，跳过>>")


if __name__ == '__main__':
    base_path = os.path.dirname(os.path.abspath(__file__))
    print(base_path)

    src_path = os.path.join(base_path, 'src')
    dist_path = os.path.join(base_path, 'dist')

    fileC = FileCopy(src_path, dist_path)
    fileC.read_files()
