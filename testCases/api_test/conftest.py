from testCases.conftest import api_test_data
import pytest


@pytest.fixture(scope="function")
def testcase_data(request):
    case_name = request.function.__name__
    return api_test_data.get(case_name)