CREATE TABLE User (
    username VARCHAR(255) PRIMARY KEY,
    password VARCHAR(255) NOT NULL,
    rol INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE Event (
    eventid        INTEGER PRIMARY KEY,
    name           VARCHAR(255) NOT NULL,
    description    VARCHAR(255),
    poster_path    VARCHAR(255),
    event_date     DATE NOT NULL,
    event_location VARCHAR(255),
    n_participants INTEGER NOT NULL DEFAULT 0,
    owner          VARCHAR(255) NOT NULL REFERENCES User(username)
);

CREATE TABLE Assitance (
    participant VARCHAR(255) REFERENCES User(username),
    event INT REFERENCES Event(eventid),
    credentials_path VARCHAR(255),
    certificate_path VARCHAR(255),
    assited BOOLEAN NOT NULL DEFAULT FALSE
);
