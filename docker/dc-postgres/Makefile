#!/usr/bin/env make

include makefile.env
export

pwd := $(shell pwd)

volume_postgres := postgres-data
dc := docker-compose.yml

remove_volumes:
	@echo "Remove PostgreSQL volumes"
	@if [ -d ${volume_postgres} ]; then \
  		sudo rm -rf ${volume_postgres}; \
	 fi

up:
	@echo "Docker compose up"
	@docker-compose --file ${dc} up --detach

down:
	@echo "Docker compose down"
	@docker-compose --file ${dc} down --volumes

pure_up: up

pure_down: down remove_volumes

logs:
	@docker-compose --file ${dc} logs --follow
