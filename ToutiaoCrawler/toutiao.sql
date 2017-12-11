# create database toutiao

CREATE TABLE `news` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `tag` varchar(255) DEFAULT NULL,
  `source` varchar(255) DEFAULT NULL,
  `source_url` varchar(255) DEFAULT NULL,
  `content` longtext,
  `keyword` varchar(255) DEFAULT NULL,
  `keywords` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7214 DEFAULT CHARSET=utf8;

