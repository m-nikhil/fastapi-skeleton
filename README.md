**Developement setup**
- Required python3 and pip3
- ```pip3 install pipenv```
- ```pipenv install```, at the application directory
- copy .env.sample to .env and then fillin the values.
- ```sh start.sh```, to start the fastapi server
- ```export PYTHONPATH=.```, at the application directory each time before development

**Scripts**
- docker-compose up -d --build --force-recreate --renew-anon-volumes
- alembic revision  --autogenerate -m "create user table"
- alembic upgrade head
