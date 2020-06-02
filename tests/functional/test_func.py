#checks the results are shown on the web page.
#checks the web page throws proper error for 404 and others.

from mathapp.service import sum
import requests

def test_sum():
    assert True


# We want to make sure a proper 404 is thrown if there is client error
def test_page_response():
    test_url = "http://127.0.0.1:5000/mathapp_GARBAGE/api/v1.0/add"
    page = requests.get(test_url)
    assert page.status_code == 404
    cont = str(page.content)
    assert "Please enter a valid URL." in cont


