# 导入海龟绘图模块
import turtle as t

# 定义一个曲线绘制函数
def degree_curve(n, r, d=1):
    for i in range(n):
        t.left(d)
        t.circle(r, abs(d))

# 绘制玫瑰花
def draw_rose():
    # 初始位置设定
    s = 0.2
    # 设置弹窗大小
    t.setup(450 * 5 * s, 750 * 5 * s)
    # 背景颜色
    t.bgcolor('wheat')
    t.pencolor("black")
    # 设置填充颜色为红色，绘制花朵
    t.fillcolor("red")
    t.speed(100)
    # 提起画笔，移动到指定位置
    t.penup()
    t.goto(0, 900 * s)
    # 放下画笔
    t.pendown()

    # 绘制花朵形状
    t.begin_fill()
    t.circle(200 * s,30)
    degree_curve(60, 50 * s)
    t.circle(200 * s,30)
    degree_curve(4, 100 * s)
    t.circle(200 * s,50)
    degree_curve(50, 50 * s)
    t.circle(350 * s,65)
    degree_curve(40, 70 * s)
    t.circle(150 * s,50)
    degree_curve(20, 50 * s, -1)
    t.circle(400 * s,60)
    degree_curve(18, 50 * s)
    t.fd(250 * s)
    t.right(150)
    t.circle(-500 * s,12)
    t.left(140)
    t.circle(550 * s,110)
    t.left(27)
    t.circle(650 * s,100)
    t.left(130)
    t.circle(-300 * s,20)
    t.right(123)
    t.circle(220 * s,57)
    t.end_fill()
    
    # 绘制花枝形状
    t.left(120)
    t.fd(280 * s)
    t.left(115)
    t.circle(300 * s,33)
    t.left(180)
    t.circle(-300 * s,33)
    degree_curve(70, 225 * s, -1)
    t.circle(350 * s,104)
    t.left(90)
    t.circle(200 * s,105)
    t.circle(-500 * s,63)
    t.penup()
    t.goto(170 * s,-30 * s)
    t.pendown()
    t.left(160)
    degree_curve(20, 2500 * s)
    degree_curve(220, 250 * s, -1)
    
    # 绘制一个绿色叶子
    t.fillcolor('green')
    t.penup()
    t.goto(670 * s,-180 * s)
    t.pendown()
    t.right(140)
    t.begin_fill()
    t.circle(300 * s, 120)
    t.left(60)
    t.circle(300 * s, 120)
    t.end_fill()
    t.penup()
    t.goto(180 * s, -550 * s)
    t.pendown()
    t.right(85)
    t.circle(600 * s, 40)
    
    # 绘制另一个绿色叶子
    t.penup()
    t.goto(-150 * s,-1000 * s)
    t.pendown()
    t.begin_fill()
    t.rt(120)
    t.circle(300 * s,115)
    t.left(75)
    t.circle(300 * s,100)
    t.end_fill()
    t.penup()
    t.goto(430 * s,-1070 * s)
    t.pendown()
    t.right(30)
    t.circle(-600 * s,35)
    t.exitonclick()

# 程序入口
if __name__=="__main__":
    print('开始绘制玫瑰花')
    draw_rose()
    print('结束绘制玫瑰花')
    # input('暂停，等待输入（输入任意内容按回车键可退出）：')