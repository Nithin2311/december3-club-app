# December3.club Makefile — common operations.
.DEFAULT_GOAL := help
.PHONY: help up down reset build logs ps gen-secrets

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN{FS=":.*?## "}{printf "  \033[36m%-14s\033[0m %s\n",$$1,$$2}'

up: ## Build + start the whole stack
	docker compose up -d --build

down: ## Stop the stack (keep volumes)
	docker compose down

reset: ## Stop the stack and DELETE the database volume (destroys data)
	docker compose down -v

build: ## Build images without starting
	docker compose build

logs: ## Tail logs for all services
	docker compose logs -f

ps: ## Show service status
	docker compose ps

gen-secrets: ## Print fresh secrets to paste into .env
	@echo "POSTGRES_PASSWORD=$$(openssl rand -hex 24)"
	@echo "SESSION_SECRET=$$(openssl rand -hex 32)"
