# check-imei-bot

Для запуска приложения:
1. git clone https://github.com/paddington22/check_imei_bot.git
2. для установки виртуального окружения использую rye:
    * rye sync 
   P.S так же можно воспользоваться poetry
    * poetry init
    * poetry install
3. создать бд в PosgreSQL 
4. создать .env файл, образец прикреплю в письме 
5. запустить программу для вебхуков (использовал tuna)
6. добавить в .env файл BOT_WEBHOOK_URL 
7. заполнить все остальные поля в .env файле 
8. выполнить команду aerich upgrade 
9. запустить run_server.py 
10. документация доступна на localhost:8000/docs 
11. бот доступен, в боте с токеном, который указан в .env файле