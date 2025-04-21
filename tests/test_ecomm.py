import requests

BASE_URL = "http://127.0.0.1:5000"

def test_get_products():
    response = requests.get(f"{BASE_URL}/products")
    assert response.status_code == 200
    
def test_get_product():
    response = requests.get(f"{BASE_URL}/products/1")
    assert response.status_code == 200
    
def test_post_user():
    response = requests.post(f"{BASE_URL}/products", json={"name": "earbuds", "price": 150, "stock":3})
    assert response.status_code == 201 # Expect HTTP 201 Created
  