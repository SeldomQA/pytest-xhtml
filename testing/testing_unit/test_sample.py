import pytest

# 简单的测试用例
def test_pass():
    assert 1 + 1 == 2

def test_fail():
    assert 1 + 1 == 3

def test_skip():
    pytest.skip("这个测试被跳过")

@pytest.mark.xfail
def test_xfail():
    assert 1 + 1 == 3

@pytest.mark.xfail(reason="预期失败，但实际会通过")
def test_xpass():
    """这是一个 Unexpected passes 用例 - 预期失败但实际通过"""
    assert 1 + 1 == 2

def test_error():
    """这是一个 Error 用例 - 测试执行时发生异常"""
    # 故意引发一个异常来模拟错误
    raise ValueError("模拟测试执行错误")

@pytest.fixture
def error_fixture():
    # 在fixture中引发异常，也会导致测试错误
    raise RuntimeError("fixture中的错误")

def test_error_with_fixture(error_fixture):
    """使用会出错的fixture的测试用例"""
    assert True

if __name__ == '__main__':
    pytest.main(["-v", "--html=report.html", "test_sample.py"])