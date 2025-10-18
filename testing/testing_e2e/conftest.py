import pytest
from datetime import datetime, timezone
from selenium import webdriver


@pytest.fixture
def driver():
    """提供 WebDriver 实例用于测试"""
    driver = webdriver.Edge()
    yield driver
    driver.quit()


def pytest_xhtml_results_table_header(cells):
    cells.insert(2, "<th>Description</th>")
    cells.insert(1, '<th class="sortable time" data-column-type="time">Time</th>')


def pytest_xhtml_results_table_row(report, cells):
    cells.insert(2, f"<td>{report.description}</td>")
    cells.insert(1, f'<td class="col-time">{datetime.now(timezone.utc)}</td>')


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    # 只为测试用例添加描述，不处理收集阶段的报告
    if hasattr(report, 'nodeid') and '::' in report.nodeid:
        report.description = str(item.function.__doc__ or "No description")
    
    # 当测试失败时添加截图
    if report.when == "call" and report.failed:
        # 获取当前测试的 driver fixture
        driver = item.funcargs.get('driver')
        if driver:
            # 使用 base64 编码获取截图
            screenshot_base64 = driver.get_screenshot_as_base64()
            
            # 将截图添加到报告额外信息中 - 使用 pytest-xhtml 期望的格式
            if not hasattr(report, 'extras'):
                report.extras = []
            
            # 使用 pytest-xhtml 支持的格式
            report.extras.append({
                'name': 'Screenshot',
                'format_type': 'image',  # 必需字段
                'content': screenshot_base64,  # base64 内容
                'mime_type': 'image/png',  # 必需字段
                'extension': 'png'  # 必需字段
            })
