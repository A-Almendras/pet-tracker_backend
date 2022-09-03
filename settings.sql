CREATE DATABASE pettracker;
CREATE USER pettracker_user WITH PASSWORD 'pettracker';
GRANT ALL PRIVILEGES ON DATABASE pettracker TO pettracker_user;