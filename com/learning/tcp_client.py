#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('127.0.0.1', 9999))
# 接受欢迎信息
print(s.recv(1024).decode('utf-8'))

for data in [b'Michael', b'Trevor', b'Franklin']:
    # 发送数据
    s.send(data)
    # 接受数据
    print(s.recv(1024).decode('utf-8'))

s.send(b'exit')
s.close()
