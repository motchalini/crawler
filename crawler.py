from logging import basicConfig, getLogger, DEBUG

from scraper import Scraper


# ログフォーマットを定義
formatter = "[%(asctime)s][%(name)s][%(levelname)s]%(message)s"
# ログレベル
basicConfig(level=DEBUG, format=formatter)


class Crawler:
    """ Crawler
    self.user_agent : ユーザーエージェントの情報を設定
    self.engine : 検索サイトを設定

    get_search_url(word, engine="google") : 検索サイトで検索結果の一覧を取得
        word: 検索するワード
        [engine]: 使用する検索サイト（デフォルトは google）
    """

    def __init__(self, engine="google"):
        # User-Agent
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                           AppleWebKit/537.36 (KHTML, like Gecko) \
                           Chrome/69.0.3497.100"
        # engine
        self.engine = engine

    def get_search_url(self, word):
        """ get_search_url
        word: 検索するワード
        [engine]: 使用する検索サイト（デフォルトは google）
        """
        logger = getLogger("get_search_url()")
        try:
            if self.engine == "google":
                # google 検索
                search_url = "https://www.google.co.jp/search"
                search_params = {"q": word}
                search_headers = {"User-Agent": self.user_agent}
                # データ取得
                soup = Scraper.get_html(search_url, search_params, search_headers)
                if soup != None:
                    tags = soup.select(".r > a")
                    urls = [tag.get("href") for tag in tags]
                    return urls
                else:
                    raise Exception("No Data")
            else:
                raise Exception("No Engine")
        except Exception as e:
            logger.warning(e)
            return None


if __name__ == '__main__':
    try:
        # インスタンス化
        crawler = Crawler()
        urls = crawler.get_search_url("python")
        if urls != None:
            for url in urls:
                if Scraper.get_robots_txt(url):
                    soup = Scraper.get_html(url)
                    print(soup.title.get_text())
                else:
                    print("クロールが拒否されました [{}]".format(url))
        else:
            print("取得できませんでした")
    except Exception as e:
        print("エラーになりました")
