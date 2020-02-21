import requests
import json

# an example of a post request
res = requests.post('http://localhost:8080/load', json=["foobar", "aabb", "baba", "boofar", "test"])
if res.ok:
    print(res.json())

# an example of a get request
res2 =  requests.get('http://localhost:8080/get', params={'word' : 'ttse'})
if res2.ok:
    print(res2.json())
