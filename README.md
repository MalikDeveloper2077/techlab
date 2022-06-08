### Перед запуском
```
pip3 install -r requirements.txt
```  
  
Необходимо создать в корне директории файл **.env**, в котором нужно указать  
```DATABASE_URL=...```  
Как показано в **.env.example**, или в **core.settings** (поддерживается **PostgreSQL**)

### Для запуска сервера  
```
uvicorn main:app --reload
```  
  
API доступен по адресу *localhost:8000/docs*

### Для запуска нагрузочного тестирования  
```
locust -f app/tests/v1/users_locust.py --headless --host http://localhost:8000 -u 10 -r 1 -t 10s
```  
  
*где:*  
*--host* - url сервера для тестирования  
*-u* количество пользователей  
*-r* количество создаваемых пользователей в секунду  
*-t* ограничение по времени (s/m/h)  
  
