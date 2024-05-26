DROP TABLE IF EXISTS `raptor_badge`;

CREATE TABLE `raptor_badge` (
  `id` INTEGER PRIMARY KEY, 
  `description` TEXT NOT NULL, 
  `owner_id` INTEGER NOT NULL,
  `event_id` INTEGER NOT NULL,
  `date` INTEGER DEFAULT (UNIXEPOCH()) NOT NULL
);
