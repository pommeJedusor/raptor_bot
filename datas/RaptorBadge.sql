DROP TABLE IF EXISTS `raptor_badge`;

CREATE TABLE `raptor_badge` (
  `raptor_badge_id` INTEGER PRIMARY KEY, 
  `description` TEXT NOT NULL, 
  `owner_id` INTEGER,
  `date` INTEGER DEFAULT (UNIXEPOCH())
);
