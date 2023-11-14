def test1():
    from urllib.request import urlopen
    from bs4 import BeautifulSoup

    url = "https://www.naver.com"
    html = urlopen(url)
    bs_obj = BeautifulSoup(html.read(), "html.parser")

    # li_list = bs_obj.select("#shortcutArea > ul > li")
    # for item in li_list:
    #     print(item.text)
    print(bs_obj)
test1()

