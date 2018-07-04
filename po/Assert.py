#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/7/4


def asser(func):
    def wrapper(*args, **kwargs):
        print("用例开始执行......")
        try:
            func(*args, **kwargs)
        except Exception as e:
            print("用例开始执行......")


            d.app_stop("com.chinamobile.cloudapp")

    return wrapper