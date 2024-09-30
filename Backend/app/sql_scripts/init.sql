-- init.sql

CREATE EXTENSION IF NOT EXISTS "uuid-ossp"; 

CREATE TABLE hand (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    stack INT NOT NULL,
    setup TEXT NOT NULL,
    status BOOLEAN NOT NULL,
    hole_cards JSONB NOT NULL,
    pot INT NOT NULL, 
    winnings JSONB,
    time_stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE action (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    hand_id UUID NOT NULL REFERENCES hand(id) ON DELETE CASCADE,
    player INT,
    type TEXT NOT NULL,
    amount INT,
    card TEXT,
    time_stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);