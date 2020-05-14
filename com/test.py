#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
r = requests.get('http://www.taobao.com')
print(r.status_code)
print(r.encoding)
