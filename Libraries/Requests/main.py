# Requests

# Requests is a library that allows you to send HTTP requests using Python.
# It is a powerful and easy-to-use library for working with web APIs.

import requests

# help(requests)

# Get request
r = requests.get("https://httpbin.org/get")

if r.status_code == 200:
    print(r.json())
else:
    print(f"Error: {r.status_code}")

# Post request
r = requests.post("https://httpbin.org/post", data={"key": "value"})

if r.status_code == 200:
    print(r.json())
else:
    print(f"Error: {r.status_code}")

# Put request
r = requests.put("https://httpbin.org/put", data={"key": "value"})

if r.status_code == 200:
    print(r.json())
else:
    print(f"Error: {r.status_code}")

# Delete request
r = requests.delete("https://httpbin.org/delete")

if r.status_code == 200:
    print(r.json())
else:
    print(f"Error: {r.status_code}")

# Head request
r = requests.head("https://httpbin.org/get")

if r.status_code == 200:
    print(r.headers)
else:
    print(f"Error: {r.status_code}")

# Options request (Header : Access-Control-Alllow-Methods)
r = requests.options("https://httpbin.org/get")

# print(dir(r))

if r.status_code == 200:
    print(r.headers["Access-Control-Allow-Methods"])
else:
    print(f"Error: {r.status_code}")


# Passing parameters in url
payload = {"key1": "value1", "key2": "value2"}
r = requests.get("https://httpbin.org/get", params=payload)

print(r.url)

# Passing list of items
payload = {"key1": "value1", "key2": ["value2", "value3"]}
r = requests.get("https://httpbin.org/get", params=payload)

print(r.url)

# Custom headers
headers = {"key1": "value1", "key2": "value2"}
r = requests.get("https://httpbin.org/get", headers=headers)

print(r.headers)