# My First FastAPI with Python 🐍💻

This is a test with FastAPI. 

### virtual environment

> 1. Go to the directory, for example:
> `cd C:\Users\Saida\Desktop\Corus_prueba\TechnicalTestCorusBackendSaidaHumbert`
> 
> 2. Create an virtual environment:
> `python -m venv "name_environment"`
> 
> 3. Install dependencies:
> `pip install -r requirements.txt`
> 
> 4. activate environment:
> `myenv\Scripts\activate`
> 
> 5. deactivate environment: 
> `deactivate`


### Execute app:

Instantly updates changes to the main file

`uvicorn __init__:app --reload` 

### Start app
To test the different functions of the app use:

`http://localhost:8000/docs`

More information about documentation for FastAPI: [SwaggerUI](https://github.com/swagger-api/swagger-ui) 

### Tests
To launch the tests:

 `python -m pytest tests`

### Docker

Example for create a new image:

`docker build -t 'name_image' .`

Start container and mapping port

`docker run -d -p 8000:8080 'name_image'`

*Example correct logs that can you see:*
> 
> INFO:     172.17.0.1:56410 - "GET / HTTP/1.1" 200 OK
> 
> INFO:     Started server process [1]
> 
> INFO:     Waiting for application startup.
> 
> INFO:     Application startup complete.
> 
> INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)



## webgrafía
I used this links for help me:

- https://kinsta.com/es/blog/fastapi/
- https://fastapi.tiangolo.com/
- https://aulasoftwarelibre.github.io/taller-de-docker/dockerfile/
- https://www.fastapitutorial.com/blog/unit-testing-in-fastapi/
