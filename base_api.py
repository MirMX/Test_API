import pytest
import requests

from data import DataAPI


class Reqs:

    def key_tab():

        def response():
            response = requests.get(DataAPI.URL_GET, auth=DataAPI.AUTH_JIRA)
            return response
        # > try if there is new issue created to get the key
        # > otherwise get the key from the last created issue with name: summary_issue
        try:
            key = pytest.key
        except Exception:
            print("\n\nno new key")
            response()
            resp = response().json()
            # > try if there is issue with the name: summary_issue to get the key
            # > othewise print a message (...no key)
            try:
                print(f"key: {(resp['issues'][0]['key'])}")
                key = resp['issues'][0]['key']
            except Exception:
                print("There is no Issue Report and therefore no key")
                key = None
                return key
        return key
# >--------------------------------------------------------------------------- #

    def create_issue():
        post_req = requests.post(
            DataAPI.URL_POST, auth=DataAPI.AUTH_JIRA, json=DataAPI.JSON_CREATE)
        code = post_req.status_code
        print(f"Status code: {code}")
        pytest.key = post_req.json()['key']    # > get the key issue (TAB-#)
        return pytest.key, code
# ---------------------------------------------------------------------------- #
    def url_get_issue():
        key = Reqs.key_tab()
        urlGet = f"https://betesterapi.atlassian.net/rest/agile/1.0/issue/{key}"
        return urlGet

    def get_issue(urlGet):
        resp = requests.get(urlGet, auth=DataAPI.AUTH_JIRA)
        code = resp.status_code
        print(f"Status code: {code}")
        return resp
# ---------------------------------------------------------------------------- #
    def url_set_user():
        key = Reqs.key_tab()
        urlSet = f"https://betesterapi.atlassian.net/rest/api/3/issue/{key}/assignee"
        return urlSet

    def set_user():
        response = requests.put(
            Reqs.url_set_user(), auth=DataAPI.AUTH_JIRA, json=DataAPI.JSON_PUT)
        resp = response.status_code
        print(f"\nSet User - Status code: {resp}")
# ---------------------------------------------------------------------------- #
    def url_delete():
        key = Reqs.key_tab()
        urlDel = f"https://betesterapi.atlassian.net/rest/api/3/issue/{key}"
        return urlDel
    
    def delete_issue():
        response = requests.delete(Reqs.url_delete(), auth=DataAPI.AUTH_JIRA)
        resp = response.status_code
        print(f"\nDelete Issue - Status code: {resp}")
        return resp
