
#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/7/3
import uiautomator2 as u2
from time import sleep
from random import choice
import pytest


url = '10.0.0.7'
def fun():
    d = u2.connect(url)
    d.app_start("com.chinamobile.cloudapp")
    sleep(5)
    itab = [
        "com.chinamobile.cloudapp:id/root_bottom_home_tab_1",
        "com.chinamobile.cloudapp:id/root_bottom_home_tab_2",
        "com.chinamobile.cloudapp:id/root_bottom_home_tab_3",
        "com.chinamobile.cloudapp:id/root_bottom_home_tab_4",
        "com.chinamobile.cloudapp:id/root_bottom_home_tab_5"]
    while(True):
        d(resourceId= choice(itab)).click()
        sleep(0.1)


if __name__ == "__main__":
    fun()