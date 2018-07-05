NAME=flask_skeleton

run:
	docker-compose build
	docker-compose up -d

stop:
	docker stop ${NAME}_uwsgi_1 ${NAME}_nginx_1
	docker rm ${NAME}_uwsgi_1 ${NAME}_nginx_1

test:
	docker-compose -f docker-compose.test.yml up --build --force-recreate
	docker stop ${NAME}_app_test_1
	docker rm ${NAME}_app_test_1
