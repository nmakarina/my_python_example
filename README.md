# my_python_example

Python 2.7.7 + Flask
база данных - MongoDB
для асинхронной работы используется gevent

сервис для асинхронного обмена данными формата json. Обмен данными происходит по идентификатору получателя. 
При отправке данных на сервер они хранятся и отображаются в течении часа, после чего удаляются.

для запуска:
1. скачать монго https://www.mongodb.com/download-center?jmp=nav#community
2. создать папку C:\data\db
3. запустить …\MongoDB\Server\3.2\bin\mongod.exe
4. запустить my_progect.py
5. сервис доступен по адресу http://localhost:5000/<user_id>, например http://localhost:5000/id1
6. кнопка Send - отправка запроса для user_id
7. кнопка View message list - вывод списка всех запросов за последний час для user_id
