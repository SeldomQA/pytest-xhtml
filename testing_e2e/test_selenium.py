# write a test that sorts the table and asserts the order.
# sort default columns and custom sortable column
from time import sleep
from selenium.webdriver.common.by import By

def test_bing_index(driver):
    """测试 Bing 搜索功能"""
    # 访问 Bing 搜索页面
    driver.get("https://www.bing.com")


def test_baidu_index(driver):
    """测试 Bing 搜索功能"""
    # 访问 Bing 搜索页面
    driver.get("https://www.baidu.com")


def test_bing_search_fail(driver):
    """测试 Bing 搜索功能"""
    # 访问 Bing 搜索页面
    driver.get("https://www.bing.com")
    sleep(10)
    assert driver.title == "pytest-xhtml - 搜索11"


def test_baidu_search_error(driver):
    """测试 Baidu 搜索功能"""
    # 访问 Bing 搜索页面
    driver.get("https://www.baidu.com")
    driver.find_element(By.ID, "kw11").send_keys("pytest-xhtml")
