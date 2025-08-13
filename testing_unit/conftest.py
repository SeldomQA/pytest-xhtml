import pytest
from datetime import datetime, timezone


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
