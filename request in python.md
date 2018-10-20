### Library Required

We will be using Requests library as it is concise and easy to use. Install it using

```sh
pip install requests
```

## A Simple Example

```python
import requests

r = requests.get('http://maps.googleapis.com/maps/api/geocode/json?address=Bengaluru')
print (r.text)
```
We create an object `r` which will store the request-response. `requests.get` method send a get request to the `googleapis` server. To see content of the response we use `r.text`.

Use `r.status_code` to see the status code.

## Post request example

```python
import requests
 
url = 'http://httpbin.org/post'
payload = {'a':'test', 'b':'my post request'}
r = requests.post(url, data=payload) 
print(r.json())

data = r.json()
print(data['form'])
```

The above example sends a post request to `httpbin`. `payload` is the data that we want to send in the post request. `r.json()` prints the whole response message, while `data['form']` prints the data that we sent in the payload.

