import requests
from requests.structures import CaseInsensitiveDict

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json, text/plain, */*"
headers["Application-API-Key"] = "8df143c7-fd10-460e-bcc0-d0c1cf947699"
headers["Application-Name"] = "myVisit.com v4.0"
headers["Host"] = "central.qnomy.com"
headers["authorization"] = "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6InljeDFyWFRmalRjQjZIQWV1aGxWQklZZmZUbyJ9.eyJpc3MiOiJodHRwOi8vY2VudHJhbC5xbm9teS5jb20iLCJhdWQiOiJodHRwOi8vY2VudHJhbC5xbm9teS5jb20iLCJuYmYiOjE2NTE0MjMxNjUsImV4cCI6MTY4MjUyNzE2NSwidW5pcXVlX25hbWUiOiI2ZDFlZDI3My1mY2FkLTQ1NDgtYmMwYi1iM2QyMzc2MDRiNDIifQ.lweFODVv3106GrKHl6V18a75W-B50m5uz5-L8xPjBwRe2wGegSgZBzoAXgYK8Pg_ueTak0GipeMNBhjXJWfTVmJf1sZVOvD_UuOiAhHPENSRvExsttRsvlth8AHaOf1Z2pLy7dgu6cqjkjvFfbOezwta40wZ872mMZUM2mAeqzFJC3VTW5jQEkYoSeAEWJXWgD8dF4sZnSBt6_WJ4NgD71CgZCetUwf4Q7SRDZUn_PCs1eTMsvOzNd7OlkaXsbsXzg_wiDeN6fPTWieDNTpm8PJyEuoZ8s3lVekmV9oKa_FIbaNrrupoZP6XnPcws9D0p7ZPY4XZJUQmt2FtEDthaw"


def get_number_of_places(service_id, calendar_id):
    return int(get_places(service_id, calendar_id)['TotalResults'])

def get_places(service_id, calendar_id):
    url = f"https://myvisit.com/CentralAPI/SearchAvailableSlots?CalendarId={calendar_id}&ServiceId={service_id}&dayPart=0"
    try:
        resp = requests.get(url, headers=headers)
        return resp.json()
    except:
        return {
            'TotalResults': 0
        }