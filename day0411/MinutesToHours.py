#!/usr/bin/env python3
import sys
def Hours(m):
    if m < 0:
        raise ValueError('You entered value is Error!')
    else:
        print('{} H,{} M'.format(int(m/60),m%60))
try:
    Hours(int(sys.argv[1]))
except:
    print('参数错误！')
#print('这是用来将用户输入的分钟数转化为小时数和分钟数。')
