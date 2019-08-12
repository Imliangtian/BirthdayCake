#   Author :  Liang Tian
#   MadeDate : 2018-07-07
# coding: utf-8
from turtle import *
import pygame
import time

#  蛋糕盘部分
def cake(x,y):
    penup()     # 起笔
    goto(x,y)   #移动到坐标（x,y)
    pendown()   #落笔
    pensize(10) #画笔大小
    pencolor('yellow')  #画笔颜色
    speed(5)    #画笔速度
    setheading(90)  #设置画笔方向角度为90度
    begin_fill()    #开始填充
    fillcolor('white')  #填充颜色为白色
    hideturtle()    #隐藏画笔箭头
    a = 1.5
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.3
            left(3)  # 向左转3度
            forward(a)  # 向前走a的步长
        else:
            a = a - 0.3
            left(3) # 向左转3度
            forward(a)  # 向前走a的步长
    end_fill()  #结束填充

#  蛋糕躯体部分
def cakebody(x, y):
    penup() #起笔
    goto(x, y)  #移动到坐标（x,y)
    pendown()   #落笔
    pensize(10) #画笔大小
    pencolor('yellow')  #画笔颜色为黄色
    speed(5)    #画笔速度
    setheading(270) #设置画笔方向角度为270度
    forward(100)    #向前走100步长
    penup() #起笔
    goto(x - 277, y)    #移动到坐标为（x-277，y）
    pendown()   #落笔
    pensize(10) #画笔大小
    pencolor('yellow')  #画笔颜色为黄色
    speed(5)    #画笔速度
    setheading(270) #设置画笔方向角度270度
    forward(100)    #向前走100步长
    setheading(310) #设置画笔方向角度310度
    circle(180, 100)    #画半径=180，弧度=100的圆弧
    begin_fill()    #开始填充
    fillcolor('white')  #填充颜色为白色
    hideturtle()    #隐藏画笔箭头
    end_fill()  #结束填充

# 生日祝福文字
def wishes(x,y):
    names=['刘','敏',':'] #定义名字
    wishes=['生','日','快','樂']    #定义祝福内容
    penup() #起笔
    goto(x,y)   #移动到坐标（x,y)
    pencolor('green')   #画笔颜色为绿色
    for name in names:  #按照格式依次输出名字
     write(name, move=True, font = ("隶书", 18,"bold"))   #打印名字
     time.sleep(0.4)    #设置时间间隔0.4秒
    penup() #起笔
    goto(x, y-30)   #移动到坐标（x，y-30）
    pencolor('red') #画笔颜色为红色
    for wish in wishes: #按照格式依次输出祝福内容
     write(wish, move=True,font = ("隶书", 22,"bold"))    #打印祝福内容
     time.sleep(0.4)    #设置时间间隔为0.4秒

# 生日祝福标语
def slogan(x,y):
    color=['#FFA500','#40E0D0','#FF0000','#FFC0CB','#4682B4','#FFFFFF','#00CED1','#FF0000','#FFC0CB','#FFA500',
           '#C71585', '#FFA500','#FF0000','#FFC0CB']    #定义颜色数组
    slogan = ['H', 'a', 'p', 'p', 'y', ' ', 'B', 'i', 'r', 't', 'h', 'd', 'a', 'y'] #定义生日祝福标语
    i=0
    penup() #起笔
    goto(x, y)  #移动到坐标（x,y)
    for slogan in slogan:   #按照格式依次输出生日祝福标语
        pencolor(color[i])  #切换不同颜色
        write(slogan,move=True,font=("harlow solid italic",35,"bold"))  #打印生日祝福标语
        time.sleep(0.3) #设置时间间隔0.3秒
        i = i + 1   #逐次加1

