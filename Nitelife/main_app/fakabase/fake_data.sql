
-- 1.create the database named nitelife
-- 2.connect to the nitelife database
-- 3.copy below code and paste into terminal
-- 4.run command to create table named event
-- 5.uncomment the insert commands below

-- CREATE TABLE IF NOT EXISTS event (
-- ID serial NOT NULL PRIMARY KEY,
-- creator (party host) INT serial NOT NULL, <-- fk for user who created the event
-- title VARCHAR(255) DEFAULT NULL,
-- location VARCHAR(255) DEFAULT NULL,
-- bio (description) VARCHAR(255) DEFAULT NULL,
-- image BYTEA DEFAULT NULL, <-- may need diffrent data type
-- guest INT serial NOT NULL, <-- fk for users attending
-- created_at TIMESTAMP DEFAULT CURRENT,
-- );

-- INSERT INTO `event` (`creator`, `title`, `location`, `bio`, `image`, `created_at`) 
-- VALUES 
-- ( 1, 'Prom', 'Subways', 'Come have the night of your life! Plus all you can eat foot longs!', 'https://live.staticflickr.com/1586/25124783374_1bccab8593_b.jpg', '2021-05-07 18:57:42.517205-07'
-- )

-- INSERT INTO `event` (`creator`, `title`, `location`, `bio`, `image`, `created_at`) 
-- VALUES 
-- ( 2, 'YATCH PARTY!', 'TheSuperYatchClub', 'Come have the night of your life! Plus all you can snort cocaine!', 'https://i.insider.com/58a1cc4cdd0895dc6e8b4cb2?width=1190', '2021-05-07 18:57:42.517205-07'
-- )
