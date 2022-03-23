import pytest
import requests
import json

urlPost = "https://betesterapi.atlassian.net/rest/api/3/issue"
urlUser = "https://betesterapi.atlassian.net/rest/api/3/myself"
headersList = {
    "Authorization": "Basic YmV0ZXN0ZXJqaXJhMDFAeWFuZGV4LnJ1OjBQbVpKbjVlS3Nhd3NvZHAwRllRODdEMg==",
}
json_post = {
    "fields": {
        "project": {
            "key": "TAB"
        },
        "summary": "Create_issue_MX_HM",
        "description": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "Steps -->"
                        }
                    ]
                }
            ]
        },
        "issuetype": {
            "name": "Bug"
        }
    }
}
json_put = {"accountId": "602d11684890ef0071f6d5b0"}


def key_tab():

    def response():
        response = requests.get(urlGet, headers=headersList)
        return response

    try:
        print(pytest.key)
        key = pytest.key
    except AttributeError:
        urlGet = f"https://betesterapi.atlassian.net//rest/api/2/search?jql=project%20%3D%20TAB%20AND%20text%20~%20%22MX_HM%22"
        print("\nno new key")
        response()
        resp = response().json()

        try:
            print(f"key: {(resp['issues'][0]['key'])}")
            key = resp['issues'][0]['key']
        except IndexError:
            print("There is no issue at this moment and therefore no key")
            key = None
            return key
    return key


def temlpate_get():
    key = key_tab()
    if key is not None:
        urlGet = f"https://betesterapi.atlassian.net/rest/agile/1.0/issue/{key}"
        response = requests.get(urlGet, headers=headersList)
    else:
        response = None
    return response


def temlpate_delete():
    key = key_tab()
    if key is not None:
        urlDel = f"https://betesterapi.atlassian.net/rest/api/3/issue/{key}"
        response = requests.delete(urlDel, headers=headersList)
    else:
        response = None
    return response


def temlpate_set_user():
    key = key_tab()
    if key is not None:
        urlSet = f"https://betesterapi.atlassian.net/rest/api/3/issue/{key}/assignee"
        response = requests.put(
            urlSet, headers=headersList, json=json_put)
        urlGet = f"https://betesterapi.atlassian.net/rest/agile/1.0/issue/{key}"
        response = requests.get(urlGet, headers=headersList)
    else:
        response = None
    return response


# @pytest.mark.skip
def test_01_create_issue():
    pytest.post_req = requests.post(
        urlPost, headers=headersList, json=json_post)
    pytest.key = pytest.post_req.json()['key']
    code = pytest.post_req.status_code
    assert code == 201, 'Code error'
    print(f"\nStatus code: {code}")


# @pytest.mark.skip
def test_02_1_status_code200():
    response = temlpate_get()
    if response != None:
        exp_code = 200
        code = response.status_code
        assert code == exp_code, 'Code error'
        print(f"\nStatus code: {code}")


# @pytest.mark.skip
def test_02_2_time():
    response = temlpate_get()
    if response != None:
        exp_time_req = 3000
        time_resp = round(response.elapsed.microseconds / 1000)
        assert time_resp < exp_time_req, 'Time response less than 3000 ms'
        print(f"\nTime: {time_resp} ms")


# @pytest.mark.skip
def test_02_3_date():
    response = temlpate_get()
    if response != None:
        date_resp = response.headers['Date']
        assert date_resp != None, 'Tite does not have date'
        print(f"\nDate: {date_resp}")


# @pytest.mark.skip
def test_02_4_issue_type():
    response = temlpate_get()
    if response != None:
        resp = response.json()
        issue_type = resp['fields']['issuetype']['name']
        exp_issue_type = "Баг"
        assert issue_type == exp_issue_type, 'Type does not match'
        print(f"\nIssue Type: {issue_type}")


# @pytest.mark.skip
def test_03_1_get_current_user():

    response = requests.get(urlUser, headers=headersList)
    resp = response.json()
    current_user = resp['displayName']
    exp_current_user = "Be Tester"
    assert current_user == exp_current_user, 'Current user does not match'
    print(f"\nCurrent user: {current_user}")


# @pytest.mark.skip
def test_03_2_set_user():
    response = temlpate_set_user()
    if response != None:
        resp = response.json()
        assigned_user_name = resp['fields']['assignee']['displayName']
        exp_assigned_user_name = "Be Tester"
        assert assigned_user_name == exp_assigned_user_name, 'Assigned user does not matchh'
        print(f"\nAssigned user: {assigned_user_name}")


# @pytest.mark.skip
def test_04_delete_issue():
    response = temlpate_delete()
    if response != None:
        code = response.status_code
        assert code == 204, 'Code error'
        print(f"\nStatus code: {code}")
