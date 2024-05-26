DROP TABLE IF EXISTS `event`;

CREATE TABLE `event` (
  `event_id` INTEGER PRIMARY KEY, 
  `name` TEXT NOT NULL UNIQUE, 
  `description` TEXT, 
  `date` INTEGER
)
