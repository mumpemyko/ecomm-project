API testing strategy (unit, integration, load).
This API can be tested unit by unit, meaning testing the endpoints where the client Is exposed to the API using pytests. 
As for integration testing, this test aims at the real interaction between modules like flask routes and database. So I used postman, pytest
Load testing, I use locust configured it to test using 100 users at a ramp of 10. Got 0% failures.
o	Swagger & Redoc usage guide.
Swagger and redoc are for documentation of the api.
Guidelines on how to use Swagger
1.	Run the app.py
2.	Go to https//:127.0.0.1:5000 and find a swagger Api page with all the endpoints of the products
3.	Click on any endpoint and follow the prompts
As for the redoc
1.	Copy the swagger.json and save it in the folder. http://localhost:5000/swagger.json
2.	Open bash in the same directory as the json file and run this commad;
curl http://localhost:5000/swagger.json -o openapi.json

