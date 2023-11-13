import http.client

conn = http.client.HTTPConnection("127.0.0.1", 8000)

# @app.get("/")
conn.request("GET", "/")
res = conn.getresponse()
print(res.read().decode())

# @app.get("/recipt")
conn.request("GET", "/recipt")
res = conn.getresponse()
print(res.read().decode())

# @app.post("/recipt/")
headers = {'Content-type': 'application/json'}
body = '{"title": "title", "ingred": "ingred", "quantity": "quantity", "mesure": "mesure", "description": "description"}'
conn.request("POST", "/recipt/", body, headers)
res = conn.getresponse()
print(res.read().decode())

# @app.delete("/recipt/{recipt_id}")
conn.request("DELETE", "/recipt/1")
res = conn.getresponse()
print(res.read().decode()) 

# @app.put("/recipt/{recipt_id}")
headers = {'Content-type': 'application/json'}
body = '{"title": "title", "ingred": "ingred", "quantity": "quantity", "mesure": "mesure", "description"}'
conn.request("PUT", "/recipt/1", body, headers)
res = conn.getresponse()
print(res.read().decode())
