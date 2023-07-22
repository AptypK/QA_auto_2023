import pytest
import datetime
from datetime import datetime


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")
    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_non_exists(github_api):
    r = github_api.get_user("butenkosergii")
    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")
    #    print(r)
    assert r["total_count"] == 42
    # assert "become-qa-auto" in r["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("segiibutenko_repo_non_exist")
    assert r["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo("s")
    assert r["total_count"] != 0


# Personal API-test tasks - Project task #4
# Test#1.
# This test check, if there is a Ukrainian flag on the GitHub emoji list
@pytest.mark.api
def test_emoji_exists(github_api):
    emoji = github_api.get_emojis()
    # print(emoji)
    assert "ukraine" in emoji


# Test#2.
# This test check, have Commit descripion or not
@pytest.mark.api
def test_commit_message_not_empty(github_api):
    r = github_api.get_commit(
        "SergiiButenko", "furry-waddle", "2960793eb68a2b9c103d3dfc7e1c35f29ad4e95a"
    )
    # print(r["commit"])
    # print(r["commit"]["message"])
    assert r["commit"]["message"] != ""


# Test#3.
# This test check, Author of Commit
@pytest.mark.api
def test_check_commit_author(github_api):
    r = github_api.get_commit(
        "SergiiButenko", "furry-waddle", "2960793eb68a2b9c103d3dfc7e1c35f29ad4e95a"
    )
    assert r["commit"]["author"]["name"] == "Sergii Butenko"


# Test#4.
# This test checks if the commit is new or old. Is he more than a week old (7 days)
@pytest.mark.api
def test_check_commit_more_1weak(github_api):
    r = github_api.get_commit(
        "SergiiButenko", "furry-waddle", "2960793eb68a2b9c103d3dfc7e1c35f29ad4e95a"
    )
    date_today = datetime.today().date()
    date_commit = r["commit"]["author"]["date"]
    date_commit = datetime.strptime(date_commit[:10], "%Y-%m-%d").date()
    # On date 22.07.2023 198 days have passed since the commit date
    assert (date_today - date_commit).days > 7
