# Search Form
## Алгоритм запуска:
- ### git clone https://github.com/ByAvatarOff/SearchForm.git
- ### cd SearchForm
- ### mv .env.example .env  # OS Linux
- ### docker-compose build
- ### docker-compose up
- ### docker exec -it mongodb  mongorestore -d formdb ./formdb
## Запуск тестов
### docker exec -it forms pytest tests/
## endpoint /api/form/ [POST]
## example data request
`{ "user_email": "tsp7439@gmail.com", 
"user_phone": "+78822233333", 
"user_date": "2022-12-1"}`

## telegram: @ByAvatarOff