
class Crawler:
    """
    Web crawler
    """
    # User-Agent
    headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A366 Safari/600.1.4"}
    
    def __init__(self, engine="google", headers=headers):
        self.engine = engine
        self.headers = headers



if __name__ == '__main__':
    crawler = Crawler()
    print(crawler.headers)