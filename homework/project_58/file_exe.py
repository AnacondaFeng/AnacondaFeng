"""注意修改路径"""
from homework.project_58.example import Student
from homework.project_58.example import Teacher
from homework.project_58.example import Cource


def introduction(str):
    """
     输出标题文字
    :param str: 标题名字
    :return:
    """
    print("{0}{1}{2}".format('*' * 20, str, '*' * 20))


def prepare_course():
    """
    创建课程信息初始化
    :return: list course实例
    """
    dist_course = {"01": "网络爬虫", "02": "数据分析",
                   "03": "人工智能", "04": "机器学习",
                   "05": "云计算", "06": "大数据",
                   "07": "图像识别", "08": "Web开发"}

    list_course = []

    for k, v in dist_course.items():
        course_rest = Cource(k, v)
        list_course.append(course_rest)

    return list_course


def create_teacher():
    """
    创建教师信息初始化
    :return: list teacher实例
    """
    t1 = Teacher("T1", "张亮", "13301122001")
    t2 = Teacher("T2", "王朋", "13301122002")
    t3 = Teacher("T3", "李旭", "13301122003")
    t4 = Teacher("T4", "黄国发", "13301122004")
    t5 = Teacher("T5", "周勤", "13301122005")
    t6 = Teacher("T6", "谢富顺", "13301122006")
    t7 = Teacher("T7", "贾教师", "13301122007")
    t8 = Teacher("T8", "杨教师", "13301122008")

    tech_list = [t1, t2, t3, t4, t5, t6, t7, t8]

    return tech_list


def cource_to_teacher():
    """
    实现课程与教师逐一绑定
    :return: list绑定结果
    """
    rest_c2t = []
    ls_course = prepare_course()
    ls_teacher = create_teacher()
    # 实现倒序排列
    ls_teacher.reverse()

    for i in range(len(ls_course)):
        rest_c2t.append(ls_course[i].binding(ls_teacher[i]))

    return rest_c2t


def create_student():
    """
    创建学生信息初始化
    :return: list 学生对象
    """
    ls_student = ["小亮", "小明", "李红", "小丽", "Jone", "小彤", "小K", "慕慕"]
    ls_num = []
    ls_stu_obj = []
    for i in range(1000, 1008):
        ls_num.append(i)

    ls_student.reverse()
    for i in range(len(ls_student)):
        stu = Student(ls_num[i], ls_student[i])
        ls_stu_obj.append(stu)

    return ls_stu_obj


if __name__ == '__main__':
    ls_rest_c2t = cource_to_teacher()
    ls_stu_obj = create_student()
    introduction("慕课学院（1）班学生信息")
    for i in ls_stu_obj:
        print(i.__str__())

    introduction("慕课学院（1）班选课结果")
    for j in range(len(ls_rest_c2t)):
        ls_stu_obj[j].add_course(ls_rest_c2t[j])

    for k in ls_stu_obj:
        print("Name:{0}, Selected:{1}".format(k.s_name, k.course_detail))
