#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from turtle import *

ht()

speed(0)

penup()

goto(0, 120)

pendown()

for i in range(12):

    right(90)

    forward(10)

    backward(10)

    left(90)

    for j in range(4):
        circle(-120, 6)

        right(90)

        forward(5)

        backward(5)

        left(90)

    circle(-120, 6)

penup()

goto(0, 0)

pendown()


def pin(p, long, angle):
    p.left(90 - angle)

    p.forward(long)


def undo_pin(p):
    for _ in range(2):
        p.undo()


fen = clone()

miao = clone()

sec_long = 100

min_long = 60

sec_ang = 0

min_ang = 0

while True:

    pin(fen, min_long, min_ang)

    for i in range(60):
        pin(miao, sec_long, sec_ang + (i * 6))

        time.sleep(0.93)

        undo_pin(miao)

    undo_pin(fen)

    min_ang += 6
