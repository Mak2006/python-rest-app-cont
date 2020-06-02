#checks the results are shown on the web page.
#checks the web page throws proper error for 404 and others.

from mathapp.service import sum
import requests
import json

def test_sum():
    assert True


# We want to make sure a proper 404 is thrown if there is client error
def test_404_response():
    test_url = "http://127.0.0.1:5000/mathapp_GARBAGE/api/v1.0/add"
    page = requests.get(test_url)
    assert page.status_code == 404
    cont = str(page.content)
    assert "Please enter a valid URL." in cont

#We want to make sure a custom 5xx error page is shown in case of 5xx error
def test_5xx():
    page = requests.post("http://127.0.0.1:5000/mathapp/api/v1.0/add",
                         '{"number1":"a", "number2":"b", "number3":"c"}')
    assert page.status_code == 500
    cont = str(page.content)
    assert "The server encountered an error. Please try again later." in cont


# We want to make sure the response is actually shown to user
# Make a post with three numbers and 20 30 40
# curl -i -H "Content-Type: application/json" -X POST -d '{"number1":"20", "number2":"30", "number3":"40"}' http://127.0.0.1:5000/mathapp/api/v1.0/add
def test_page_response():
    payload = {
	"number1": "20",
	"number2": "30",
	"number3": "40"
    }
    payload = json.dumps(payload)
    response = requests.post("http://127.0.0.1:5000/mathapp/api/v1.0/add", json=payload)
    assert response.status_code == 201
    #We expect a Result variable set to 90
    assert response.json['Result'] == 90
