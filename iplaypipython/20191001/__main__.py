# 从海龟绘图模块中导入全部函数
from turtle import *
def daw_flag():
    # 设置大小，4个参数：宽度、高度、起始值x轴、起始值y轴
    setup(600, 400, 0, 0)
    # 设置背景为红色
    bgcolor('red')
    # 线条、填充颜色设置为黄色
    fillcolor('yellow')
    color('yellow')
    # 画笔运行速度
    speed(10)

    # 大五角星绘制
    draw_star(-280, 100, 0, 150, 144, 0)

    # 4个小五角星绘制
    draw_star(-100, 180, 305, 50, 0, 144)
    draw_star(-50, 110, 30, 50, 144, 0)
    draw_star(-40, 50, 5, 50, 144, 0)
    draw_star(-100, 10, 300, 50, 0, 144)
    

# 绘制五角星的方法，根据实际情况传入参数
def draw_star(gotox_val, gotoy_val, heading_val=0, fd_val=50, rt_val=0, lt_val=0):
    # 开始填充
    begin_fill()
    # 提起画笔，此时可以任意移动画笔位置
    up()
    # 移动至指定坐标
    goto(gotox_val, gotoy_val)
    # 设置朝向角度
    if(0 != heading):
        setheading(heading_val)
    # 放下画笔，此时再移动就开始绘制
    down()
    # for循环，绘制5条边
    for i in range(5):
        # forward，向前移动画笔指定单位，像素
        fd(fd_val)
        if(0 != rt_val):
            # right，向右旋转指定单位，度数
            rt(rt_val)
        if(0 != lt_val):
            # left，向左旋转指定单位，度数
            lt(lt_val)
    # 结束填充
    end_fill()

if __name__=="__main__":
    print('开始绘制五星红旗')
    daw_flag()
    print('结束绘制五星红旗')
    input('暂停，等待输入（输入任意内容可退出）：')
