# Lorry Admin #

## To init Admin ##

1) create virtual environment for python3.6:
```
virtualenv -p python3.6 venv
. venv/bin/activate
```

2) install requirements:
```
python -m pip install -r requirements.txt
```

3) create database and hstore extension to work with playhouse (peewee extension):
```
sudo -u postgres psql -c 'create database lorry_admin;'
```

4) make a copy of settings/local.py.default named settings/local.py and set valid local values:
```
cp settings/local.py.default settings/local.py
nano settings/local.py
```

5) do migrations
```
python manage.py migrate
```

6) fill database test lorries
```
python scripts/fill_db.py
```

## supervisor settings
1) install supervisor
```
install supervisor
```
2) make a copy scripts/lorry_admin.supervisor.conf.default named /etc/supervisor/lorry_admin.supervisor.conf
```
sudo cp scripts/lorry_admin.supervisor.conf.default /etc/supervisor/lorry_admin.supervisor.conf
```
3) first start supervisor
```
sudo service supervisor start
sudo supervisorctl
exit
```

## To run Admin ##

```
. venv/bin/activate
python manage.py runserver
```


## Development ##

1) install requirements-dev.txt
```
python -m pip install -r requirements-dev.txt
```

2) activate pre-commit
```
pre-commit install
```






