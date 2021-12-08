-- Drop all old
DROP TABLE IF EXISTS TextsGen;
DROP TABLE IF EXISTS Keywords;
DROP TABLE IF EXISTS DataFiles;
DROP TABLE IF EXISTS SearchedEntities;

-- Create tables
CREATE TABLE SearchedEntities
(
    n_entity_id SERIAL UNIQUE        NOT NULL,
    n_status    INT                  NOT NULL, -- 0,1,2,3 (ready, in progress, failed, error)
    s_name      VARCHAR(1024) UNIQUE NOT NULL,
    s_query     VARCHAR(2048),
    ts_searched TIMESTAMP,
    b_tfidf     BOOLEAN DEFAULT False,
    b_word2vec  BOOLEAN DEFAULT False,
    b_ner       BOOLEAN DEFAULT False,
    PRIMARY KEY (n_entity_id)
);

CREATE TABLE TextsGen
(
    n_text_id    SERIAL UNIQUE NOT NULL,
    n_entity_id  INT           NOT NULL,
    n_status     INT           NOT NULL, -- 0,1,2,3 (ready, in progress, failed, error)
    s_text_type  VARCHAR(128)  NOT NULL, -- Email, Newsletter, BusinessLetter
    s_message    VARCHAR       NOT NULL, -- Full generated Text
    s_meta_info  VARCHAR(4096),
    s_link       VARCHAR(4096),          -- CALL TO ACTION URL
    ts_generated TIMESTAMP,
    PRIMARY KEY (n_text_id),
    FOREIGN KEY (n_entity_id) REFERENCES SearchedEntities (n_entity_id)

);

CREATE TABLE DataFiles
(
    n_file_id      SERIAL UNIQUE NOT NULL,
    n_entity_id    INT           NOT NULL,
    n_status       INT           NOT NULL, -- 0,1,2,3 (ready, in progress, failed, error)
    s_path         VARCHAR(4096),
    s_title        VARCHAR(4096),
    s_description  VARCHAR(4096),
    s_text         VARCHAR,
    ts_created     TIMESTAMP,
    b_leakage_warn BOOLEAN DEFAULT False,
    PRIMARY KEY (n_file_id),
    FOREIGN KEY (n_entity_id) REFERENCES SearchedEntities (n_entity_id)

);

CREATE TABLE Keywords
(
    n_keyword_id     SERIAL UNIQUE NOT NULL,
    n_file_id        INT           NOT NULL,
    s_keyword        VARCHAR(4096) NOT NULL,
    s_tag            VARCHAR(4096) NOT NULL,
    n_no_occurcances INT,
    PRIMARY KEY (n_keyword_id),
    FOREIGN KEY (n_file_id) REFERENCES DataFiles (n_file_id)

);