# Beyond Backend
A simple REST backend to start simulations and retrieve results asynchronously

## Used tools
* Flask + connexion
* openapi-generator to create and update stubs from openapi.yaml
* Gunicorn for wsgi deployment
* Celery for background tasks
* Redis as celery backend
* Caddy as reverse proxy
* Docker and docker-compose for deployment and containerization
* Ansible to simplify deployment
* PDM as package and dependency manager
* pyenv to ensure the same python version on all dev machines
