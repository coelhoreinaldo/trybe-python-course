FROM mysql:8.0.32

ENV MYSQL_ROOT_PASSWORD password

# Copia o script SQL que acabamos de criar para um determinado diretório no container
COPY ./database/01_create_database.sql /docker-entrypoint-initdb.d/data.sql01kc


# docker run -d -p 3306:3306 --name=schedule-mysql-container -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=schedule_database schedule-db