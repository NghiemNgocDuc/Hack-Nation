.PHONY: up down logs test fmt
up:
	docker compose up --build

logs:
	docker compose logs -f --tail=200

down:
	docker compose down -v

test:
	pytest -q

fmt:
	ruff check --fix || true
