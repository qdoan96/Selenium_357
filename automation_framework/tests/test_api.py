import pytest
import sys
import os
from automation_framework.API.api_helper import APIHelper

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture(scope="module")
def api_helper():
    return APIHelper()

def test_get_user_information(api_helper):
    base_url = "https://jsonplaceholder.typicode.com"
    url = f"{base_url}/users/1"
    response_data = api_helper.get_data(url)

    # Các assertion của Pytest đơn giản hơn và không cần self.
    assert response_data is not None
    assert isinstance(response_data, dict)
    assert response_data['id'] == 1
    print("\nTest GET thành công!")

def test_create_new_user(api_helper):
    base_url = "https://jsonplaceholder.typicode.com"
    url = f"{base_url}/posts"
    new_user_data = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

    response_data = api_helper.post_data(url, data=new_user_data)

    # Các assertion của Pytest
    assert response_data is not None
    assert isinstance(response_data, dict)
    assert 'id' in response_data  # Kiểm tra xem có trường 'id' trả về không
    assert response_data['title'] == "foo"
    print("Test POST thành công!")