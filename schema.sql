DROP TABLE IF EXISTS applications;

CREATE TABLE applications (
       id integer PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
       company text NOT NULL,
       role text NOT NULL,
       status text NOT NULL CHECK (status IN ('applied', 'interviewing', 'offer', 'rejected')),
       date_applied date NOT NULL
);
