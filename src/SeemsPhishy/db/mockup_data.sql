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

INSERT INTO DataFiles (n_entity_id, n_status, s_path, s_title)
VALUES
       (3 ,0, 'https://www.ibm.com/annualreport/assets/downloads/IBM_Annual_Report_2018.pdf' ,'IBM-PDF'),
       (1 ,0, 'https://www.ibm.com/annualreport/assets/downloads/IBM_Annual_Report_2018.pdf' ,'Microsoft-PDF'),
       (2 ,0, 'https://www.ibm.com/annualreport/assets/downloads/IBM_Annual_Report_2018.pdf' ,'HelloFresh-PDF');

INSERT INTO Keywords (n_file_id, s_keyword, s_tag, n_no_occurrences)
VALUES
       (3 ,'Manhattan', 'City', 3),
       (2 ,'New York', 'City', 4),
       (3 ,'New York', 'City', 2),
       (1 ,'Mr. Trump', 'Person', 1),
       (1 ,'FBI', 'Org', 12);
