CREATE DATABASE testdb;


USE testdb;




CREATE TABLE user(
id INT PRIMARY KEY, 
 name VARCHAR(50),
 email VARCHAR(60)
 );

 
 
 CREATE TABLE news(
 id INT ,
 newsid INT,
 title VARCHAR(50),
 body VARCHAR(100),
 created_at VARCHAR (60)
 );


INSERT INTO user VALUES
 (1, 'Tayiba','jf47242420@gmail.com'),
 (2, 'Tasnova','taherajanant@gamil.com'),
 (3, 'Tawfa','jannatul@gamil.com'),
 (4, 'Israt','isratjahan@gamil.com'),
 (5, 'Liza','lizaahmed@gamil.com'),
 (6, 'Neha','nehaf@gamil.com'),
 (7, 'Nila','nilaf@gamil.com'),
 (8, 'Inaya','inayauddin@gamil.com'),
 (9, 'Fahmida','fahmida@gamil.com'),
 (10, 'Salwa','salwaj@gamil.com');


INSERT INTO news (id, newsid, title, body, created_at)
VALUES
(0, 1, 'Double Decker Launched',
 'MU launched a double decker bus for students last semester.',
 '2024-10-15'),

(1, 2, 'Sattol Bus Updated',
 'The Sattol route bus timing was updated for better transport.',
 '2024-11-02'),

(2, 3, 'Exam Office Updated Routine',
 'The exam office published a new exam routine.',
 '2024-12-01'),

(3, 4, 'SWE Lab in Room 301',
 'The SWE lab in room 301 is used for classes of SWE department students.',
 '2024-08-20'),

(4, 5, 'University Bank Extended Hours',
 'The MU banking booth extended its daily service time.',
 '2024-10-05'),

(5, 6, 'SWE BBQ Night Held',
 'The SWE Department arranged a BBQ night for all batches.',
 '2024-12-20'),

(6, 7, 'Programming Olympiad S2 Held',
 'Programming Olympiad Season 2 was held on 18 June with Programming Hero as digital partner.',
 '2024-06-18'),

(7, 8, 'SWE TechJam Contest Held',
 'The SWE TechJam programming contest was successfully completed in January 2025.',
 '2025-01-10'),

(8, 9, 'Campus WiFi Upgraded',
 'MU completed a full upgrade of the campus WiFi system.',
 '2024-08-12'),

(9, 10, 'Seven Vikings Won Match',
 'The SWE Seven Vikings football team won the inter-department match.',
 '2024-11-22'),

(10, 11, 'SWE Innovators Forum Launched',
 'The SWE Innovators Forum was launched for SWE students.',
 '2024-09-18'),

(11, 12, 'Cholo Japan Seminar Held',
 'The Cholo Japan career path seminar was held by Daffodil IT Japan.',
 '2024-10-12'),

(12, 13, 'SWE Reached 10 Running Batches',
 'The SWE department reached 10 active running batches this year.',
 '2024-12-15');







