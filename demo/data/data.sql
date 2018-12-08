-- MySQL dump 10.13  Distrib 5.7.24, for Linux (x86_64)
--
-- Host: localhost    Database: online_social_networks
-- ------------------------------------------------------
-- Server version	5.7.24-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `weibo_user_profile`
--

DROP TABLE IF EXISTS `weibo_user_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `weibo_user_profile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `user_id` varchar(255) DEFAULT NULL,
  `weibo_num` varchar(255) DEFAULT NULL,
  `following` varchar(255) DEFAULT NULL,
  `follower` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `weibo_user_profile`
--

LOCK TABLES `weibo_user_profile` WRITE;
/*!40000 ALTER TABLE `weibo_user_profile` DISABLE KEYS */;
INSERT INTO `weibo_user_profile` VALUES
(7,'FATBIGGUY','6212090268','84','182','59'),
(8,'牛汉威','5427178881','71','273','76'),
(9,'锤子杨','3966868064','185','91','47'),
(10,'优秀搬砖民工','5599920821','44','102','16'),
(11,'工大橘子君','5754775462','5','75','34'),
(12,'李沚昕2333','5817588052','10','44','48'),
(13,'jinyan1826','5888917815','57','346','21'),(14,'南风有木','5683508732','225','174','49'),
(15,'用户6126500558','6126500558','2','46','6'),
(16,'文武之治520','3199996080','300','78','79'),(17,'抹茶味的旋宝','6266052686','16','43','11'),
(18,'黄半仙-yu','6011644949','25','163','51'),
(19,'尹夜偶晾82992','6361326368','10','91','12'),(20,'乌克丽丽_gg','6346555210','38','68','38'),(21,'秀秀秀秀媛啦','5520824066','227','293','76'),(22,'某咩_唯爱某兔','3082414677','754','140','47'),(23,'sha_3shayu','5136447737','273','99','46'),(24,'進擊de熊寶寶','5546191014','92','127','73'),(25,'落叶59464','6554154139','4','66','21'),(26,'JusDYM','5996244920','7','52','33'),(27,'pity牙医','5084870842','230','156','120'),(28,'福虎Tiger','1401215534','502','353','79'),(29,'杰西大官人','6620851812','18','88','24'),(30,'起名恐惧症患者丶','6170725650','67','156','45'),(31,'LESLIE丶余','6083112371','17','120','51'),(32,'幻想加菲猫coolgirl','5651873761','17','78','22'),(33,'这个昵称新改的','3329154322','486','52','50'),(34,'iMiyaaaa_美音','5262467572','2796','276','310'),(35,'星空6089330915','6089330915','12','178','37'),(36,'鑫海安好','6646677298','70','168','14'),(37,'二思小姑娘','5231603159','30','53','16'),(38,'月光下的凤尾竹f4','6468710777','64','33','19'),(39,'雨酔枫笙','3884358778','9','95','48'),(40,'N苏柚Y','6372350243','155','77','18'),(41,'一半糖一半伤_46098','5585673861','142','110','11'),(42,'Conver-雨','5743625535','13','279','62'),(43,'答与不答','6574167541','63','238','71'),(44,'沙丁鱼哦','5543580678','62','29','36'),(45,'纪念10月离去的你','2641472087','82','533','46'),(46,'那一朵向阳花花','3717084375','316','236','116'),(47,'殷彩鹤','6293376227','46','202','20'),(48,'雪影飞菲','5114142824','51','108','26'),(49,'腻撑2018','1855825885','9','221','40'),(50,'花落夏寂','5594064831','214','348','29'),(51,'YunWorkbench','3779064072','12','362','40'),(52,'主义一定要实现','1776824593','218','152','78'),(53,'孙笑川厨','5272362641','104','786','80'),(54,'痞子鱼儿333','6601023960','126','350','97'),(55,'夏洛特家的柯基','6086404451','69','289','26'),(56,'申蓝小哥哥','6479720209','152','106','67');
/*!40000 ALTER TABLE `weibo_user_profile` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-07 18:44:36
