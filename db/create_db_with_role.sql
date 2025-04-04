-- Drop the database and role if they already exist
DROP DATABASE IF EXISTS lernwe_local;
DROP ROLE IF EXISTS lernwe_local;

-- Create the role
CREATE ROLE lernwe_local WITH
    LOGIN
    SUPERUSER
    INHERIT
    CREATEDB
    PASSWORD 'lernwe_local';

-- Create the database owned by the new role
CREATE DATABASE lernwe_local
    WITH OWNER = lernwe_local;