# 心形眼睛
def heart(x,y):
    penup() #起笔
    goto(x,y)   #移动到坐标（x,y）
    pendown()   #落笔
    pensize(3)  #画笔大小
    color('red','pink') #画笔颜色红色，填充颜色粉色
    speed(10)   #画笔速度
    setheading(0)   #设置画笔方向角度为0度
    begin_fill()    #开始填充
    left(140)   #向左转140度
    forward(20) #向前移动20步长
    for i in range(200):
        right(1)    #向右转1度
        forward(0.18)   #向前移动0.18步长
    left(120)   #向左转120度
    for i in range(200):
        right(1)    #向右转1度
        forward(0.18)   #向前移动0.18步长
    forward(20) #向前移动20步长
    end_fill()  #结束填充

# 嘴巴
def mouth(x,y):
    penup() #起笔
    goto(x, y)  #移动到坐标（x,y)
    pendown()   #落笔
    pensize(8)  #画笔大小
    color('red', 'pink')    #画笔颜色红色，填充颜色粉色
    speed(10)   #画笔速度
    setheading(300) #设置画笔方向角度为300度
    begin_fill()    #开始填充
    circle(40,120)  #画半径=40，弧度=120的圆弧

# 生日蜡烛
def candle(x,y,color):
    penup() #起笔
    goto(x,y)   #移动到坐标（x,y)
    pendown()   #落笔
    pensize(2)  #画笔大小
    pencolor(color) #画笔颜色
    speed(10)   #画笔速度
    setheading(90)  #画笔方向角度为90度
    begin_fill()    #开始填充
    fillcolor(color)    #填充颜色
    forward(90) #向前移动90步长
    right(90)   #向右转90度
    forward(3)  #向前移动3步长
    setheading(60)  #画笔方向角度为60度
    circle(60,15)   #画半径=60，弧度=15的圆弧
    right(155)  #向右转155度
    circle(60,15)   #画半径=60，弧度=15的圆弧
    setheading(0)   #画笔方向角度为0度
    forward(3)   #向前移动3步长
    right(90)    #向右转90度
    forward(89)  #向前移动89步长
    right(90)    #向右转90度
    forward(10)  #向前移动10步长
    end_fill()  #结束填充

# 星星
def star(x,y,color,n):
    penup() #起笔
    goto(x, y)  #移动到坐标（x,y)
    pendown()   #落笔
    pensize(2)  #画笔大小
    pencolor(color) #画笔颜色
    speed(10)   #画笔速度
    begin_fill()    #开始填充
    fillcolor(color)    #填充颜色
    for i in range(5):  #画五角星
        forward(n)  #向前移动n步长
        left(144)  # 左转144°
    end_fill()  #结束填充

# 播放音乐
def play(path):
    pygame.init()   #初始化
    track = pygame.mixer.music.load(path)   #加载路径下的音乐文件
    pygame.mixer.music.play()   #开始播放音乐
    time.sleep(32)  #缓冲32秒
    pygame.mixer.music.stop()   #结束播放

# 主程序
def main():
    cake(100,100)   #画蛋糕盘
    cakebody(100,100)   #画蛋糕躯体
    star(-150, 0, 'orange', 18) #画五角星
    star(-120,-35,'crimson',22) #画五角星
    star(-80,-18,'yellow',22)   #画五角星
    star(-40,-50,'skyblue',22)  #画五角星
    star(0,-18,'pink',22)   #画五角星
    star(40,-35,'violet',22)    #画五角星
    star(70,0,'lime',18)    #画五角星
    heart(-130,90)  #画心形左眼
    heart(55,90)    #画心形右眼
    mouth(-70,60)   #画嘴巴
    candle(-115,140,'red')  #画生日蜡烛
    candle(-80,140,'red')   #画生日蜡烛
    candle(-45, 140,'red')  #画生日蜡烛
    candle(-10, 140,'yellow')   #画生日蜡烛
    candle(25, 140,'red')   #画生日蜡烛
    wishes(-90, 110)    #打印生日祝福
    slogan(-200, 255)   #打印生日祝福标语
    play('刘敏生日快乐.mp3')  #播放生日快乐歌曲
    done()  #完成


if __name__ == '__main__':
        main()


