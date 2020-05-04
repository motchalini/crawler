import unittest

from crawler import Crawler

class TestCrawler(unittest.TestCase):

    def test_get_robots_txt(self):
        crawler = Crawler()

        # 1. 渡した url の robots.txt でスクレイピングが許可されている
        self.assertEqual(crawler.get_robots_txt("https://note.com/"), True)
        self.assertEqual(crawler.get_robots_txt("https://www.notion.so/"), True)
        self.assertEqual(crawler.get_robots_txt("https://github.com/humans.txt"), True)

        # 2. 渡した url の robots.txt が存在しない
        self.assertEqual(crawler.get_robots_txt("https://mikutter.hachune.net/"), True)
        self.assertEqual(crawler.get_robots_txt("https://app.simplenote.com/"), True)

        # 3. 渡した url の robots.txt でスクレイピングが許可されていない
        self.assertEqual(crawler.get_robots_txt("https://github.com/"), False)
        self.assertEqual(crawler.get_robots_txt("https://www.google.com/"), False)

        # 4. 渡した url が存在しない
        self.assertEqual(crawler.get_robots_txt("https://www.aaabbbccc.com/"), False)
        self.assertEqual(crawler.get_robots_txt("https://nooooooooote.com/"), False)
        

    def test_get_html(self):
        ok_url = "https://www.google.com"
        ng_url = "https://gooooole.com/"
        ok_params = {"q": "python"}
        ng_params = {"aaa"}
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                      AppleWebKit/537.36 (KHTML, like Gecko) \
                      Chrome/69.0.3497.100"
        ok_headers = {"User-Agent": user_agent}
        ng_headers = {"aaa"}
        title = "Google"

        crawler = Crawler()

        # 1) 引数は url のみ
        self.assertEqual(crawler.get_html(ok_url).title.get_text(), title)
        self.assertEqual(crawler.get_html(ng_url), None)

        # 2) 引数は url params のみ
        self.assertEqual(crawler.get_html(
            ok_url, params=ok_params).title.get_text(), title)
        self.assertEqual(crawler.get_html(ok_url, params=ng_params), None)
        self.assertEqual(crawler.get_html(ng_url, params=ok_params), None)
        self.assertEqual(crawler.get_html(ng_url, params=ng_params), None)

        # 3) 引数は url headers のみ
        self.assertEqual(crawler.get_html(
            ok_url, headers=ok_headers).title.get_text(), title)
        self.assertEqual(crawler.get_html(ok_url, headers=ng_headers), None)
        self.assertEqual(crawler.get_html(ng_url, headers=ok_headers), None)
        self.assertEqual(crawler.get_html(ng_url, headers=ng_headers), None)

        # 4) 引数は url params headers
        self.assertEqual(crawler.get_html(
            ok_url, params=ok_params, headers=ok_headers).title.get_text()
            , title)
        self.assertEqual(crawler.get_html(
            ok_url, params=ok_params, headers=ng_headers), None)
        self.assertEqual(crawler.get_html(
            ok_url, params=ng_params, headers=ok_headers), None)
        self.assertEqual(crawler.get_html(
            ok_url, params=ng_params, headers=ng_headers), None)
        self.assertEqual(crawler.get_html(
            ng_url, params=ok_params, headers=ok_headers), None)
        self.assertEqual(crawler.get_html(
            ng_url, params=ok_params, headers=ng_headers), None)
        self.assertEqual(crawler.get_html(
            ng_url, params=ng_params, headers=ok_headers), None)
        self.assertEqual(crawler.get_html(
            ng_url, params=ng_params, headers=ng_headers), None)


    def test_get_search_url(self):
        # 1) Google で検索ワード「Python」
        crawler1 = Crawler()
        self.assertEqual(len(crawler1.get_search_url("Python")), 10)

        # 2) Google 以外で検索ワード「Python」
        crawler2 = Crawler("yahoo")
        self.assertEqual(crawler2.get_search_url("Python"), None)

        # 3) Google で検索ワード ""
        crawler3 = Crawler("Google")
        self.assertEqual(len(crawler1.get_search_url("")), 0)


if __name__ == '__main__':
    unittest.main()