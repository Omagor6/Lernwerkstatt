
-- DROP TABLES
DROP TABLE IF EXISTS student_mentor CASCADE;
DROP TABLE IF EXISTS absence CASCADE;
DROP TABLE IF EXISTS goal CASCADE;
DROP TABLE IF EXISTS person CASCADE;

-- DROP ENUM TYPES
DROP TYPE IF EXISTS role CASCADE;
DROP TYPE IF EXISTS goal_type CASCADE;

-- CREATE ENUM TYPES
CREATE TYPE role AS ENUM ('student', 'coach', 'bb');
CREATE TYPE goal_type AS ENUM ('individual');

-- CREATE person TABLE
CREATE TABLE person (
    person_id      SERIAL PRIMARY KEY,
    name           VARCHAR(255),
    type           role NOT NULL,
    surname        VARCHAR(255),
    apprenticeship VARCHAR(255),
    phone          VARCHAR(255),
    email          VARCHAR(255),
    password       VARCHAR(255)
);

-- CREATE goal TABLE
CREATE TABLE goal (
    goal_id           SERIAL PRIMARY KEY,
    description       TEXT,
    grading           INT, -- 1–4 depending on type
    created_timestamp TIMESTAMP DEFAULT current_timestamp,
    due_date          DATE,
    type              goal_type NOT NULL
);

-- CREATE absence TABLE
CREATE TABLE absence (
    absence_id   SERIAL PRIMARY KEY,
    student_id   INT REFERENCES person(person_id) ON DELETE RESTRICT,
    mentor_id    INT REFERENCES person(person_id) ON DELETE RESTRICT,
    absence_time TIMESTAMP NOT NULL,
    CHECK (absence_time::time = '08:00:00' OR absence_time::time = '12:00:00')
);

-- CREATE student_mentor TABLE
CREATE TABLE student_mentor (
    id         SERIAL PRIMARY KEY,
    student_id INT REFERENCES person(person_id) ON DELETE RESTRICT,
    mentor_id  INT REFERENCES person(person_id) ON DELETE RESTRICT,
    responsible_from    DATE,
    responsible_until   DATE
);
