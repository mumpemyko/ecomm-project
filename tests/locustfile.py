from locust import HttpUser, task, between

class ProductUser(HttpUser):
    wait_time = between(1, 3)  # Users will wait 1 to 3 seconds between tasks

    @task
    def create_product(self):
        self.client.post("/products/", json={
            "name": "LoadTest Product",
            "price": 9.99,
            "stock": 10
        })

    @task
    def get_products(self):
        self.client.get("/products/")
