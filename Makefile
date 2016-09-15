.SILENT:

docker-api:
	docker exec -it bookmark-api bash

docker-web:
	docker exec -it bookmark-web bash

docker-db:
	docker exec -it bookmark-db bash
