#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/7/4

import requests as r
import json
import pytest
import allure

class Test_config():

    @allure.step("获取服务器信息")
    def test_fuwuqi(self):
        self.url = 'http://223.87.179.196/api/ServiceCenter.do?action=getAppServer&verf=93A98F16E15E7744718827D14B7E7BE3&pv=3&data=HQdLXSpWXlZfS1xYGAdLXSpZXl5YS1xYDQdLXSpYXl5fS1xYCh1LXSpbX15WS1xYGABLXSpfQFtAXkBZW1ZLXFgYDUtdKllbVktcWBsHS10qS1xYGx5LXSpLXFgbAEtdKktcW1ssLSNLXFtbKl1aVl1WWlxeX1lLXFtaXh8fQA0BA0tcWBoDS10qIT4%2BITxfXx1LXFgDC0tdKlwKV1lbWV9cDFxfDVlXV1tLXFgDXEtdKlZYWVpYXV5dWFpdXFdXWUtcWB4AS10qS1xYAx1LXSpLXFgaGEtdKlxbS1xYABpLXSoZBwgHS1xYAg1LXSpLXFgNC0tdKktcWAIAS10qS1xYAg9LXSpLXFgCAUtdKktcWB4cS10qS1xbK1tLXFtWLUtcW1dZS1xbK1pLXFssL0tcWy8tS1xbK1tLXFssVktcW1ZcS1xYDRpLXSpLXFsrW0tcW1YtS1xbV1lLXFsrWktcWywvS1xbLy1LXFsrW0tcWyxWS1xbVlxLXFgNAUtdKktcWB0aS10qS1xYARhLXSoPAAocAQcKWUBfQF9LXFgaDEtdKiE%2BPiFLXFgdGUtdKl9eVl5LXFgdBktdKlxeX1hLXFgNG0tdKi8vHA0GWFpLXCw%2BHAENCx0dARxLXCwcCxhLXCxcS1wsS1xbXFYPDxwNBlhaS1xbXFdLXFgdAUtdKh4BHBocDwcaS1xYAglLXSpLXFgNHEtdKktcWB0KS10qDQYHAA8DGx0HDQ%3D%3D&format=json'
        result = r.get(self.url)
        rejson = json.loads(result.text)
        assert rejson['msg']== 'Success'
        assert result.status_code ==200

    @allure.step("获取配置")
    def test_conf(self):
        self.url = 'http://master1.china-plus.net/api/ServiceCenter.do?action=getConf&format=json&verf=7D0E398FFC95C31F227B982F3AC2298F&pv=3&data=HQdLXSpWXlZfS1xYGAdLXSpZXl5YS1xYDQdLXSpYXl5fS1xYCh1LXSpbX15WS1xYGABLXSpfQFtAXkBZW1ZLXFgYDUtdKllbVktcWBsHS10qS1xYGx5LXSpLXFgbAEtdKktcW1ssLSNLXFtbKl1aVl1WWlxeX1lLXFtaXh8fQA0BA0tcWBoDS10qIT4%2BITxfXx1LXFgDC0tdKlwKV1lbWV9cDFxfDVlXV1tLXFgDXEtdKlZYWVpYXV5dWFpdXFdXWUtcWB4AS10qS1xYAx1LXSpLXFgaGEtdKlxbS1xYABpLXSoZBwgHS1xYAg1LXSpLXFgNC0tdKktcWAIAS10qS1xYAg9LXSpLXFgCAUtdKktcWB4cS10qS1xbK1tLXFtWLUtcW1dZS1xbK1pLXFssL0tcWy8tS1xbK1tLXFssVktcW1ZcS1xYDRpLXSpLXFsrW0tcW1YtS1xbV1lLXFsrWktcWywvS1xbLy1LXFsrW0tcWyxWS1xbVlxLXFgNAUtdKktcWB0aS10qS1xYARhLXSoPAAocAQcKWUBfQF9LXFgaDEtdKiE%2BPiFLXFgdGUtdKl9eVl5LXFgdBktdKlxeX1hLXFgNG0tdKi8vHA0GWFpLXCw%2BHAENCx0dARxLXCwcCxhLXCxcS1wsS1xbXFYPDxwNBlhaS1xbXFdLXFgdAUtdKh4BHBocDwcaS1xYAglLXSpLXFgNHEtdKktcWB0KS10qDQYHAA8DGx0HDUtcWA%3D%3D'
        result = r.get(self.url)
        rejson = json.loads(result.text)
        assert rejson['msg']== 'Success'
        assert result.status_code ==200

    @allure.step("获取语言列表")
    def test_yuyan(self):
        self.url = 'http://master1.china-plus.net/api/ServiceCenter.do?action=CNGetLanguageList&format=json&verf=7D0E398FFC95C31F227B982F3AC2298F&pv=3&data=HQdLXSpWXlZfS1xYGAdLXSpZXl5YS1xYDQdLXSpYXl5fS1xYCh1LXSpbX15WS1xYGABLXSpfQFtAXkBZW1ZLXFgYDUtdKllbVktcWBsHS10qS1xYGx5LXSpLXFgbAEtdKktcW1ssLSNLXFtbKl1aVl1WWlxeX1lLXFtaXh8fQA0BA0tcWBoDS10qIT4%2BITxfXx1LXFgDC0tdKlwKV1lbWV9cDFxfDVlXV1tLXFgDXEtdKlZYWVpYXV5dWFpdXFdXWUtcWB4AS10qS1xYAx1LXSpLXFgaGEtdKlxbS1xYABpLXSoZBwgHS1xYAg1LXSpLXFgNC0tdKktcWAIAS10qS1xYAg9LXSpLXFgCAUtdKktcWB4cS10qS1xbK1tLXFtWLUtcW1dZS1xbK1pLXFssL0tcWy8tS1xbK1tLXFssVktcW1ZcS1xYDRpLXSpLXFsrW0tcW1YtS1xbV1lLXFsrWktcWywvS1xbLy1LXFsrW0tcWyxWS1xbVlxLXFgNAUtdKktcWB0aS10qS1xYARhLXSoPAAocAQcKWUBfQF9LXFgaDEtdKiE%2BPiFLXFgdGUtdKl9eVl5LXFgdBktdKlxeX1hLXFgNG0tdKi8vHA0GWFpLXCw%2BHAENCx0dARxLXCwcCxhLXCxcS1wsS1xbXFYPDxwNBlhaS1xbXFdLXFgdAUtdKh4BHBocDwcaS1xYAglLXSpLXFgNHEtdKktcWB0KS10qDQYHAA8DGx0HDUtcWA%3D%3D'
        result = r.get(self.url)
        rejson = json.loads(result.text)
        assert rejson['msg']== 'Success'
        assert result.status_code ==200

    @allure.step("获取更新信息")
    def test_gengxin(self):
        self.url = 'http://master1.china-plus.net/api/ServiceCenter.do?action=getUpdateMessage&format=json&verf=7D0E398FFC95C31F227B982F3AC2298F&pv=3&data=HQdLXSpWXlZfS1xYGAdLXSpZXl5YS1xYDQdLXSpYXl5fS1xYCh1LXSpbX15WS1xYGABLXSpfQFtAXkBZW1ZLXFgYDUtdKllbVktcWBsHS10qS1xYGx5LXSpLXFgbAEtdKktcW1ssLSNLXFtbKl1aVl1WWlxeX1lLXFtaXh8fQA0BA0tcWBoDS10qIT4%2BITxfXx1LXFgDC0tdKlwKV1lbWV9cDFxfDVlXV1tLXFgDXEtdKlZYWVpYXV5dWFpdXFdXWUtcWB4AS10qS1xYAx1LXSpLXFgaGEtdKlxbS1xYABpLXSoZBwgHS1xYAg1LXSpLXFgNC0tdKktcWAIAS10qS1xYAg9LXSpLXFgCAUtdKktcWB4cS10qS1xbK1tLXFtWLUtcW1dZS1xbK1pLXFssL0tcWy8tS1xbK1tLXFssVktcW1ZcS1xYDRpLXSpLXFsrW0tcW1YtS1xbV1lLXFsrWktcWywvS1xbLy1LXFsrW0tcWyxWS1xbVlxLXFgNAUtdKktcWB0aS10qS1xYARhLXSoPAAocAQcKWUBfQF9LXFgaDEtdKiE%2BPiFLXFgdGUtdKl9eVl5LXFgdBktdKlxeX1hLXFgNG0tdKi8vHA0GWFpLXCw%2BHAENCx0dARxLXCwcCxhLXCxcS1wsS1xbXFYPDxwNBlhaS1xbXFdLXFgdAUtdKh4BHBocDwcaS1xYAglLXSpLXFgNHEtdKktcWB0KS10qDQYHAA8DGx0HDUtcWA%3D%3D'
        result = r.get(self.url)
        rejson = json.loads(result.text)
        assert rejson['msg']== 'Success'
        assert result.status_code ==200



if __name__ == "__main__":
    pytest.main()