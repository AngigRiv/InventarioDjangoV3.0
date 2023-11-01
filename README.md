# Pasos para clonar el project:
1) Instalar Virtual Env:
    pip install virtualenv
2) Crear entorno:
    python3 -m venv entorno
    ó
    python -m venv entorno
    ó
    py -m venv entorno
3) Activa el entorno:
    .\entorno\Scripts\activate   
4) Instalar Django:
   pip install django
5) Instalar la conexión con Mysql:
   pip install mysqlclient pymysql
6) Migraciones:
   - python manage.py makemigrations inventario
   - python manage.py makemigrations inventario
   - python manage.py migrate inventario 0011 --fake
   - python manage.py migrate inventario
   - python manage.py migrate
7) Ejecutar el proyecto
   python manage.py runserver
