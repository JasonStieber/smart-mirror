# from flask import Flask, request, session
# from config.secret_keys import MS_CLIENT_ID, MS_CLIENT_SECRET, MS_USER_ID, FLASK_SECRET
# from config.settings import TENANT_ID 
# import msal
# import webbrowser
# import requests
# import json
# from helper import print_pretty_request

# GRAPH_ENDPOINT = "https://graph.microsoft.com/v1.0/me/"
# app = Flask(__name__)

# app.secret_key = FLASK_SECRET

# # Create a ConfidentialClientApplication
# client_app = msal.ConfidentialClientApplication(
#     MS_CLIENT_ID,
#     authority=f'https://login.microsoftonline.com/{TENANT_ID}',
#     client_credential=MS_CLIENT_SECRET,
# )

# # The URL the user will be redirected to after they sign in
# redirect_uri = 'http://localhost:5000/getAToken'

# # The scopes your app requires
# scopes = ['Tasks.ReadWrite', 'Tasks.Read', 'Tasks.Read.Shared', 'Tasks.ReadWrite.Shared','User.ReadBasic.All','User.Read']

# @app.route('/')
# def home():
#     # Generate the URL for the user to sign in and get a code
#     authorization_url = client_app.get_authorization_request_url(scopes, redirect_uri=redirect_uri)
#     # Open the user's web browser to the Azure AD login page
#     webbrowser.open(authorization_url)
#     return "Check your browser for a sign-in prompt."

# @app.route('/getAToken')
# def get_token():
#     code = request.args.get('code')

#     # Get an access token and a refresh token using this code
#     result = client_app.acquire_token_by_authorization_code(code, scopes, redirect_uri)
#     print("\n\n\n The resutls from teh get token request are as follows \n\n\n")
#     print(json.dumps(result, indent=4))
#     if 'access_token' in result:
#         session['token'] = result['access_token']
#         #don't and use the token right now lsets see what happens
#         graph_header  = {
#             'Authorization': 'Bearer ' + result['access_token'],
#             'Accept': 'application/json',
#             'Host': "graph.microsoft.com"

#         }

#         #Make request to end point
#         response = requests.get(GRAPH_ENDPOINT, headers = graph_header)

#         if response.status_code == 200:
#             print("we got 200 ok response \n\n\n\n")
#             print(json.dumps(response.json(), indent=4))
#         elif response.status_code == 401:
#             print("401 error didn't receive graph info")
#             # print_pretty_request(response)
#             print(json.dumps(response.json(), indent=4))
#         else:
#             print("We got a responce other than 200 or 401 see bwlow")
#             print(json.dumps(response.json(), indent=4))
#         return "we relieved the data good job"
#         return "Got the access token. You can close this window and return back to the app."
#         #create header for new request to MS Graph
#     else:
#         return "Could not acquire token."

# # @app.route("/graphcall")
# # def graph_call():
# #     #retrieve token from the session
# #     token = session.get('token')

# #     if not token:
# #         return "No token found in session"
# #     else:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
# #         graph_header  = {
# #             'Authorization': 'Bearer ' + token,
# #             'Accept': 'application/json',
# #             'Host': 'graph.microsoft.com',

# #         }

# #         #Make request to end point
# #         response = requests.get(GRAPH_ENDPOINT, headers = graph_header)

# #         if response.status_code == 200:
# #             print(json.dumps(response.json(), indent=4))
# #         elif response.status_code == 401:
# #             print("401 error didn't receive graph info")
# #         return "we relieved the data good job"

# if __name__ == "__main__":
#     app.run(port=5000)
