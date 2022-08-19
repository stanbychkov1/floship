# floship

1. Создайте файл .env в корневом каталоге со следующими переменными:
```bash
DJANGO_USERNAME_ADMIN=admin
DJANGO_PASSWORD_ADMIN=admin
DJANGO_EMAIL_ADMIN=admin@admin.com
SECRET_KEY=<Задайте ваш секртеный ключ>
```
2. Запустите комманду ```docker-compose up --build``` в корневом каталоге приложения.
Приложению по умолчанию создано как магазин и три склада.