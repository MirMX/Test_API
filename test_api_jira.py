import pytest
import requests

# >----------------- url for creating Issue with POST method ----------------- #
urlPost = "https://betesterapi.atlassian.net/rest/api/3/issue"
# >---------------------- url for getting current user ----------------------- #
urlUser = "https://betesterapi.atlassian.net/rest/api/3/myself"
# >--------------------- headers data for requests --------------------------- #
headersList = {
    "Authorization": "Basic YmV0ZXN0ZXJqaXJhMDFAeWFuZGV4LnJ1OjBQbVpKbjVlS3Nhd3NvZHAwRllRODdEMg==",
}
# >------------ json data for creating Issue with POST method ------------- #
summary_issue = "Create_issue_MX_HM"
json_post = {
    "fields": {
        "project": {
            "key": "TAB"
        },
        "summary": summary_issue,
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
# >---------------- json data to assign issue with PUT method ---------------- #
json_put = {"accountId": "602d11684890ef0071f6d5b0"}


# >------------------------- Get Issue Key {TAB-...} ------------------------- #
def key_tab():

    def response():
        response = requests.get(urlGet, headers=headersList)
        return response
    # > try if there is new issue created to get the key
    # > otherwise get the key from the last created issue with name: summary_issue
    try:
        print(pytest.key)
        key = pytest.key
    except AttributeError:
        urlGet = f"https://betesterapi.atlassian.net//rest/api/2/search?jql=project%20%3D%20TAB%20AND%20text%20~%20%22{summary_issue}%22"
        print("\nno new key")
        response()
        resp = response().json()
        # > try if there is issue with the name: summary_issue to get the key
        # > othewise print a message (...no key)
        try:
            print(f"key: {(resp['issues'][0]['key'])}")
            key = resp['issues'][0]['key']
        except IndexError:
            print("There is no issue at this moment and therefore no key")
            key = None
            return key
    return key


# ---------------------------------------------------------------------------- #
# >                 Templates for different requests methods                   #
# ---------------------------------------------------------------------------- #
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


# ---------------------------------------------------------------------------- #
# >                                   Tests                                    #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
# TODO         Uncomment - @pytest.mark.skip - to skip test(s)                 #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
#                   1 Step - Test 1 - Create Issue Report                      #
# ---------------------------------------------------------------------------- #
# @pytest.mark.skip
def test_01_create_issue():
    pytest.post_req = requests.post(
        urlPost, headers=headersList, json=json_post)
    pytest.key = pytest.post_req.json()['key']    # > get the key issue (TAB-#)
    code = pytest.post_req.status_code
    assert code == 201, 'Status Code Error'
    print(f"\nStatus code: {code}")


# ---------------------------------------------------------------------------- #
#                  2 Step - Test 1 - Check Issue Status Code                   #
# ---------------------------------------------------------------------------- #
# @pytest.mark.skip
def test_02_1_status_code200():
    response = temlpate_get()
    if response != None:
        exp_code = 200  # > expect code 200
        code = response.status_code
        assert code == exp_code, 'Status Code Error'
        print(f"\nStatus code: {code}")


# ---------------------------------------------------------------------------- #
#                     2 Step - Test 2 - Check Time Response                    #
# ---------------------------------------------------------------------------- #
# @pytest.mark.skip
def test_02_2_time():
    response = temlpate_get()
    if response != None:
        exp_time_req = 3000  # > expect less than 3000 ms
        time_resp = round(response.elapsed.microseconds / 1000)
        assert time_resp < exp_time_req, 'Time response less than 3000 ms'
        print(f"\nTime: {time_resp} ms")


# ---------------------------------------------------------------------------- #
#                2 Step - Test 3 - Check Date in Title response                #
# ---------------------------------------------------------------------------- #
# @pytest.mark.skip
def test_02_3_date():
    response = temlpate_get()
    if response != None:
        date_resp = response.headers['Date']  # > get Date from Title
        assert date_resp != None, 'Tite does not have date'
        print(f"\nDate: {date_resp}")


# ---------------------------------------------------------------------------- #
#                     2 Step - Test 4 - Check Type of Issue                    #
# ---------------------------------------------------------------------------- #
# @pytest.mark.skip
def test_02_4_issue_type():
    response = temlpate_get()
    if response != None:
        resp = response.json()
        issue_type = resp['fields']['issuetype']['name']  # > get Issue Type
        exp_issue_type = "Баг"
        assert issue_type == exp_issue_type, 'Type does not match'
        print(f"\nIssue Type: {issue_type}")


# ---------------------------------------------------------------------------- #
#                      3 Step - Test 1 - Get current user                      #
# ---------------------------------------------------------------------------- #
# @pytest.mark.skip
def test_03_1_get_current_user():

    response = requests.get(urlUser, headers=headersList)
    resp = response.json()
    current_user = resp['displayName']  # > get the user name
    exp_current_user = "Be Tester"
    assert current_user == exp_current_user, 'Current user does not match'
    print(f"\nCurrent user: {current_user}")


# ---------------------------------------------------------------------------- #
#                        3 Step - Test 2 - Assign Issue                        #
# ---------------------------------------------------------------------------- #
# @pytest.mark.skip
def test_03_2_set_user():
    response = temlpate_set_user()
    if response != None:
        # > check if the Issue assigned
        resp = response.json()
        assigned_user_name = resp['fields']['assignee']['displayName']
        exp_assigned_user_name = "Be Tester"
        assert assigned_user_name == exp_assigned_user_name, 'Assigned user does not matchh'
        print(f"\nAssigned user: {assigned_user_name}")


# ---------------------------------------------------------------------------- #
#                        4 Step - Test 1 - Delete Issue                        #
# ---------------------------------------------------------------------------- #
# @pytest.mark.skip
def test_04_delete_issue():
    response = temlpate_delete()
    if response != None:
        code = response.status_code
        assert code == 204, 'Status Code Error'
        print(f"\nStatus code: {code}")
