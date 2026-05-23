def test_baidu_homepage(page):
    page.goto("https://www.baidu.com")
    assert page.title() is not None


def test_bing_homepage(page):
    page.goto("https://www.bing.com")
    assert page.title() is not None


def test_bing_search_fail(page):
    page.goto("https://www.bing.com")
    page.wait_for_timeout(3000)
    assert page.title() == "pytest-xhtml - search"


def test_baidu_search_error(page):
    page.goto("https://www.baidu.com")
    page.locator("#kw11").fill("pytest-xhtml")
