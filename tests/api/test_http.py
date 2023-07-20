import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get("https://api.github.com/zen")
    print(f"Response is {r.text}")


@pytest.mark.http
def test_second_request():
    r = requests.get("https://api.github.com/users/defunkt")
    # print(f"Response Body is{r.json()}")
    body = r.json()
    headers = r.headers
    assert body["name"] == "Chris Wanstrath"  # Check name
    assert r.status_code == 200
    assert headers["Server"] == "GitHub.com"  # Check header {Server}


@pytest.mark.http
def test_status_code_request():
    r = requests.get("https://api.github.com/users/sergii_butenko")
    assert r.status_code == 404
