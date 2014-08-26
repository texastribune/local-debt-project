resetdb:
	dropdb local_debt
	createdb local_debt
	psql -d local_debt -c 'CREATE EXTENSION postgis;'
	python manage.py syncdb --noinput
	python manage.py migrate
	python manage.py load_shapefiles
	python import.py
