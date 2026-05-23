import pytest
from datetime import datetime, timezone


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
    }


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

    if hasattr(report, 'nodeid') and '::' in report.nodeid:
        report.description = str(item.function.__doc__ or "No description")

    if report.when == "call" and report.failed:
        page = item.funcargs.get('page')
        if page:
            screenshot_bytes = page.screenshot(full_page=True)
            import base64
            screenshot_base64 = base64.b64encode(screenshot_bytes).decode()

            if not hasattr(report, 'extras'):
                report.extras = []

            report.extras.append({
                'name': 'Screenshot',
                'format_type': 'image',
                'content': screenshot_base64,
                'mime_type': 'image/png',
                'extension': 'png',
            })
