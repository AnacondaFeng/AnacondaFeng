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


    def backup_file(self, file_name):
        """按照文件名处理备份"""
        pass


if __name__ == '__main__':

    base_path = os.path.dirname(os.path.abspath(__file__))
    print(base_path)

    src_path = os.path.join(base_path, 'src')
    dist_path = os.path.join(base_path, 'dist')

    fileC = FileCopy(src_path, dist_path)
    fileC.read_files()