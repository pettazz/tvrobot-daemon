#!/usr/bin/env sh

mysql -u root -h 127.0.0.1 -e "DROP DATABASE IF EXISTS tvrobotd; CREATE DATABASE tvrobotd;"
mysql -u root -h 127.0.0.1 tvrobotd < schema-test.sql

if [ -f core/config.py ];
then
    cp core/config.py core/config-backup.py
fi

cp core/config-test.py core/config.py

nosetests test/

mysql -u root -h 127.0.0.1 -e "DROP DATABASE tvrobotd;"

if [ -f core/config-backup.py ];
then
    mv core/config-backup.py core/config.py
fi