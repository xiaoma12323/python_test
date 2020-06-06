#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from turtle import *

# 设置色彩模式是RGB:
colormode(255)

lt(90)

lv = 14
le = 120
s = 45

width(lv)

# 初始化RGB颜色:
r = 0
g = 0
b = 0
pencolor(r, g, b)

penup()
bk(le)
pendown()
fd(le)


def draw_tree(bl, level):
    global r, g, b
    # save the current pen width
    w = width()

    # narrow the pen width
    width(w * 3.0 / 4.0)
    # set color:
    r = r + 1
    g = g + 2
    b = b + 3
    pencolor(r % 200, g % 200, b % 200)

    bl = 3.0 / 4.0 * bl

    lt(s)
    fd(bl)

    if level < lv:
        draw_tree(bl, level + 1)
    bk(bl)
    rt(2 * s)
    fd(bl)

    if level < lv:
        draw_tree(bl, level + 1)
    bk(bl)
    lt(s)

    # restore the previous pen width
    width(w)


speed("fastest")

draw_tree(le, 4)

done()
