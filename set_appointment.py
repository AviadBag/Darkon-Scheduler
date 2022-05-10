import requests
import logging

# Returns [visit_token, visit_id]
def setup_visit():
    cookies = {
    'ARRAffinitySameSite': '09e4dbcfb7d151ae26749cddf13422c292961bb7c3da19ef05434b6587763168',
    }

    headers = {
        'Host': 'central.qnomy.com',
        # 'Content-Length': '4',
        'Sec-Ch-Ua': '"(Not(A:Brand";v="8", "Chromium";v="101"',
        'Application-Api-Key': '8df143c7-fd10-460e-bcc0-d0c1cf947699',
        'Accept-Language': 'he',
        'Sec-Ch-Ua-Mobile': '?0',
        'Authorization': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6InljeDFyWFRmalRjQjZIQWV1aGxWQklZZmZUbyJ9.eyJpc3MiOiJodHRwOi8vY2VudHJhbC5xbm9teS5jb20iLCJhdWQiOiJodHRwOi8vY2VudHJhbC5xbm9teS5jb20iLCJuYmYiOjE2NTE4MzIzMjAsImV4cCI6MTY4MjkzNjMyMCwidW5pcXVlX25hbWUiOiI2ZDFlZDI3My1mY2FkLTQ1NDgtYmMwYi1iM2QyMzc2MDRiNDIifQ.TYbS8tx0-lT7BMm44tEYm2vsi9JZZ6STgdg0_KLG3VdLtZPmqejO-jnRV6A74nImIrNVarep9rbzWvDhSO7UNbqHnv_Zkz3FSFgvW63IX1qQsFDdZXWe4El-Juxq__ze9X8de6-xmz5pJTVa_S8uSniielHRd8lsLNmQlKOXCwvlPJF1ICi69aK2nkjXmpTclBDnQSFJtMwOmAFQMzT7_kfRPNRAqwPyExcdIDUybfQueRi9QMfWuskLHEG42D5ZQwvgxRtxlWRils_mggTckB5ShDEX-oXAt1nqqvf6WBz45NRl4WQJdgPEAGIRIHh7QgRk96deSAwUrpn3T4FAMg',
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
        'Application-Name': 'myVisit.com v4.0',
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://myvisit.com',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://myvisit.com/',
        # 'Accept-Encoding': 'gzip, deflate',
        'Connection': 'close',
        # 'Cookie': 'ARRAffinitySameSite=09e4dbcfb7d151ae26749cddf13422c292961bb7c3da19ef05434b6587763168',
    }

    response = requests.post('https://central.qnomy.com/CentralAPI/Service/2247/PrepareVisit', cookies=cookies, headers=headers, verify=False)
    json_data = response.json()
    
    logging.info(f'Generated visit token: {json_data["Data"]["PreparedVisitToken"]}')

    return [json_data["Data"]["PreparedVisitToken"], json_data["Data"]["PreparedVisitId"]]

def send_id(id, token):
    cookies = {
    'ARRAffinitySameSite': '09e4dbcfb7d151ae26749cddf13422c292961bb7c3da19ef05434b6587763168',
    }

    headers = {
        'Host': 'central.qnomy.com',
        # 'Content-Length': '146',
        'Sec-Ch-Ua': '"(Not(A:Brand";v="8", "Chromium";v="101"',
        'Application-Api-Key': '8df143c7-fd10-460e-bcc0-d0c1cf947699',
        'Accept-Language': 'he',
        'Sec-Ch-Ua-Mobile': '?0',
        'Authorization': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6InljeDFyWFRmalRjQjZIQWV1aGxWQklZZmZUbyJ9.eyJpc3MiOiJodHRwOi8vY2VudHJhbC5xbm9teS5jb20iLCJhdWQiOiJodHRwOi8vY2VudHJhbC5xbm9teS5jb20iLCJuYmYiOjE2NTE4MzIzMjAsImV4cCI6MTY4MjkzNjMyMCwidW5pcXVlX25hbWUiOiI2ZDFlZDI3My1mY2FkLTQ1NDgtYmMwYi1iM2QyMzc2MDRiNDIifQ.TYbS8tx0-lT7BMm44tEYm2vsi9JZZ6STgdg0_KLG3VdLtZPmqejO-jnRV6A74nImIrNVarep9rbzWvDhSO7UNbqHnv_Zkz3FSFgvW63IX1qQsFDdZXWe4El-Juxq__ze9X8de6-xmz5pJTVa_S8uSniielHRd8lsLNmQlKOXCwvlPJF1ICi69aK2nkjXmpTclBDnQSFJtMwOmAFQMzT7_kfRPNRAqwPyExcdIDUybfQueRi9QMfWuskLHEG42D5ZQwvgxRtxlWRils_mggTckB5ShDEX-oXAt1nqqvf6WBz45NRl4WQJdgPEAGIRIHh7QgRk96deSAwUrpn3T4FAMg',
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
        'Application-Name': 'myVisit.com v4.0',
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://myvisit.com',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://myvisit.com/',
        # 'Accept-Encoding': 'gzip, deflate',
        'Connection': 'close',
        # 'Cookie': 'ARRAffinitySameSite=09e4dbcfb7d151ae26749cddf13422c292961bb7c3da19ef05434b6587763168',
    }

    json_data = {
        'PreparedVisitToken': token,
        'QuestionnaireItemId': 199,
        'QuestionId': 113,
        'AnswerIds': None,
        'AnswerText': id,
    }

    logging.info(f'Sending ID {id}')
    return requests.post(f'https://central.qnomy.com/CentralAPI/PreparedVisit/{token}/Answer', cookies=cookies, headers=headers, json=json_data, verify=False).json()

