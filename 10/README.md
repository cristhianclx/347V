flask --app main shell

flask --app main run --reload


http POST 127.0.0.1:5000/login username=test password=123456

HTTP/1.1 200 OK
Connection: close
Content-Length: 288
Content-Type: application/json
Date: Wed, 11 Oct 2023 00:28:08 GMT
Server: Werkzeug/3.0.0 Python/3.8.13

{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5Njk4NDA4OCwianRpIjoiM2VhMGIxODktODgwOC00YTdkLTlmMjktMDdjOGM2MTFlNGNlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InRlc3QiLCJuYmYiOjE2OTY5ODQwODgsImV4cCI6MTY5Njk4NDk4OH0.McXEf6-0tPVzmC-_iSEKZ5gR6Ja18H95AWH61qaQwIY"
}

http GET 127.0.0.1:5000/protected "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5Njk4NDA4OCwianRpIjoiM2VhMGIxODktODgwOC00YTdkLTlmMjktMDdjOGM2MTFlNGNlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InRlc3QiLCJuYmYiOjE2OTY5ODQwODgsImV4cCI6MTY5Njk4NDk4OH0.McXEf6-0tPVzmC-_iSEKZ5gR6Ja18H95AWH61qaQwIY"

{
    "is_logged": true
}
