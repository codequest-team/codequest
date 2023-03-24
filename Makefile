# Собрать
build:
	cp ./.envs/.local/.front-ms ./front-ms/.env
	cp ./.envs/.production/.front-ms ./front-ms/.env.production.local
	docker compose build --no-cache

# Запустить
up:
	docker compose rm -f
	docker compose up

# Остановить
down:
	docker compose down

# Очистка
clean:
	docker compose rm -f
	docker volume rm `docker volume ls -q`

dev:
	./docker-compose.sh dev

prod:
	./docker-compose.sh prod