def send_phone(phone, token):
    cookies = {
        'ARRAffinitySameSite': '09e4dbcfb7d151ae26749cddf13422c292961bb7c3da19ef05434b6587763168',
    }

    headers = {
        'Host': 'central.qnomy.com',
        # 'Content-Length': '147',
        'Sec-Ch-Ua': '"(Not(A:Brand";v="8", "Chromium";v="101"',
        'Application-Api-Key': '8df143c7-fd10-460e-bcc0-d0c1cf947699',
        'Accept-Language': 'he',
        'Sec-Ch-Ua-Mobile': '?0',
        'Authorization': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6InljeDFyWFRmalRjQjZIQWV1aGxWQklZZmZUbyJ9.eyJpc3MiOiJodHRwOi8vY2VudHJhbC5xbm9teS5jb20iLCJhdWQiOiJodHRwOi8vY2VudHJhbC5xbm9teS5jb20iLCJuYmYiOjE2NTE4MzIzMjAsImV4cCI6MTY4MjkzNjMyMCwidW5pcXVlX25hbWUiOiI2ZDFlZDI3My1mY2FkLTQ1NDgtYmMwYi1iM2QyMzc2MDRiNDIifQ.TYbS8tx0-lT7BMm44tEYm2vsi9JZZ6STgdg0_KLG3VdLtZPmqejO-jnRV6A74nImIrNVarep9rbzWvDhSO7UNbqHnv_Zkz3FSFgvW63IX1qQsFDdZXWe4El-Juxq__ze9X8de6-xmz5pJTVa_S8uSniielHRd8lsLNmQlKOXCwvlPJF1ICi69aK2nkjXmpTclBDnQSFJtMwOmAFQMzT7_kfRPNRAqwPyExcdIDUybfQueRi9QMfWuskLHEG42D5ZQwvgxRtxlWRils_mggTckB5ShDEX-oXAt1nqqvf6WBz45NRl4WQJdgPEAGIRIHh7QgRk96deSAwUrpn3T4FAMg',
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
        'Application-Name': 'myVisit.com v4.0',
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://myvisit.com',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://myvisit.com/',
        # 'Accept-Encoding': 'gzip, deflate',
        'Connection': 'close',
        # 'Cookie': 'ARRAffinitySameSite=09e4dbcfb7d151ae26749cddf13422c292961bb7c3da19ef05434b6587763168',
    }

    json_data = {
        'PreparedVisitToken': token,
        'QuestionnaireItemId': 200,
        'QuestionId': 114,
        'AnswerIds': None,
        'AnswerText': phone,
    }

    logging.info(f'Sending phone {phone}')
    return requests.post(f'https://central.qnomy.com/CentralAPI/PreparedVisit/{token}/Answer', cookies=cookies, headers=headers, json=json_data, verify=False).json()

