# FastAPI
A RESTful API service template built with fastapi.

![Integration](https://github.com/DarkbordermanTemplate/fastapi/workflows/Integration/badge.svg)
![Build](https://github.com/DarkbordermanTemplate/fastapi/workflows/Build/badge.svg)
![Release](https://github.com/DarkbordermanTemplate/fastapi/workflows/Release/badge.svg)

## Development

### Prerequisite

| Name | Version |
| --- | --- |
| Python | 3.8 |
| pipenv(Python module) | 2018.11.26 or up |

### Environment setup

0. Initialize environment variable

```
cp sample.env .env
```

1. Initialize Python environment

```
pipenv install --dev
```

2. Enter the environment and start developing

```
pipenv shell
```

3. Start development API service

```
cd api/
uvicorn app:APP
```
The server will run at http://127.0.0.1:8000


### Formatting

This project uses `black` and `isort` for formatting

```
inv integration.reformat
```

### Linting

This project uses `pylint` and `flake8` for linting

```
inv integration.lint
```

### Testing

This project uses `pytest` and its extension(`pytest-cov`) for testing

```
inv integration.pytest
```

## Deployment

### Prerequisite

| Name | Version |
| --- | --- |
| Docker | 19.03.6 |
| docker-compose | 1.17.1 |

### Building image

```
docker-compose build
```
This will build the image with tag `fastapi:latest`

### Deployment step

The service is deployed with `docker-compose`

0. Start containers
```
docker-compose up
```

## Contribution

* Darkborderman/Divik(reastw1234@gmail.com)
