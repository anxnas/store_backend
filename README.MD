# Backend API для интернет-магазин

Это проект интернет-магазина, который предоставляет CRUD API для управления товарами, их типами и ценами. Проект построен на Django и Django REST Framework.

## Установка

### С использованием Poetry

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/anxnas/store_backend.git
   cd store_backend
   ```

2. **Установите Poetry, если он еще не установлен:**

   ```bash
   pip install poetry
   ```

3. **Установите зависимости:**

   ```bash
   poetry install
   ```

4. **Активируйте виртуальное окружение:**

   ```bash
   poetry shell
   ```

5. **Примените миграции:**

   ```bash
   python manage.py migrate
   ```

6. **Создайте суперпользователя для доступа к админке:**

   ```bash
   python manage.py createsuperuser
   ```

7. **Запустите сервер:**

   ```bash
   python manage.py runserver
   ```

### С использованием Docker

1. **Убедитесь, что Docker установлен и запущен.**

2. **Убедитесь, что все переменные окружения правильно настроены в файле `.env`.**

3. **Измените пароль админа в `docker-compose.yml`**

4. **Соберите и запустите контейнеры:**

   ```bash
   docker-compose up --build
   ```

## Использование

### Админка

Админка доступна по адресу: [http://localhost:8000/admin/](http://localhost:8000/admin/)

### API Эндпоинты

- **Продукты (Products)**
  - Получить список всех продуктов: `GET http://localhost:8000/api/products/`
  - Создать новый продукт: `POST http://localhost:8000/api/products/`
  - Получить конкретный продукт: `GET http://localhost:8000/api/products/{id}/`
  - Обновить продукт: `PUT http://localhost:8000/api/products/{id}/`
  - Частично обновить продукт: `PATCH http://localhost:8000/api/products/{id}/`
  - Удалить продукт: `DELETE http://localhost:8000/api/products/{id}/`
  - Уменьшить количество товара: `POST http://localhost:8000/api/products/{id}/decrease_quantity/`

- **Типы продуктов (Product Types)**
  - Получить все типы: `GET http://localhost:8000/api/product-types/`
  - Создать тип: `POST http://localhost:8000/api/product-types/`
  - Получить конкретный тип: `GET http://localhost:8000/api/product-types/{id}/`
  - Обновить тип: `PUT http://localhost:8000/api/product-types/{id}/`
  - Частично обновить тип: `PATCH http://localhost:8000/api/product-types/{id}/`
  - Удалить тип: `DELETE http://localhost:8000/api/product-types/{id}/`

- **Цены (Prices)**
  - Получить все цены: `GET http://localhost:8000/api/prices/`
  - Создать цену: `POST http://localhost:8000/api/prices/`
  - Получить конкретную цену: `GET http://localhost:8000/api/prices/{id}/`
  - Обновить цену: `PUT http://localhost:8000/api/prices/{id}/`
  - Частично обновить цену: `PATCH http://localhost:8000/api/prices/{id}/`
  - Удалить цену: `DELETE http://localhost:8000/api/prices/{id}/`


## Зависимости

- Python 3.7 или новее
- Django 3.1 или новее
- Django REST Framework 3.12 или новее

## Лицензия

Этот проект лицензирован под MIT License. Подробности см. в файле LICENSE.