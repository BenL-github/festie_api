DROP TABLE IF EXISTS Genre CASCADE;
DROP TABLE IF EXISTS US_State CASCADE;
DROP TABLE IF EXISTS App_User CASCADE;
DROP TABLE IF EXISTS Festival CASCADE;
DROP TABLE IF EXISTS Artist CASCADE;
DROP TABLE IF EXISTS Favorite_Artist CASCADE;
DROP TABLE IF EXISTS Artist_Festival CASCADE;

CREATE TABLE IF NOT EXISTS Genre (
    genre_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    genre_name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS US_State (
    state_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    state_name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS App_User (
    app_user_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    f_name VARCHAR(255) NOT NULL,
    l_name VARCHAR(255) NOT NULL, 
    email VARCHAR(255) NOT NULL, 
    state_id INT NOT NULL,
    CONSTRAINT fk_app_user_state_id
        FOREIGN KEY (state_id) 
            REFERENCES US_State(state_id)
);

CREATE TABLE IF NOT EXISTS Festival (
    festival_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    festival_name VARCHAR(255) NOT NULL UNIQUE,
    price SMALLINT NOT NULL, 
    state_id INT NOT NULL, 
    CONSTRAINT fk_festival_state_id
        FOREIGN KEY (state_id)
            REFERENCES US_State(state_id)
);

CREATE TABLE IF NOT EXISTS Artist (
    artist_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    artist_name VARCHAR(255) NOT NULL UNIQUE,
    genre_id INT NOT NULL,
    CONSTRAINT fk_artist_genre_id
        FOREIGN KEY (genre_id)
            REFERENCES Genre (genre_id)
);

CREATE TABLE IF NOT EXISTS Favorite_Artist (
    app_user_id INT NOT NULL,
    artist_id INT NOT NULL,
    score INT NOT NULL,
    CONSTRAINT fk_favorite_artist_app_user_id
        FOREIGN KEY (app_user_id)
            REFERENCES App_User (app_user_id),
    CONSTRAINT fk_favorite_artist_artist_id
        FOREIGN KEY (artist_id)
            REFERENCES Artist (artist_id)
);

CREATE TABLE IF NOT EXISTS Artist_Festival (
    artist_id INT NOT NULL,
    festival_id INT NOT NULL,
    CONSTRAINT fk_artist_festival_artist_id
        FOREIGN KEY (artist_id)
            REFERENCES Artist (artist_id),
    CONSTRAINT fk_artist_festival_festival_id
        FOREIGN KEY (festival_id)
            REFERENCES Festival (festival_id)
);