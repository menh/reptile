CREATE TABLE IF NOT EXISTS `iask_answers` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '??ID',
  `text` text NOT NULL COMMENT '????',
  `question_id` int(18) NOT NULL COMMENT '??ID',
  `answerer` varchar(255) NOT NULL COMMENT '???',
  `date` varchar(255) NOT NULL COMMENT '????',
  `is_good` int(11) NOT NULL COMMENT '???????',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `iask_questions` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '??ID',
  `text` text NOT NULL COMMENT '????',
  `questioner` varchar(255) NOT NULL COMMENT '???',
  `date` date NOT NULL COMMENT '????',
  `ans_num` int(11) NOT NULL COMMENT '????',
  `url` varchar(255) NOT NULL COMMENT '????',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;