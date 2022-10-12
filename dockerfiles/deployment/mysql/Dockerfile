FROM mysql

ENV MYSQL_ROOT_PASSWORD password
ADD jsp_backup.sql /docker-entrypoint-initdb.d

EXPOSE 3306
