import requests
import json

# an example of a post request — loads the dictionary
res = requests.post('http://localhost:8080/load', json=["foOBAr", "aabb", "baba", "boofar", "test"])

# an example of a get request — returns anagrams for a given word from a dictionary we load in POST 
res2 =  requests.get('http://localhost:8080/get', params={'word' : 'baab'})
if res2.ok:
    print(res2.json())
