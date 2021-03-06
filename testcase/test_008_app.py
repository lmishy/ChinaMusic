#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/7/4

import requests as r
import json
import pytest
import allure

class Test_config():

    @allure.step("获取登录用户信息")
    def test_loginmg(self):
        self.url = 'http://master1.china-plus.net/api/ServiceCenter.do?action=getUserInfo&format=json&verf=AE175D6FC677930DA3504F7AC9486A05&pv=3&data=HQdLXSpWXlZfS1xYGAdLXSpZXl5YS1xYDQdLXSpYXl5fS1xYCh1LXSpbX15WS1xYGABLXSpfQFtAXkBZW1ZLXFgYDUtdKllbVktcWBsHS10qS1xYGx5LXSpLXFgbAEtdKktcW1ssLSNLXFtbKl1aVl1WWlxeX1lLXFtaXh8fQA0BA0tcWBoDS10qIT4%2BITxfXx1LXFgDC0tdKlwKV1lbWV9cDFxfDVlXV1tLXFgDXEtdKlZYWVpYXV5dWFpdXFdXWUtcWB4AS10qS1xYAx1LXSpLXFgaGEtdKlxbS1xYABpLXSoZBwgHS1xYAg1LXSpLXFgNC0tdKktcWAIAS10qS1xYAg9LXSpLXFgCAUtdKktcWB4cS10qS1xbK1tLXFtWLUtcW1dZS1xbK1pLXFssL0tcWy8tS1xbK1tLXFssVktcW1ZcS1xYDRpLXSpLXFsrW0tcW1YtS1xbV1lLXFsrWktcWywvS1xbLy1LXFsrW0tcWyxWS1xbVlxLXFgNAUtdKktcWB0aS10qS1xYARhLXSoPAAocAQcKWUBfQF9LXFgaDEtdKiE%2BPiFLXFgdGUtdKl9eVl5LXFgdBktdKlxeX1hLXFgNG0tdKi8vHA0GWFpLXCw%2BHAENCx0dARxLXCwcCxhLXCxcS1wsS1xbXFYPDxwNBlhaS1xbXFdLXFgdAUtdKh4BHBocDwcaS1xYAglLXSpLXFgNHEtdKktcWB0KS10qDQYHAA8DGx0HDUtcWBsAS10qS1ssLSNLWypdWlZdVlpcXl9ZS1peHx9ADQED'
        result = r.get(self.url)
        rejson = json.loads(result.text)
        assert rejson['msg']== 'Success'
        assert result.status_code ==200

    @allure.step("获取分享图标")
    def test_share(self):
        self.url = 'http://223.87.178.9/api/ServiceCenter.do?action=getWeiboSendPics&verf=7D0E398FFC95C31F227B982F3AC2298F&pv=3&data=HQdLXSpWXlZfS1xYGAdLXSpZXl5YS1xYDQdLXSpYXl5fS1xYCh1LXSpbX15WS1xYGABLXSpfQFtAXkBZW1ZLXFgYDUtdKllbVktcWBsHS10qS1xYGx5LXSpLXFgbAEtdKktcW1ssLSNLXFtbKl1aVl1WWlxeX1lLXFtaXh8fQA0BA0tcWBoDS10qIT4%2BITxfXx1LXFgDC0tdKlwKV1lbWV9cDFxfDVlXV1tLXFgDXEtdKlZYWVpYXV5dWFpdXFdXWUtcWB4AS10qS1xYAx1LXSpLXFgaGEtdKlxbS1xYABpLXSoZBwgHS1xYAg1LXSpLXFgNC0tdKktcWAIAS10qS1xYAg9LXSpLXFgCAUtdKktcWB4cS10qS1xbK1tLXFtWLUtcW1dZS1xbK1pLXFssL0tcWy8tS1xbK1tLXFssVktcW1ZcS1xYDRpLXSpLXFsrW0tcW1YtS1xbV1lLXFsrWktcWywvS1xbLy1LXFsrW0tcWyxWS1xbVlxLXFgNAUtdKktcWB0aS10qS1xYARhLXSoPAAocAQcKWUBfQF9LXFgaDEtdKiE%2BPiFLXFgdGUtdKl9eVl5LXFgdBktdKlxeX1hLXFgNG0tdKi8vHA0GWFpLXCw%2BHAENCx0dARxLXCwcCxhLXCxcS1wsS1xbXFYPDxwNBlhaS1xbXFdLXFgdAUtdKh4BHBocDwcaS1xYAglLXSpLXFgNHEtdKktcWB0KS10qDQYHAA8DGx0HDUtcWA%3D%3D&format=json'
        result = r.get(self.url)
        rejson = json.loads(result.text)
        assert rejson['msg']== 'Success'
        assert result.status_code ==200

    @allure.step("获取推送token")
    def test_token(self):
        self.url = 'http://master1.china-plus.net/api/ServiceCenter.do?action=upPushToken&format=json&verf=C48A2B1705ECDE29865573757871BFD8&pv=3&data=HQdLXSpWXlZfS1xYGAdLXSpZXl5YS1xYDQdLXSpYXl5fS1xYCh1LXSpbX15WS1xYGABLXSpfQFtAXkBZW1ZLXFgYDUtdKllbVktcWBsHS10qS1xYGx5LXSpLXFgbAEtdKktcW1ssLSNLXFtbKl1aVl1WWlxeX1lLXFtaXh8fQA0BA0tcWBoDS10qIT4%2BITxfXx1LXFgDC0tdKlwKV1lbWV9cDFxfDVlXV1tLXFgDXEtdKlZYWVpYXV5dWFpdXFdXWUtcWB4AS10qS1xYAx1LXSpLXFgaGEtdKlxbS1xYABpLXSoZBwgHS1xYAg1LXSpLXFgNC0tdKktcWAIAS10qS1xbK1tLXFtXLEtcW1csS1xbK1tLXFssWUtcW1cqS1xbK1lLXFtXLUtcW1ZfS1xbK1hLXFtWVktcW1deS1xbK1dLXFtWXUtcWywqS1xbK1tLXFssVktcW1ZcS1xbK1hLXFsvKktcWy9YS1xbK1pLXFssK0tcWy8oS1xbK1tLXFtWLUtcWywvS1xbK1tLXFtXLEtcW1csS1xbK1tLXFssWUtcW1cqS1xbK1lLXFtXLUtcW1ZfS1xbK1hLXFtWVktcW1deS1xbK1dLXFtWXUtcWywqS1xbK1tLXFssVktcW1ZcS1xbK1hLXFsvKktcWy9YS1xbK1pLXFssK0tcWy8oS1xbK1tLXFtWLUtcWywvS1xbK1tLXFtWW0tcW1ZdS1xbK1tLXFtWKktcW1YrS1xbK1ZLXFssWUtcWy8oXEtcWytbS1xbVihLXFssWUtcWytaS1xbLC9LXFssL0tcWytWS1xbL19LXFtWLUtcWytbS1xbL1pLXFsvV0tcWytYS1xbL19LXFsvW0tcWAIPS10qXV5AW1ZZWVlYS1xYAgFLXSpfXlpAXltdWF1ZS1xYHhxLXSpLXFsrW0tcW1csS1xbVyxLXFsrW0tcWyxZS1xbVypLXFsrWUtcW1ctS1xbVl9LXFgNGktdKktcWytYS1xbVlZLXFtXXktcWytXS1xbVl1LXFssKktcWytbS1xbLFZLXFtWXEtcWA0BS10qS1xbK1hLXFsvKktcWy9YS1xbK1pLXFssK0tcWy8oS1xbK1tLXFtWLUtcWywvS1xYHRpLXSpLXFsrW0tcW1csS1xbVyxLXFsrW0tcWyxZS1xbVypLXFsrWUtcW1ctS1xbVl9LXFsrWEtcW1ZWS1xbV15LXFsrV0tcW1ZdS1xbLCpLXFsrW0tcWyxWS1xbVlxLXFsrWEtcWy8qS1xbL1hLXFsrWktcWywrS1xbLyhLXFsrW0tcW1YtS1xbLC9LXFsrW0tcW1ZbS1xbVl1LXFsrW0tcW1YqS1xbVitLXFsrVktcWyxZS1xbLyhcS1xbK1tLXFtWKEtcWyxZS1xbK1pLXFssL0tcWywvS1xbK1ZLXFsvX0tcW1YtS1xbK1tLXFsvWktcWy9XS1xbK1hLXFsvX0tcWy9bS1xYARhLXSoPAAocAQcKWUBfQF9LXFgaDEtdKiE%2BPiFLXFgdGUtdKl9eVl5LXFgdBktdKlxeX1hLXFgNG0tdKi8vHA0GWFpLXCw%2BHAENCx0dARxLXCwcCxhLXCxcS1wsS1xbXFYPDxwNBlhaS1xbXFdLXFgdAUtdKh4BHBocDwcaS1xYAglLXSpLXFgNHEtdKktcWB0KS10qDQYHAA8DGx0HDUtcWB4aAEtdKghaClpeVgtWD1cNWVheC1tfDQ8PWlxcWA9dXA8LDA1YS1xYDRoHS10qCFoKWl5WC1YPVw1ZWF4LW18NDw9aXFxYD11cDwsMDVg%3D'
        result = r.get(self.url)
        rejson = json.loads(result.text)
        assert rejson['msg']== 'Success'
        assert result.status_code ==200

    @allure.step("获取推送详情")
    def test_push(self):
        self.url = 'http://master1.china-plus.net/api/ServiceCenter.do?action=getPushDetails&format=json&verf=1E43D07543425B083D48FFD4C11A5406&pv=3&data=HQdLXSpWXlZfS1xYGAdLXSpZXl5YS1xYDQdLXSpYXl5fS1xYCh1LXSpbX15WS1xYGABLXSpfQFtAXkBZW1ZLXFgYDUtdKllbVktcWBsHS10qS1xYGx5LXSpLXFgbAEtdKktcW1ssLSNLXFtbKl1aVl1WWlxeX1lLXFtaXh8fQA0BA0tcWBoDS10qIT4%2BITxfXx1LXFgDC0tdKlwKV1lbWV9cDFxfDVlXV1tLXFgDXEtdKlZYWVpYXV5dWFpdXFdXWUtcWB4AS10qS1xYAx1LXSpLXFgaGEtdKlxbS1xYABpLXSoZBwgHS1xYAg1LXSpLXFgNC0tdKktcWAIAS10qS1xYAg9LXSpLXFgCAUtdKktcWB4cS10qS1xbK1tLXFtWLUtcW1dZS1xbK1pLXFssL0tcWy8tS1xbK1tLXFssVktcW1ZcS1xYDRpLXSpLXFsrW0tcW1YtS1xbV1lLXFsrWktcWywvS1xbLy1LXFsrW0tcWyxWS1xbVlxLXFgNAUtdKktcWB0aS10qS1xYARhLXSoPAAocAQcKWUBfQF9LXFgaDEtdKiE%2BPiFLXFgdGUtdKl9eVl5LXFgdBktdKlxeX1hLXFgNG0tdKi8vHA0GWFpLXCw%2BHAENCx0dARxLXCwcCxhLXCxaS1wsS1xbXFYPDxwNBlhaS1xbXFdLXFgdAUtdKh4BHBocDwcaS1xYAglLXSpLXFgNHEtdKktcWB0KS10qDQYHAA8DGx0HDUtcWA%3D%3D'
        result = r.get(self.url)
        rejson = json.loads(result.text)
        assert rejson['msg']== 'Success'
        assert result.status_code ==200

    @allure.step("获取广告URL信息")
    def test_AD(self):
        self.url = 'http://master1.china-plus.net/api/ServiceCenter.do?action=getPushDetails&format=json&verf=1E43D07543425B083D48FFD4C11A5406&pv=3&data=HQdLXSpWXlZfS1xYGAdLXSpZXl5YS1xYDQdLXSpYXl5fS1xYCh1LXSpbX15WS1xYGABLXSpfQFtAXkBZW1ZLXFgYDUtdKllbVktcWBsHS10qS1xYGx5LXSpLXFgbAEtdKktcW1ssLSNLXFtbKl1aVl1WWlxeX1lLXFtaXh8fQA0BA0tcWBoDS10qIT4%2BITxfXx1LXFgDC0tdKlwKV1lbWV9cDFxfDVlXV1tLXFgDXEtdKlZYWVpYXV5dWFpdXFdXWUtcWB4AS10qS1xYAx1LXSpLXFgaGEtdKlxbS1xYABpLXSoZBwgHS1xYAg1LXSpLXFgNC0tdKktcWAIAS10qS1xYAg9LXSpLXFgCAUtdKktcWB4cS10qS1xbK1tLXFtWLUtcW1dZS1xbK1pLXFssL0tcWy8tS1xbK1tLXFssVktcW1ZcS1xYDRpLXSpLXFsrW0tcW1YtS1xbV1lLXFsrWktcWywvS1xbLy1LXFsrW0tcWyxWS1xbVlxLXFgNAUtdKktcWB0aS10qS1xYARhLXSoPAAocAQcKWUBfQF9LXFgaDEtdKiE%2BPiFLXFgdGUtdKl9eVl5LXFgdBktdKlxeX1hLXFgNG0tdKi8vHA0GWFpLXCw%2BHAENCx0dARxLXCwcCxhLXCxaS1wsS1xbXFYPDxwNBlhaS1xbXFdLXFgdAUtdKh4BHBocDwcaS1xYAglLXSpLXFgNHEtdKktcWB0KS10qDQYHAA8DGx0HDUtcWA%3D%3D'
        result = r.get(self.url)
        rejson = json.loads(result.text)
        assert rejson['msg']== 'Success'
        assert result.status_code ==200


    @allure.step("用户偏向")
    def test_prefer(self):
        self.url = 'http://master1.china-plus.net/api/ServiceCenter.do?action=userPreference&format=json&verf=230289EF744FB9D244222395FE2277D8&pv=3&data=HQdLXSpWXlZfS1xYGAdLXSpZXl5YS1xYDQdLXSpYXl5fS1xYCh1LXSpbX15WS1xYGABLXSpfQFtAXkBZW1ZLXFgYDUtdKllbVktcWBsHS10qS1xYGx5LXSpLXFgbAEtdKktcW1ssLSNLXFtbKl1aVl1WWlxeX1lLXFtaXh8fQA0BA0tcWBoDS10qIT4%2BITxfXx1LXFgDC0tdKlwKV1lbWV9cDFxfDVlXV1tLXFgDXEtdKlZYWVpYXV5dWFpdXFdXWUtcWB4AS10qS1xYAx1LXSpLXFgaGEtdKlxbS1xYABpLXSoZBwgHS1xYAg1LXSpLXFgNC0tdKktcWAIAS10qS1xbK1tLXFtXLEtcW1csS1xbK1tLXFssWUtcW1cqS1xbK1lLXFtXLUtcW1ZfS1xbK1hLXFtWVktcW1deS1xbK1dLXFtWXUtcWywqS1xbK1tLXFssVktcW1ZcS1xbK1hLXFsvKktcWy9YS1xbK1pLXFssK0tcWy8oS1xbK1tLXFtWLUtcWywvS1xbK1tLXFtXLEtcW1csS1xbK1tLXFssWUtcW1cqS1xbK1lLXFtXLUtcW1ZfS1xbK1hLXFtWVktcW1deS1xbK1dLXFtWXUtcWywqS1xbK1tLXFssVktcW1ZcS1xbK1hLXFsvKktcWy9YS1xbK1pLXFssK0tcWy8oS1xbK1tLXFtWLUtcWywvS1xbK1tLXFtWW0tcW1ZdS1xbK1tLXFtWKktcW1YrS1xbK1ZLXFssWUtcWy8oXEtcWytbS1xbVihLXFssWUtcWytaS1xbLC9LXFssL0tcWytWS1xbL19LXFtWLUtcWytbS1xbL1pLXFsvV0tcWytYS1xbL19LXFsvW0tcWAIPS10qXV5AW1ZZWVlYS1xYAgFLXSpfXlpAXltdWF1ZS1xYHhxLXSpLXFsrW0tcW1csS1xbVyxLXFsrW0tcWyxZS1xbVypLXFsrWUtcW1ctS1xbVl9LXFgNGktdKktcWytYS1xbVlZLXFtXXktcWytXS1xbVl1LXFssKktcWytbS1xbLFZLXFtWXEtcWA0BS10qS1xbK1hLXFsvKktcWy9YS1xbK1pLXFssK0tcWy8oS1xbK1tLXFtWLUtcWywvS1xYHRpLXSpLXFsrW0tcW1csS1xbVyxLXFsrW0tcWyxZS1xbVypLXFsrWUtcW1ctS1xbVl9LXFsrWEtcW1ZWS1xbV15LXFsrV0tcW1ZdS1xbLCpLXFsrW0tcWyxWS1xbVlxLXFsrWEtcWy8qS1xbL1hLXFsrWktcWywrS1xbLyhLXFsrW0tcW1YtS1xbLC9LXFsrW0tcW1ZbS1xbVl1LXFsrW0tcW1YqS1xbVitLXFsrVktcWyxZS1xbLyhcS1xbK1tLXFtWKEtcWyxZS1xbK1pLXFssL0tcWywvS1xbK1ZLXFsvX0tcW1YtS1xbK1tLXFsvWktcWy9XS1xbK1hLXFsvX0tcWy9bS1xYARhLXSoPAAocAQcKWUBfQF9LXFgaDEtdKiE%2BPiFLXFgdGUtdKl9eVl5LXFgdBktdKlxeX1hLXFgNG0tdKi8vHA0GWFpLXCw%2BHAENCx0dARxLXCwcCxhLXCxcS1wsS1xbXFYPDxwNBlhaS1xbXFdLXFgdAUtdKh4BHBocDwcaS1xYAglLXSpLXFgNHEtdKktcWB0KS10qDQYHAA8DGx0HDUtcWB4IHUtdKktcW1ssS1xbWSxLXFtcXA8NGktcW1xcS1xbXS9LXFtcXA8KCktcW1xcS1xbXC1LXFtcXAcKS1xbXFxLXFtdL0tcW1xcS1xbXFxLXFtcLUtcW1xcBwAKCxZLXFtcXEtcW10vS1xbXFxLXFtcXEtcW1wtS1xbXFwcBwpLXFtcXEtcW10vS1xbXFxfXl5eW0tcW1xcS1xbXC1LXFtcXBwAC0tcW1xcS1xbXS9LXFtcXEtcW1xcS1xbXC1LXFtcXBwaHktcW1xcS1xbXS9LXFtcXAocDwgaLwIMGwNLXFtcXEtcW1wtS1xbXFwcGwJLXFtcXEtcW10vS1xbXFxLXFtcXEtcW1wtS1xbXFwdAEtcW1xcS1xbXS9LXFtcXEtcW1xcS1xbWSpLXFtbKg%3D%3D'
        result = r.get(self.url)
        rejson = json.loads(result.text)
        assert rejson['msg']== 'Success'
        assert result.status_code ==200


if __name__ == "__main__":
    pytest.main()