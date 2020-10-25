import pytest
from tests import APITestcase, AssertRequest, AssertResponse

ROUTE = "/health"

CASES = [
    APITestcase(
        "OK",
        AssertRequest("GET", ROUTE, headers={}, payload={}),
        AssertResponse("OK", 200),
    )
]


@pytest.mark.parametrize("case", CASES, ids=[case.name for case in CASES])
def test(case: APITestcase):
    case.run()
