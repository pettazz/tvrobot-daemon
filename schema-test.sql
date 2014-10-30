

CREATE TABLE `Bobby` (
  `guid` varchar(64) NOT NULL DEFAULT '',
  `name` varchar(64) NOT NULL DEFAULT '',
  `hats` tinyint(1) NOT NULL,
  PRIMARY KEY (`guid`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


INSERT INTO Bobby (`guid`, `name`, `hats`) VALUES ('a1', 'lol', TRUE);
INSERT INTO Bobby (`guid`, `name`, `hats`) VALUES ('b2', 'rofl', FALSE);