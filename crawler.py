import os, sys, time

import bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Crawler:
    """
    Web crawler
    
    Crawler(user_agent)
        user_agent : User-Agent(default : "windows10 chrome")
    """
    # User-Agent
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100"
    
    def __init__(self, user_agent=user_agent):
        try:
            self.user_agent = r"--user-agent=" + user_agent
            print(self.user_agent)

            # Chrome オプション定義
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument(self.user_agent)

            # selenium 起動
            print("selenium 起動...")
            self.driver = webdriver.Chrome(chrome_options=options)
            print("OK.")
        except Exception as e:
            raise Exception(e.args[0])
        

    def get_html(self, url):
        """
        url の html データを selenium で取得

        get_html(url)
            url : 取得するページのurl
        """
        try:
            # ページを開く
            self.driver.get(url)
            # ページが読み込まれるまで待機
            wait.until(ec.presence_of_all_elements_located)

            # データ取得
            #resp = requests.get(url, timeout=3.5, headers=self.headers)
            #resp.raise_for_status()
            #return bs4.BeautifulSoup(resp.text, "html.parser")
            return driver.page_source
        except Exception as e:
            raise Exception(e.args[0])

    def __repr__(self):
        """
        print() の表示内容
            [crawler] + self.value
        """
        value = "[crawler]" + self.value
        return value

if __name__ == '__main__':
    crawler = Crawler()
    #html = crawler.get_html("https://google.com/")
    #print(html)