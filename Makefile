.DEFAULT_GOAL:=help
SHELL:=/bin/bash

define run_docker
	$(if $(1), echo $(1), echo 'services list is not defined'; exit 1)
	docker-compose -f docker-compose.yml up "$1"
endef

all: help

run-application: ## Run all extended services (Postgres, Image handler, Redis, Application)
	@$(call run_docker,"application")

help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
