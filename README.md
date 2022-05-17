Проект "Payments"
===========================


Описание
----------------
---

>> stripe.com/docs - платёжная система с подробным API и бесплатным тестовым режимом для имитации и тестирования платежей. С помощью python библиотеки stripe можно удобно создавать платежные формы разных видов, сохранять данные клиента, и реализовывать прочие платежные функции. 
Мы предлагаем вам познакомиться с этой прекрасной платежной системой, реализовав простой сервер с одной html страничкой, который общается со Stripe и создает платёжные формы для товаров. 
Для решения нужно использовать Django. Решение бонусных задач даст вам возможность прокачаться и показать свои умения, но это не обязательно.


Задание
----------------
---
Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
Django Модель Item с полями (name, description, price) 
API с двумя методами:
* GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
* GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее  с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)




Основные технологии
-------------------
---

>> * Python
>> * Django
>> * Postgresql
>> * Docker
>> * Docker Compose


Установка и запуск
------------------
---

* Переходим в директорию
```
cd payments
```
* Делаем файл docker_commands.sh исполняемым
```
chmod +x docker_commands.sh
```

Запуск с помощью docker-compose
-------------------------------
---
~~~
docker-compose up -d --build
~~~