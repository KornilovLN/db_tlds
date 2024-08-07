-- init.sql

DO
$$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'leon') THEN
      CREATE ROLE leon WITH LOGIN PASSWORD '18leon28';
   END IF;
END
$$;

DO
$$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'tsdb') THEN
      CREATE DATABASE tsdb;
      GRANT ALL PRIVILEGES ON DATABASE tsdb TO leon;
   END IF;
END
$$;

-- Подключаемся к базе данных tsdb и создаем расширение TimescaleDB
\connect tsdb

CREATE EXTENSION IF NOT EXISTS timescaledb;

-- Создаем таблицу data
CREATE TABLE IF NOT EXISTS data (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMPTZ NOT NULL,
    container_id VARCHAR(255) NOT NULL,  -- Изменено на строку
    x DOUBLE PRECISION NOT NULL,
    y DOUBLE PRECISION NOT NULL,
    counter INT NOT NULL
);

-- Создаем таблицу status
CREATE TABLE IF NOT EXISTS status (
    id SERIAL PRIMARY KEY,
    flag VARCHAR(255) NOT NULL
);
