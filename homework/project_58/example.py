class Student(object):
    """定义学生类"""

    def __init__(self, s_num, s_name):
        """初始化构造函数记录学生学号、姓名及课程"""
        self.s_num = s_num
        self.s_name = s_name
        self.__course = []

    @property
    def course_detail(self):
        """ 以属性的方式返回学生的已选课程信息"""
        return self.__course

    def add_course(self, cour_info):
        """实现添加课程信息cour_info至学生对象的已选课程"""
        self.__course.append(cour_info)

    def __str__(self):
        """返回学生信息表信息"""
        return "name:{0}, s_number:{1}".format(self.s_name, self.s_num)


class Teacher(object):
    """定义教师类"""

    def __init__(self, t_num, t_name, t_phone):
        """初始化构造函数记录教师编号、姓名及手机号码"""
        self.t_num = t_num
        self.t_name = t_name
        self.t_phone = t_phone

    def __str__(self):
        """返回教师编号与教师姓名属性"""
        return "name:{0}, t_number:{1}".format(self.t_name, self.t_num)


class Cource(object):
    """定义课程类"""

    def __init__(self, c_num, c_name, teacher=None):
        """定义构造函数描述课程编号、课程名称、授课教师"""
        self.c_num = c_num
        self.c_name = c_name
        self.teacher = teacher

    def binding(self, teacher):
        """实现课程绑定授课教师"""
        if isinstance(teacher, Teacher) and teacher.t_name:
            self.teacher = teacher.t_name
            rest_dist = {'课程名称': self.c_name, '教师名称': self.teacher}
            # return '{{课程名称:{0}, 教师名称:{1}}}'.format(self.c_name, self.teacher)
            return rest_dist
        else:
            return None
