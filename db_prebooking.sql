-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Aug 17, 2024 at 05:52 AM
-- Server version: 8.0.31
-- PHP Version: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_prebooking`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add tb_cart', 7, 'add_tb_cart'),
(26, 'Can change tb_cart', 7, 'change_tb_cart'),
(27, 'Can delete tb_cart', 7, 'delete_tb_cart'),
(28, 'Can view tb_cart', 7, 'view_tb_cart'),
(29, 'Can add tbl_menu', 8, 'add_tbl_menu'),
(30, 'Can change tbl_menu', 8, 'change_tbl_menu'),
(31, 'Can delete tbl_menu', 8, 'delete_tbl_menu'),
(32, 'Can view tbl_menu', 8, 'view_tbl_menu'),
(33, 'Can add tbl_order', 9, 'add_tbl_order'),
(34, 'Can change tbl_order', 9, 'change_tbl_order'),
(35, 'Can delete tbl_order', 9, 'delete_tbl_order'),
(36, 'Can view tbl_order', 9, 'view_tbl_order'),
(37, 'Can add tbl_register', 10, 'add_tbl_register'),
(38, 'Can change tbl_register', 10, 'change_tbl_register'),
(39, 'Can delete tbl_register', 10, 'delete_tbl_register'),
(40, 'Can view tbl_register', 10, 'view_tbl_register'),
(41, 'Can add tbl_restaurant', 11, 'add_tbl_restaurant'),
(42, 'Can change tbl_restaurant', 11, 'change_tbl_restaurant'),
(43, 'Can delete tbl_restaurant', 11, 'delete_tbl_restaurant'),
(44, 'Can view tbl_restaurant', 11, 'view_tbl_restaurant'),
(45, 'Can add tbl_worker', 12, 'add_tbl_worker'),
(46, 'Can change tbl_worker', 12, 'change_tbl_worker'),
(47, 'Can delete tbl_worker', 12, 'delete_tbl_worker'),
(48, 'Can view tbl_worker', 12, 'view_tbl_worker'),
(49, 'Can add tbl_worker_status', 13, 'add_tbl_worker_status'),
(50, 'Can change tbl_worker_status', 13, 'change_tbl_worker_status'),
(51, 'Can delete tbl_worker_status', 13, 'delete_tbl_worker_status'),
(52, 'Can view tbl_worker_status', 13, 'view_tbl_worker_status'),
(53, 'Can add tbl_payment', 14, 'add_tbl_payment'),
(54, 'Can change tbl_payment', 14, 'change_tbl_payment'),
(55, 'Can delete tbl_payment', 14, 'delete_tbl_payment'),
(56, 'Can view tbl_payment', 14, 'view_tbl_payment'),
(57, 'Can add tbl_menu_feedback', 15, 'add_tbl_menu_feedback'),
(58, 'Can change tbl_menu_feedback', 15, 'change_tbl_menu_feedback'),
(59, 'Can delete tbl_menu_feedback', 15, 'delete_tbl_menu_feedback'),
(60, 'Can view tbl_menu_feedback', 15, 'view_tbl_menu_feedback'),
(61, 'Can add tbl_feedback', 16, 'add_tbl_feedback'),
(62, 'Can change tbl_feedback', 16, 'change_tbl_feedback'),
(63, 'Can delete tbl_feedback', 16, 'delete_tbl_feedback'),
(64, 'Can view tbl_feedback', 16, 'view_tbl_feedback'),
(65, 'Can add tbl_booking', 17, 'add_tbl_booking'),
(66, 'Can change tbl_booking', 17, 'change_tbl_booking'),
(67, 'Can delete tbl_booking', 17, 'delete_tbl_booking'),
(68, 'Can view tbl_booking', 17, 'view_tbl_booking');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'prebookingapp', 'tb_cart'),
(8, 'prebookingapp', 'tbl_menu'),
(9, 'prebookingapp', 'tbl_order'),
(10, 'prebookingapp', 'tbl_register'),
(11, 'prebookingapp', 'tbl_restaurant'),
(12, 'prebookingapp', 'tbl_worker'),
(13, 'prebookingapp', 'tbl_worker_status'),
(14, 'prebookingapp', 'tbl_payment'),
(15, 'prebookingapp', 'tbl_menu_feedback'),
(16, 'prebookingapp', 'tbl_feedback'),
(17, 'prebookingapp', 'tbl_booking');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-08-17 04:51:00.144608'),
(2, 'auth', '0001_initial', '2024-08-17 04:51:00.791766'),
(3, 'admin', '0001_initial', '2024-08-17 04:51:01.038721'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-08-17 04:51:01.053681'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-08-17 04:51:01.071634'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-08-17 04:51:01.169371'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-08-17 04:51:01.223226'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-08-17 04:51:01.284065'),
(9, 'auth', '0004_alter_user_username_opts', '2024-08-17 04:51:01.297030'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-08-17 04:51:01.353880'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-08-17 04:51:01.356869'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-08-17 04:51:01.371911'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-08-17 04:51:01.424767'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-08-17 04:51:01.482616'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-08-17 04:51:01.532481'),
(16, 'auth', '0011_update_proxy_permissions', '2024-08-17 04:51:01.550432'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-08-17 04:51:01.604289'),
(18, 'prebookingapp', '0001_initial', '2024-08-17 04:51:02.992363'),
(19, 'sessions', '0001_initial', '2024-08-17 04:51:03.052201');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('as43g0ejg6bc31wpn45o7smokee90nwx', 'eyJpZCI6MX0:1sfCHS:prju9hOMcFUO31BhDYzNbMwZxPFILELdwsfnw6EaGR8', '2024-08-31 05:47:14.841626');

-- --------------------------------------------------------

--
-- Table structure for table `prebookingapp_tbl_booking`
--

DROP TABLE IF EXISTS `prebookingapp_tbl_booking`;
CREATE TABLE IF NOT EXISTS `prebookingapp_tbl_booking` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `time` varchar(100) NOT NULL,
  `total_guest` varchar(100) NOT NULL,
  `phn` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `items` longtext,
  `booking_status` varchar(100) NOT NULL,
  `restaurant_id_id` bigint DEFAULT NULL,
  `user_id_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `prebookingapp_tbl_booking_restaurant_id_id_83e69dba` (`restaurant_id_id`),
  KEY `prebookingapp_tbl_booking_user_id_id_7d88e3db` (`user_id_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `prebookingapp_tbl_feedback`
--

DROP TABLE IF EXISTS `prebookingapp_tbl_feedback`;
CREATE TABLE IF NOT EXISTS `prebookingapp_tbl_feedback` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `ratings` int DEFAULT NULL,
  `msg` varchar(100) NOT NULL,
  `restaurant_id_id` bigint DEFAULT NULL,
  `user_id_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `prebookingapp_tbl_feedback_restaurant_id_id_6d161c83` (`restaurant_id_id`),
  KEY `prebookingapp_tbl_feedback_user_id_id_3684cf23` (`user_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `prebookingapp_tbl_feedback`
--

INSERT INTO `prebookingapp_tbl_feedback` (`id`, `ratings`, `msg`, `restaurant_id_id`, `user_id_id`) VALUES
(1, 5, 'good ambience and food', 1, 2),
(2, 4, 'great service and quality food', 2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `prebookingapp_tbl_menu`
--

DROP TABLE IF EXISTS `prebookingapp_tbl_menu`;
CREATE TABLE IF NOT EXISTS `prebookingapp_tbl_menu` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `foodcategory` varchar(100) NOT NULL,
  `img` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `price` varchar(100) NOT NULL,
  `qnty` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `restaurant_id_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `prebookingapp_tbl_menu_restaurant_id_id_445d21a3` (`restaurant_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `prebookingapp_tbl_menu`
--

INSERT INTO `prebookingapp_tbl_menu` (`id`, `foodcategory`, `img`, `description`, `price`, `qnty`, `status`, `restaurant_id_id`) VALUES
(1, 'Buger', 'files/f2.png', 'jumbo chicken  cheese burger ', '189', '7', 'pending', 1),
(2, 'Pizza', 'files/o2_tfEDg52.jpg', 'Paneer Tikka Pizza', '250', '10', 'pending', 1),
(3, 'Biryani', 'files/chicken-biryani-recipe_JnbL8xg.jpg', 'tasty chicken biriyani', '230', '10', 'pending', 1);

-- --------------------------------------------------------

--
-- Table structure for table `prebookingapp_tbl_menu_feedback`
--

DROP TABLE IF EXISTS `prebookingapp_tbl_menu_feedback`;
CREATE TABLE IF NOT EXISTS `prebookingapp_tbl_menu_feedback` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `ratings` int DEFAULT NULL,
  `msg` varchar(100) NOT NULL,
  `menu_id_id` bigint DEFAULT NULL,
  `user_id_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `prebookingapp_tbl_menu_feedback_menu_id_id_b7eae13f` (`menu_id_id`),
  KEY `prebookingapp_tbl_menu_feedback_user_id_id_0e5f8b1b` (`user_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `prebookingapp_tbl_menu_feedback`
--

INSERT INTO `prebookingapp_tbl_menu_feedback` (`id`, `ratings`, `msg`, `menu_id_id`, `user_id_id`) VALUES
(1, 4, 'very yummy', 1, 2),
(2, 5, 'nice food', 1, 2),
(3, 4, 'very tasty', 3, 2),
(4, 4, 'very tasty', 3, 2),
(5, 4, 'gggg', 2, 2),
(6, 4, 'hhh', 2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `prebookingapp_tbl_order`
--

DROP TABLE IF EXISTS `prebookingapp_tbl_order`;
CREATE TABLE IF NOT EXISTS `prebookingapp_tbl_order` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `total` varchar(30) NOT NULL,
  `date` varchar(100) NOT NULL,
  `time` varchar(100) NOT NULL,
  `payment_status` varchar(30) NOT NULL,
  `status` varchar(30) NOT NULL,
  `order_id` varchar(100) NOT NULL,
  `cart_id_id` bigint DEFAULT NULL,
  `menu_id_id` bigint DEFAULT NULL,
  `user_id_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `prebookingapp_tbl_order_cart_id_id_60c35834` (`cart_id_id`),
  KEY `prebookingapp_tbl_order_menu_id_id_01199592` (`menu_id_id`),
  KEY `prebookingapp_tbl_order_user_id_id_0a3702eb` (`user_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `prebookingapp_tbl_order`
--

INSERT INTO `prebookingapp_tbl_order` (`id`, `total`, `date`, `time`, `payment_status`, `status`, `order_id`, `cart_id_id`, `menu_id_id`, `user_id_id`) VALUES
(1, '617', '2024-08-17', '11:15:07', 'paid', 'allocate', '254657701356955305980316428919319990423', 1, 1, 2);

-- --------------------------------------------------------

--
-- Table structure for table `prebookingapp_tbl_payment`
--

DROP TABLE IF EXISTS `prebookingapp_tbl_payment`;
CREATE TABLE IF NOT EXISTS `prebookingapp_tbl_payment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` varchar(100) NOT NULL,
  `card_name` varchar(100) NOT NULL,
  `card_number` varchar(100) NOT NULL,
  `card_date` varchar(100) NOT NULL,
  `card_cvv` varchar(100) NOT NULL,
  `pay_status` varchar(100) NOT NULL,
  `order_id_id` bigint DEFAULT NULL,
  `user_id_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `prebookingapp_tbl_payment_order_id_id_03aa3b99` (`order_id_id`),
  KEY `prebookingapp_tbl_payment_user_id_id_807d0c35` (`user_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `prebookingapp_tbl_payment`
--

INSERT INTO `prebookingapp_tbl_payment` (`id`, `date`, `card_name`, `card_number`, `card_date`, `card_cvv`, `pay_status`, `order_id_id`, `user_id_id`) VALUES
(1, '', 'ffgfs', '999999999999', '1988', '123', 'paid', 1, 2);

-- --------------------------------------------------------

--
-- Table structure for table `prebookingapp_tbl_register`
--

DROP TABLE IF EXISTS `prebookingapp_tbl_register`;
CREATE TABLE IF NOT EXISTS `prebookingapp_tbl_register` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL,
  `phn` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `pswd` varchar(100) NOT NULL,
  `adrs` varchar(100) NOT NULL,
  `plc` varchar(100) NOT NULL,
  `dob` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `utype` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `prebookingapp_tbl_register`
--

INSERT INTO `prebookingapp_tbl_register` (`id`, `email`, `phn`, `name`, `pswd`, `adrs`, `plc`, `dob`, `gender`, `utype`) VALUES
(1, 'admin@gmail.com', '', 'admin', '123', '', '', '', '', 'admin'),
(2, 'dev@gmail.com', '9876543210', 'dev', '123', 'dev abc house TVM Kerala', 'Thrissur', '2024-08-16', 'male', 'user');

-- --------------------------------------------------------

--
-- Table structure for table `prebookingapp_tbl_restaurant`
--

DROP TABLE IF EXISTS `prebookingapp_tbl_restaurant`;
CREATE TABLE IF NOT EXISTS `prebookingapp_tbl_restaurant` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL,
  `phn` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `pswd` varchar(100) NOT NULL,
  `adrs` varchar(100) NOT NULL,
  `plc` varchar(100) NOT NULL,
  `licence_number` varchar(100) NOT NULL,
  `img` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `prebookingapp_tbl_restaurant`
--

INSERT INTO `prebookingapp_tbl_restaurant` (`id`, `email`, `phn`, `name`, `pswd`, `adrs`, `plc`, `licence_number`, `img`, `status`) VALUES
(1, 'abc@gmail.com', '9876543210', 'ABC REST', '123', 'abc rest , xyz street,near gsgGFGxs 798544323 ', 'Thrissur', '7654321987', 'files/R1.jfif', 'approved'),
(2, 'mc@gmail.com', '7867564335', 'MC DONALDS', '123', 'ggahg vgvdf ggsfg stretyfwyt677888', 'Thrissur', '7865542545', 'files/r3.jpg', 'pending');

-- --------------------------------------------------------

--
-- Table structure for table `prebookingapp_tbl_worker`
--

DROP TABLE IF EXISTS `prebookingapp_tbl_worker`;
CREATE TABLE IF NOT EXISTS `prebookingapp_tbl_worker` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL,
  `phn` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `pswd` varchar(100) NOT NULL,
  `adrs` varchar(100) NOT NULL,
  `utype` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `restaurant_id_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `prebookingapp_tbl_worker_restaurant_id_id_4302c5e9` (`restaurant_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `prebookingapp_tbl_worker`
--

INSERT INTO `prebookingapp_tbl_worker` (`id`, `email`, `phn`, `name`, `pswd`, `adrs`, `utype`, `status`, `restaurant_id_id`) VALUES
(1, 'surya@gmail.com', '656778889', 'surya', '123', 'gvhagdh gfghaffd sbvv', 'worker', 'pending', 1),
(2, 'karthik@gmail.com', '656778889', 'karthik', '123', 'gvhagdh gfghaffd sbvv', 'worker', 'pending', 1);

-- --------------------------------------------------------

--
-- Table structure for table `prebookingapp_tbl_worker_status`
--

DROP TABLE IF EXISTS `prebookingapp_tbl_worker_status`;
CREATE TABLE IF NOT EXISTS `prebookingapp_tbl_worker_status` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `work_status` varchar(100) NOT NULL,
  `order_id_id` bigint DEFAULT NULL,
  `restaurant_id_id` bigint DEFAULT NULL,
  `worker_id_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `prebookingapp_tbl_worker_status_order_id_id_1d85a7d2` (`order_id_id`),
  KEY `prebookingapp_tbl_worker_status_restaurant_id_id_041f7250` (`restaurant_id_id`),
  KEY `prebookingapp_tbl_worker_status_worker_id_id_e67c52a5` (`worker_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `prebookingapp_tbl_worker_status`
--

INSERT INTO `prebookingapp_tbl_worker_status` (`id`, `work_status`, `order_id_id`, `restaurant_id_id`, `worker_id_id`) VALUES
(1, 'Allocate', 1, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `prebookingapp_tb_cart`
--

DROP TABLE IF EXISTS `prebookingapp_tb_cart`;
CREATE TABLE IF NOT EXISTS `prebookingapp_tb_cart` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `qnty` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `total_price` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `menu_id_id` bigint DEFAULT NULL,
  `user_id_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `prebookingapp_tb_cart_menu_id_id_c843f4b6` (`menu_id_id`),
  KEY `prebookingapp_tb_cart_user_id_id_ed06f7ef` (`user_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `prebookingapp_tb_cart`
--

INSERT INTO `prebookingapp_tb_cart` (`id`, `qnty`, `date`, `total_price`, `status`, `menu_id_id`, `user_id_id`) VALUES
(1, '3', '2024-08-17', '567', 'paid', 1, 2);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