def set_visit_type(token):
    cookies = {
        'ARRAffinitySameSite': '09e4dbcfb7d151ae26749cddf13422c292961bb7c3da19ef05434b6587763168',
    }

    headers = {
        'Host': 'central.qnomy.com',
        # 'Content-Length': '139',
        'Sec-Ch-Ua': '"(Not(A:Brand";v="8", "Chromium";v="101"',
        'Application-Api-Key': '8df143c7-fd10-460e-bcc0-d0c1cf947699',
        'Accept-Language': 'he',
        'Sec-Ch-Ua-Mobile': '?0',
        'Authorization': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6InljeDFyWFRmalRjQjZIQWV1aGxWQklZZmZUbyJ9.eyJpc3MiOiJodHRwOi8vY2VudHJhbC5xbm9teS5jb20iLCJhdWQiOiJodHRwOi8vY2VudHJhbC5xbm9teS5jb20iLCJuYmYiOjE2NTE4MzIzMjAsImV4cCI6MTY4MjkzNjMyMCwidW5pcXVlX25hbWUiOiI2ZDFlZDI3My1mY2FkLTQ1NDgtYmMwYi1iM2QyMzc2MDRiNDIifQ.TYbS8tx0-lT7BMm44tEYm2vsi9JZZ6STgdg0_KLG3VdLtZPmqejO-jnRV6A74nImIrNVarep9rbzWvDhSO7UNbqHnv_Zkz3FSFgvW63IX1qQsFDdZXWe4El-Juxq__ze9X8de6-xmz5pJTVa_S8uSniielHRd8lsLNmQlKOXCwvlPJF1ICi69aK2nkjXmpTclBDnQSFJtMwOmAFQMzT7_kfRPNRAqwPyExcdIDUybfQueRi9QMfWuskLHEG42D5ZQwvgxRtxlWRils_mggTckB5ShDEX-oXAt1nqqvf6WBz45NRl4WQJdgPEAGIRIHh7QgRk96deSAwUrpn3T4FAMg',
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
        'Application-Name': 'myVisit.com v4.0',
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://myvisit.com',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://myvisit.com/',
        # 'Accept-Encoding': 'gzip, deflate',
        'Connection': 'close',
        # 'Cookie': 'ARRAffinitySameSite=09e4dbcfb7d151ae26749cddf13422c292961bb7c3da19ef05434b6587763168',
    }

    json_data = {
        'PreparedVisitToken': token,
        'QuestionnaireItemId': 201,
        'QuestionId': 116,
        'AnswerIds': [
            76,
        ],
        'AnswerText': None,
    }

    logging.info('Setting visit type')
    return requests.post(f'https://central.qnomy.com/CentralAPI/PreparedVisit/{token}/Answer', cookies=cookies, headers=headers, json=json_data, verify=False).json()

def _set_appointment(token, visit_id, service_id, date, time):
    cookies = {
        'ARRAffinitySameSite': 'aa39394dbb18842b8ec3aa5c43eb93bb9c9e3ccdf2379a7672332b77a88a5770',
    }

    headers = {
        'Host': 'central.qnomy.com',
        'Sec-Ch-Ua': '"(Not(A:Brand";v="8", "Chromium";v="101"',
        'Preparedvisittoken': token,
        'Application-Api-Key': '8df143c7-fd10-460e-bcc0-d0c1cf947699',
        'Accept-Language': 'he',
        'Sec-Ch-Ua-Mobile': '?0',
        'Authorization': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6InljeDFyWFRmalRjQjZIQWV1aGxWQklZZmZUbyJ9.eyJpc3MiOiJodHRwOi8vY2VudHJhbC5xbm9teS5jb20iLCJhdWQiOiJodHRwOi8vY2VudHJhbC5xbm9teS5jb20iLCJuYmYiOjE2NTE4MzIzMjAsImV4cCI6MTY4MjkzNjMyMCwidW5pcXVlX25hbWUiOiI2ZDFlZDI3My1mY2FkLTQ1NDgtYmMwYi1iM2QyMzc2MDRiNDIifQ.TYbS8tx0-lT7BMm44tEYm2vsi9JZZ6STgdg0_KLG3VdLtZPmqejO-jnRV6A74nImIrNVarep9rbzWvDhSO7UNbqHnv_Zkz3FSFgvW63IX1qQsFDdZXWe4El-Juxq__ze9X8de6-xmz5pJTVa_S8uSniielHRd8lsLNmQlKOXCwvlPJF1ICi69aK2nkjXmpTclBDnQSFJtMwOmAFQMzT7_kfRPNRAqwPyExcdIDUybfQueRi9QMfWuskLHEG42D5ZQwvgxRtxlWRils_mggTckB5ShDEX-oXAt1nqqvf6WBz45NRl4WQJdgPEAGIRIHh7QgRk96deSAwUrpn3T4FAMg',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
        'Application-Name': 'myVisit.com v4.0',
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://myvisit.com',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://myvisit.com/',
        # 'Accept-Encoding': 'gzip, deflate',
        'Connection': 'close',
        # 'Cookie': 'ARRAffinitySameSite=aa39394dbb18842b8ec3aa5c43eb93bb9c9e3ccdf2379a7672332b77a88a5770',
    }

    logging.info(f'Setting appointment on {date}')
    response = requests.get(f'https://central.qnomy.com/CentralAPI/AppointmentSet?ServiceId={service_id}&appointmentDate={date}&appointmentTime={time}&position=%7B%22lat%22:%2231.7808%22,%22lng%22:%2235.2287%22,%22accuracy%22:1440%7D&preparedVisitId=87649690', cookies=cookies, headers=headers, verify=False)
    try:
        json_data = response.json()
        if not json_data['Success']:
            return json_data['Messages'][0]
        return '' # Success!
    except:
        return response.text

def set_appointment(id, phone, service_id, date_str, time):
    visit_token, visit_id = setup_visit()
    send_id(id, visit_token)
    send_phone(phone, visit_token)
    return _set_appointment(visit_token, visit_id, service_id, date_str, time)