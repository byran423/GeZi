def get_auth():
	from lesson4.part4.Adminlogin import Adminlogin
	login_api_obj = Adminlogin().send_request()
	return_data = login_api_obj.resp.data
	return return_data.tokenHead + ' ' + return_data.token


auth_token = get_auth()


