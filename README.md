# Currency Reference
Цель проекта "Парсер на FastAPI" - создать парсер, который собирает данные с сайта https://jservice.io/api/random?count=1
и сохраняет их в БД.
### Что умеет приложение
- При POST запросе по адресу http://127.0.0.1:8000/parser/ происходит автоматическая сборка вопросов и сохранение их в БД
- Пример запроса: { "questions_num": 3 }
### Установка и запуск
1. Скопировать репозиторий git clone https://github.com/SuNseTgReeN/FastAPI_Parser
2. Создать виртуальное окружение и установить все зависимости из requirements.txt
3. Переименовать файл .env.dev на .env
4. Выполнить сборку и запуск контейнера с приложением использую команду docker-compose up -d --build
5. Перейдите по ссылке http://127.0.0.1:8000/docs и выполните POST запрос из примера, либо можно использовать postman и выполнить запрос с него
6. Вы великолепны!
