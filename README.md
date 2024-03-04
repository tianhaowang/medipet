docker build -t my_flask_app .

docker network create app

docker run --name mysql-container --network app -v mysql-volume:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=password -p 3306:3306 -d mysql:latest 

docker run --name phpmyadmin --network app -d --link mysql-container:db -p 8080:80 phpmyadmin

Set up db:
Go to 8080 go to sql, create medibot databse, then proceed to run all the sql scripts in databse/* 

docker run --network app -p 1492:5000 my_flask_app

cd web && python3 -m http.server

database: localhost::8080
website: localhost::8000
apis: localhost::1492


