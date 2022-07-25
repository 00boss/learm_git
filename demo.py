# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 15:38:17 2022

@author: admin
"""

import sys
import os

#输出 可执行文件/py文件，所在的位置
print(sys.argv)

print(sys.argv[0])
print("修改bug")
#找到差数的绝对路劲
print(os.path.realpath(sys.argv[0]))
print("尝试git分支")
print("分支开发完成")

