import pytest
from data import DataAPI
from base_api import Reqs

# ---------------------------------------------------------------------------- #
# >                                   Tests                                    #
# ---------------------------------------------------------------------------- #


class Test_API(Reqs):

    # ---------------------------------------------------------------------------- #
    # TODO         Uncomment - @pytest.mark.skip - to skip test(s)                 #
    # ---------------------------------------------------------------------------- #
    # ---------------------------------------------------------------------------- #
    #                   1 Step - Test 1 - Create Issue Report                      #
    # ---------------------------------------------------------------------------- #
    # @pytest.mark.skip
    def test_01_create_issue(self):
        resp = Reqs.create_issue()
        assert resp[1] == 201, 'Status Code Error'

    # ---------------------------------------------------------------------------- #
    #                  2 Step - Test 1 - Check Issue Status Code                   #
    # ---------------------------------------------------------------------------- #
    def test_02__1_check_status_issue(self):
        resp = Reqs.get_issue(Reqs.url_get_issue())
        assert resp.status_code == 200, 'Status Code Error'

    # ---------------------------------------------------------------------------- #
    #                     2 Step - Test 2 - Check Time Response                    #
    # ---------------------------------------------------------------------------- #
    def test_02_2_check_time_responce(self):
        resp = Reqs.get_issue(Reqs.url_get_issue())
        exp_time_req = 3000  # > expect less than 3000 ms
        time_resp = round(resp.elapsed.microseconds / 1000)
        print(f"\nTime: {time_resp} ms")
        assert time_resp < exp_time_req, 'Time response less than 3000 ms'

    # ---------------------------------------------------------------------------- #
    #                2 Step - Test 3 - Check Date in Title response                #
    # ---------------------------------------------------------------------------- #
    def test_02_3_check_headers_date(self):

        resp = Reqs.get_issue(Reqs.url_get_issue())
        date_resp = resp.headers['Date']  # > get Date from Title
        print(f"\nDate: {date_resp}")
        assert date_resp != None, 'Tite does not have date'

    # ---------------------------------------------------------------------------- #
    #                     2 Step - Test 4 - Check Type of Issue                    #
    # ---------------------------------------------------------------------------- #
    def test_02_4_check_issue_type(self):
        response = Reqs.get_issue(Reqs.url_get_issue())
        resp = response.json()
        issue_type = resp['fields']['issuetype']['name']  # > get Issue Type
        exp_issue_type = "Баг"
        print(f"\nIssue Type: {issue_type}")
        assert issue_type == exp_issue_type, 'Type does not match'

    # ---------------------------------------------------------------------------- #
    #                      3 Step - Test 1 - Get current user                      #
    # ---------------------------------------------------------------------------- #
    def test_03_1_get_current_user(self):
        response = Reqs.get_issue(DataAPI.URL_USER)
        resp = response.json()
        current_user = resp['displayName']  # > get the user name
        exp_current_user = "Be Tester"
        print(f"\nCurrent user: {current_user}")
        assert current_user == exp_current_user, 'Current user does not match'

    # ---------------------------------------------------------------------------- #
    #                        3 Step - Test 2 - Assign Issue                        #
    # ---------------------------------------------------------------------------- #
    def test_03_2_set_user(self):
        Reqs.set_user()
        response = Reqs.get_issue(Reqs.url_get_issue())
        resp = response.json()
        assigned_user_name = resp['fields']['assignee']['displayName']
        exp_assigned_user_name = "Be Tester"
        print(f"\nAssigned user: {assigned_user_name}")
        assert assigned_user_name == exp_assigned_user_name, 'Assigned user does not matchh'

    # ---------------------------------------------------------------------------- #
    #                        4 Step - Test 1 - Delete Issue                        #
    # ---------------------------------------------------------------------------- #
    # @pytest.mark.skip
    def test_04_delete_issue(self):
        resp_del = Reqs.delete_issue()
        assert resp_del == 204, 'Status Code Error'
