INSERT INTO SearchedEntities (n_status, s_name)
VALUES
       (0, 'IBM'),
       (0, 'Microsoft'),
       (0, 'HelloFresh');

INSERT INTO TextsGen (n_entity_id, n_status, s_text_type, s_message)
VALUES
       (1, 0, 'Email', 'Hi Click on this link:'),
       (1, 0, 'Email', 'Hi Click on this link:'),
       (3, 0, 'Email', 'Hi Click on this link:'),
       (2, 0, 'Email', 'Hi Click on this link:');

INSERT INTO DataFiles (n_entity_id, n_status, s_filename, s_path, s_title)
VALUES
       (3 ,0, 'company-infos.pdf', '/data' ,'IBM-PDF'),
       (1 ,0, 'company-infos.pdf', '/data' ,'Microsoft-PDF'),
       (2 ,0, 'company-infos.pdf', '/data' ,'HelloFresh-PDF');

INSERT INTO Keywords (n_file_id, s_keyword, s_tag, n_no_occurcances)
VALUES
       (3 ,'Manhattan', 'City', 3),
       (2 ,'New York', 'City', 4),
       (1 ,'Mr. Trump', 'Person', 1),
       (1 ,'FBI', 'Org', 12);
