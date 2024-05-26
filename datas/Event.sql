DROP TABLE IF EXISTS `event`;

CREATE TABLE `event` (
  `id` INTEGER PRIMARY KEY, 
  `name` TEXT NOT NULL UNIQUE, 
  `description` TEXT, 
  `date` TEXT DEFAULT (datetime('now'))
)
