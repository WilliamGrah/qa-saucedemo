import pytest
from tests.playwright.pages.login_page import LoginPage


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


@pytest.fixture(autouse=True)
def screenshot_on_failure(request, page):
    yield
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        marker = request.node.get_closest_marker("testcase")
        name = marker.args[0] if marker else request.node.name
        page.screenshot(path=f"test-results/{name}.png")
