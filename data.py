

class DataAPI():

    # >----------------- url for creating Issue with POST method ----------------- #
    URL_POST = "https://betesterapi.atlassian.net/rest/api/3/issue"
    # >---------------------- url for getting current user ----------------------- #
    URL_USER = "https://betesterapi.atlassian.net/rest/api/3/myself"
    # >--------------------- auth data for requests --------------------------- #
    EMAIL = "betesterjira01@yandex.ru"
    PASSWORD = "wDmTIm1kbxAR5jEoVtib57CC"
    AUTH_JIRA = (EMAIL, PASSWORD)
    # >---------------- json data to assign issue with PUT method ---------------- #
    JSON_PUT = {"accountId": "602d11684890ef0071f6d5b0"}
    # >------------------- data to create or find Issue Report ------------------- #
    SUMMARY_ISSUE = "Create_issue_MX_HM"
    URL_GET = f"https://betesterapi.atlassian.net//rest/api/2/search?jql=project%20%3D%20TAB%20AND%20text%20~%20%22{SUMMARY_ISSUE}%22"
    JSON_CREATE = {
        "fields": {
            "project": {
                "key": "TAB"
            },
            "summary": SUMMARY_ISSUE,
            "description": {
                "type": "doc",
                "version": 1,
                "content": [{
                    "type": "paragraph",
                    "content": [{
                        "type": "text",
                        "text": "Steps -->"
                    }]
                }]
            },
            "issuetype": {
                "name": "Bug"
            }
        }
    }
