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

