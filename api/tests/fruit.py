import pytest
from tests import APITestcase, AssertRequest, AssertResponse

ROUTE = "/fruit"

CASES = [
    APITestcase(
        "success",
        AssertRequest("GET", ROUTE, payload={"name": "apple"}),
        AssertResponse({"name": "apple", "count": 1}, 200),
    ),
    APITestcase(
        "fail",
        AssertRequest("GET", ROUTE, payload={"name": "banana"}),
        AssertResponse("Bad Request", 400),
    ),
    APITestcase(
        "fail",
        AssertRequest("GET", f"{ROUTE}/banana"),
        AssertResponse("Bad Request", 400),
    ),
    APITestcase(
        "success",
        AssertRequest("GET", f"{ROUTE}/apple"),
        AssertResponse({"name": "apple", "count": 1}, 200),
    ),
    APITestcase(
        "success",
        AssertRequest("POST", ROUTE, payload={"name": "banana"}),
        AssertResponse("OK", 200),
    ),
    APITestcase(
        "fail",
        AssertRequest("POST", ROUTE, payload={"name": "apple"}),
        AssertResponse("Bad Request", 400),
    ),
]


@pytest.mark.parametrize("case", CASES, ids=[case.name for case in CASES])
def test(case: APITestcase):
    case.run()
