# FinTec


#### Generating Screts in python
```
python -c "import secrets; print(secrets.token_urlsafe(38))"
```

#### Update setuptools
``` pipinstall  --upgrade  setuptools```

#### Check if docker-compose can pick up .env variables
```
docker-compose -f docker-compose-local.yml config
```
#### Build docker file
```docker-compose -f docker-compose-local.yml up  --build -d  --remove-orphans ```