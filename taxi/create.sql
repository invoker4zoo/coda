DROP TABLE if EXISTS taxi_1;
CREATE TABLE recruitment
(
  data_date           TEXT,
  gps_time            TEXT,
  taxi_chart          TEXT,
  taxi_id             TEXT,
  longtitude          FLOAT,
  latitude            FLOAT,
  speed               FLOAT,
  otientation         FLOAT,
  status              INTEGER,
  useful              INTEGER
);