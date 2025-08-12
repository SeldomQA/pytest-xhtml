# write a test that sorts the table and asserts the order.
# sort default columns and custom sortable column
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

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
    
    # 等待搜索框加载完成
    wait = WebDriverWait(driver, 10)
    search_box = wait.until(
        ec.presence_of_element_located((By.NAME, "q"))
    )
    
    # 输入搜索关键词
    search_term = "pytest-xhtml"
    search_box.send_keys(search_term)
    
    # 提交搜索
    search_box.submit()
    
    # 等待搜索结果页面加载
    wait.until(
        ec.title_contains(search_term)
    )
        
    assert driver.title == "pytest-xhtml - 搜索11"


def test_baidu_search_error(driver):
    """测试 Baidu 搜索功能"""
    # 访问 Bing 搜索页面
    driver.get("https://www.baidu.com")
    driver.find_element(By.ID, "kw").send_keys("pytest-xhtml")
    driver.find_element(By.ID, "su11").click()
