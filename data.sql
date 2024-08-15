-- PRAGMA foreign_keys=OFF;
START TRANSACTION;
CREATE TABLE IF NOT EXISTS django_migrations (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    app VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    applied DATETIME NOT NULL
);
INSERT INTO django_migrations VALUES(1,'contenttypes','0001_initial','2023-10-16 23:04:29.440815');
INSERT INTO django_migrations VALUES(2,'auth','0001_initial','2023-10-16 23:04:29.459464');
INSERT INTO django_migrations VALUES(3,'admin','0001_initial','2023-10-16 23:04:29.471280');
INSERT INTO django_migrations VALUES(4,'admin','0002_logentry_remove_auto_add','2023-10-16 23:04:29.484021');
INSERT INTO django_migrations VALUES(5,'admin','0003_logentry_add_action_flag_choices','2023-10-16 23:04:29.490897');
INSERT INTO django_migrations VALUES(6,'contenttypes','0002_remove_content_type_name','2023-10-16 23:04:29.509680');
INSERT INTO django_migrations VALUES(7,'auth','0002_alter_permission_name_max_length','2023-10-16 23:04:29.521325');
INSERT INTO django_migrations VALUES(8,'auth','0003_alter_user_email_max_length','2023-10-16 23:04:29.532437');
INSERT INTO django_migrations VALUES(9,'auth','0004_alter_user_username_opts','2023-10-16 23:04:29.540986');
INSERT INTO django_migrations VALUES(10,'auth','0005_alter_user_last_login_null','2023-10-16 23:04:29.552414');
INSERT INTO django_migrations VALUES(11,'auth','0006_require_contenttypes_0002','2023-10-16 23:04:29.554305');
INSERT INTO django_migrations VALUES(12,'auth','0007_alter_validators_add_error_messages','2023-10-16 23:04:29.561675');
INSERT INTO django_migrations VALUES(13,'auth','0008_alter_user_username_max_length','2023-10-16 23:04:29.575540');
INSERT INTO django_migrations VALUES(14,'auth','0009_alter_user_last_name_max_length','2023-10-16 23:04:29.591399');
INSERT INTO django_migrations VALUES(15,'auth','0010_alter_group_name_max_length','2023-10-16 23:04:29.604039');
INSERT INTO django_migrations VALUES(16,'auth','0011_update_proxy_permissions','2023-10-16 23:04:29.613486');
INSERT INTO django_migrations VALUES(17,'auth','0012_alter_user_first_name_max_length','2023-10-16 23:04:29.624837');
INSERT INTO django_migrations VALUES(18,'sessions','0001_initial','2023-10-16 23:04:29.632744');
INSERT INTO django_migrations VALUES(24,'gigsweep_django_backend','0001_initial','2024-01-31 16:14:36.974590');
INSERT INTO django_migrations VALUES(25,'gigsweep_django_backend','0002_chatmessage','2024-01-31 16:14:36.986425');
INSERT INTO django_migrations VALUES(26,'gigsweep_django_backend','0003_delete_chatmessage','2024-01-31 16:14:36.988794');
INSERT INTO django_migrations VALUES(27,'gigsweep_django_backend','0004_chatmessage','2024-01-31 16:14:37.001470');
INSERT INTO django_migrations VALUES(28,'gigsweep_django_backend','0005_artist_upcoming_gigs','2024-01-31 16:14:37.008459');
INSERT INTO django_migrations VALUES(29,'gigsweep_django_backend','0006_delete_chatmessage','2024-01-31 16:20:34.875352');
INSERT INTO django_migrations VALUES(30,'gigsweep_django_backend','0007_rename_image_venue_profile_picture','2024-02-03 01:16:32.386711');
INSERT INTO django_migrations VALUES(31,'gigsweep_django_backend','0008_rename_profile_picture_venue_image','2024-02-03 01:39:00.220421');
INSERT INTO django_migrations VALUES(32,'gigsweep_django_backend','0009_alter_artist_email_alter_artist_password','2024-03-10 01:23:46.455253');
INSERT INTO django_migrations VALUES(33,'gigsweep_django_backend','0010_artistlistedgig_status','2024-03-15 01:42:16.302458');
INSERT INTO django_migrations VALUES(34,'gigsweep_django_backend','0011_alter_artist_artist_name','2024-03-21 01:49:10.019869');
INSERT INTO django_migrations VALUES(35,'gigsweep_django_backend','0012_alter_venue_email_alter_venue_password_and_more','2024-03-25 01:29:06.594613');
INSERT INTO django_migrations VALUES(36,'gigsweep_django_backend','0013_artistgigapplication_message_and_more','2024-06-28 21:36:15.391735');
INSERT INTO django_migrations VALUES(37,'gigsweep_django_backend','0014_alter_artistgigapplication_artist_and_more','2024-06-28 22:00:14.599951');
INSERT INTO django_migrations VALUES(38,'gigsweep_django_backend','0015_artistlistedgig_venue','2024-06-29 00:18:44.177982');
INSERT INTO django_migrations VALUES(39,'gigsweep_django_backend','0016_remove_artistlistedgig_venue_and_more','2024-06-29 01:39:21.255066');
INSERT INTO django_migrations VALUES(40,'gigsweep_django_backend','0017_alter_artistgigapplication_status','2024-06-29 01:48:31.167684');
INSERT INTO django_migrations VALUES(41,'gigsweep_django_backend','0018_artistlistedgig_venue','2024-07-01 01:50:00.617915');
INSERT INTO django_migrations VALUES(42,'gigsweep_django_backend','0019_rename_venue_artistlistedgig_venue_id','2024-07-01 01:57:27.247054');
INSERT INTO django_migrations VALUES(43,'gigsweep_django_backend','0020_rename_venue_id_artistlistedgig_venue','2024-07-02 02:08:53.363226');
INSERT INTO django_migrations VALUES(44,'gigsweep_django_backend','0021_venuenotification_artistnotification','2024-07-12 23:23:17.820191');
INSERT INTO django_migrations VALUES(45,'gigsweep_django_backend','0022_remove_artistlistedgig_venue_name','2024-07-13 00:15:09.099234');
INSERT INTO django_migrations VALUES(46,'gigsweep_django_backend','0023_artistlistedgig_venue_name','2024-07-13 01:27:25.915623');
INSERT INTO django_migrations VALUES(47,'gigsweep_django_backend','0024_rename_venue_artistlistedgig_venue_id','2024-07-13 01:30:46.241471');
INSERT INTO django_migrations VALUES(48,'gigsweep_django_backend','0025_rename_venue_id_artistlistedgig_venue','2024-07-13 01:32:28.665861');
INSERT INTO django_migrations VALUES(49,'gigsweep_django_backend','0026_alter_artistlistedgig_status','2024-07-13 01:37:12.397848');
INSERT INTO django_migrations VALUES(50,'gigsweep_django_backend','0027_venuenotification_notification_type','2024-07-16 01:27:12.070351');
INSERT INTO django_migrations VALUES(51,'gigsweep_django_backend','0028_alter_venuenotification_notification_type','2024-07-16 01:27:12.079435');
INSERT INTO django_migrations VALUES(52,'gigsweep_django_backend','0029_alter_venuenotification_notification_type','2024-07-17 16:05:07.275753');
INSERT INTO django_migrations VALUES(53,'gigsweep_django_backend','0030_venuenotification_if_artist_listed_gig','2024-07-17 16:29:35.127075');
INSERT INTO django_migrations VALUES(54,'gigsweep_django_backend','0031_rename_if_artist_listed_gig_venuenotification_if_gig_advertised_by_artist_and_more','2024-07-17 16:36:00.499105');
INSERT INTO django_migrations VALUES(55,'gigsweep_django_backend','0032_venuenotification_if_artist_gig_application_id','2024-07-17 18:32:39.592365');
INSERT INTO django_migrations VALUES(56,'gigsweep_django_backend','0033_remove_venuenotification_if_artist_gig_application_id_and_more','2024-07-20 00:49:16.556740');
CREATE TABLE IF NOT EXISTS auth_group_permissions (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    group_id INT NOT NULL,
    permission_id INT NOT NULL,
    FOREIGN KEY (group_id) REFERENCES auth_group(id),
    FOREIGN KEY (permission_id) REFERENCES auth_permission(id)
);
CREATE TABLE IF NOT EXISTS auth_user_groups (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    group_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES auth_user(id),
    FOREIGN KEY (group_id) REFERENCES auth_group(id)
);
CREATE TABLE IF NOT EXISTS auth_user_user_permissions (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    permission_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES auth_user(id),
    FOREIGN KEY (permission_id) REFERENCES auth_permission(id)
);
CREATE TABLE IF NOT EXISTS django_admin_log (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    object_id TEXT NULL,
    object_repr VARCHAR(200) NOT NULL,
    action_flag SMALLINT UNSIGNED NOT NULL,
    change_message TEXT NOT NULL,
    content_type_id INT NULL,
    user_id INT NOT NULL,
    action_time DATETIME NOT NULL,
    FOREIGN KEY (content_type_id) REFERENCES django_content_type(id),
    FOREIGN KEY (user_id) REFERENCES auth_user(id)
);
INSERT INTO django_admin_log VALUES(1,'1','Artist - GigSweep Standard',1,'[{"added": {}}]',13,1,'2023-10-17 23:36:02.902372');
INSERT INTO django_admin_log VALUES(2,'2','Venue - GigSweep Standard',1,'[{"added": {}}]',13,1,'2023-10-17 23:36:37.983633');
INSERT INTO django_admin_log VALUES(3,'3','Artist - GigSweep Pro',1,'[{"added": {}}]',13,1,'2023-10-17 23:37:45.814028');
INSERT INTO django_admin_log VALUES(4,'4','Venue - GigSweep Pro',1,'[{"added": {}}]',13,1,'2023-10-17 23:38:25.991809');
INSERT INTO django_admin_log VALUES(5,'2','The Struts',2,'[{"changed": {"fields": ["Phone number", "User type", "Image", "Artist membership type"]}}]',7,1,'2023-10-18 01:03:21.016539');
INSERT INTO django_admin_log VALUES(6,'3','Those Damn Crows',2,'[{"changed": {"fields": ["Phone number", "User type", "Image", "Artist membership type"]}}]',7,1,'2023-10-18 01:04:29.772857');
INSERT INTO django_admin_log VALUES(7,'20','Keane',2,'[{"changed": {"fields": ["Phone number", "User type", "Image", "Artist membership type"]}}]',7,1,'2023-10-18 01:05:49.319606');
INSERT INTO django_admin_log VALUES(8,'22','Keane',1,'[{"added": {}}]',7,1,'2023-10-18 16:25:08.196056');
INSERT INTO django_admin_log VALUES(9,'20','Keane',3,'',7,1,'2023-10-18 16:25:20.355195');
INSERT INTO django_admin_log VALUES(10,'1','Cancel The Transmission',2,'[{"changed": {"fields": ["Image"]}}]',7,1,'2024-01-04 00:39:16.411300');
INSERT INTO django_admin_log VALUES(11,'2','The Struts',2,'[{"changed": {"fields": ["Image"]}}]',7,1,'2024-01-08 00:24:15.184724');
INSERT INTO django_admin_log VALUES(12,'3','Those Damn Crows',2,'[{"changed": {"fields": ["Image"]}}]',7,1,'2024-01-08 00:25:12.818114');
INSERT INTO django_admin_log VALUES(13,'22','Keane',2,'[{"changed": {"fields": ["Image"]}}]',7,1,'2024-01-08 00:25:43.617826');
INSERT INTO django_admin_log VALUES(14,'1','Cancel The Transmission',2,'[{"changed": {"fields": ["Image"]}}]',7,1,'2024-01-08 00:28:07.683970');
INSERT INTO django_admin_log VALUES(15,'1','Cancel The Transmission - None',1,'[{"added": {}}]',18,1,'2024-01-09 01:20:55.275134');
INSERT INTO django_admin_log VALUES(16,'1','Cancel The Transmission - None',2,'[{"changed": {"fields": ["Receiver object id"]}}]',18,1,'2024-01-09 01:21:10.969544');
INSERT INTO django_admin_log VALUES(17,'1','Cancel The Transmission - None',2,'[{"changed": {"fields": ["Receiver object id"]}}]',18,1,'2024-01-09 01:21:17.621264');
INSERT INTO django_admin_log VALUES(18,'1','Cancel The Transmission - None',2,'[]',18,1,'2024-01-09 01:23:05.554224');
INSERT INTO django_admin_log VALUES(19,'1','The Dolls House',1,'[{"added": {}}]',9,1,'2024-01-09 01:25:30.111209');
INSERT INTO django_admin_log VALUES(20,'1','Cancel The Transmission - The Dolls House',2,'[{"changed": {"fields": ["Receiver object id"]}}]',18,1,'2024-01-09 01:25:38.710215');
INSERT INTO django_admin_log VALUES(21,'1','The Dolls House',2,'[{"changed": {"fields": ["Email"]}}]',9,1,'2024-01-15 23:28:39.586822');
INSERT INTO django_admin_log VALUES(22,'1','Cancel The Transmission',2,'[{"changed": {"fields": ["Upcoming gigs"]}}]',7,1,'2024-01-15 23:59:15.405079');
INSERT INTO django_admin_log VALUES(23,'1','Cancel The Transmission',2,'[{"changed": {"fields": ["Image"]}}]',7,1,'2024-01-16 23:29:01.717690');
INSERT INTO django_admin_log VALUES(24,'1','Cancel The Transmission',2,'[{"changed": {"fields": ["Image"]}}]',7,1,'2024-01-17 01:08:32.201310');
INSERT INTO django_admin_log VALUES(25,'1','Cancel The Transmission',2,'[{"changed": {"fields": ["Email"]}}]',7,1,'2024-01-26 02:34:37.888919');
INSERT INTO django_admin_log VALUES(26,'1','Cancel The Transmission',2,'[{"changed": {"fields": ["Email"]}}]',7,1,'2024-01-26 02:36:25.142012');
INSERT INTO django_admin_log VALUES(27,'1','Cancel The Transmission',2,'[]',7,1,'2024-01-26 03:06:39.845179');
INSERT INTO django_admin_log VALUES(28,'1','yvgubhn',1,'[{"added": {}}]',7,1,'2024-01-31 16:16:54.813325');
INSERT INTO django_admin_log VALUES(29,'1','yvgubhn',3,'',7,1,'2024-01-31 16:17:38.860503');
INSERT INTO django_admin_log VALUES(30,'2','Cancel The Transmission',1,'[{"added": {}}]',7,1,'2024-01-31 16:25:11.089692');
INSERT INTO django_admin_log VALUES(31,'1','The Dolls House',1,'[{"added": {}}]',9,1,'2024-01-31 16:36:26.107372');
INSERT INTO django_admin_log VALUES(32,'2','tcfyvgubh',1,'[{"added": {}}]',9,1,'2024-01-31 16:37:19.103136');
INSERT INTO django_admin_log VALUES(33,'2','tcfyvgubh',3,'',9,1,'2024-01-31 16:37:24.551402');
INSERT INTO django_admin_log VALUES(34,'3','App Venue',3,'',9,1,'2024-01-31 18:15:20.399198');
INSERT INTO django_admin_log VALUES(35,'7','App artist',3,'',7,1,'2024-02-02 01:36:52.725016');
INSERT INTO django_admin_log VALUES(36,'6','App artist',3,'',7,1,'2024-02-02 01:36:52.730686');
INSERT INTO django_admin_log VALUES(37,'5','App artist',3,'',7,1,'2024-02-02 01:36:52.732212');
INSERT INTO django_admin_log VALUES(38,'4','App artist',3,'',7,1,'2024-02-02 01:36:52.733756');
INSERT INTO django_admin_log VALUES(39,'9','Ertcvybu',3,'',9,1,'2024-02-02 23:44:27.607960');
INSERT INTO django_admin_log VALUES(40,'13','Tcfbvygh',3,'',9,1,'2024-02-03 01:25:27.304847');
INSERT INTO django_admin_log VALUES(41,'12','Tcfbvygh',3,'',9,1,'2024-02-03 01:25:27.309553');
INSERT INTO django_admin_log VALUES(42,'11','Rvygbuhn',3,'',9,1,'2024-02-03 01:25:27.311733');
INSERT INTO django_admin_log VALUES(43,'10','Tcfyvgbhjnk',3,'',9,1,'2024-02-03 01:25:27.313148');
INSERT INTO django_admin_log VALUES(44,'8','Xcvybguhnrt',3,'',9,1,'2024-02-03 01:25:27.314587');
INSERT INTO django_admin_log VALUES(45,'7','Xcvybguhnrt',3,'',9,1,'2024-02-03 01:25:27.316061');
INSERT INTO django_admin_log VALUES(46,'6','Test venue',3,'',9,1,'2024-02-03 01:25:27.317475');
INSERT INTO django_admin_log VALUES(47,'5','Test venue',3,'',9,1,'2024-02-03 01:25:27.319102');
INSERT INTO django_admin_log VALUES(48,'4','Tcfyvgubhyuhbgv',3,'',9,1,'2024-02-03 01:25:27.320446');
INSERT INTO django_admin_log VALUES(49,'16','Tcfbvygh',3,'',9,1,'2024-02-03 01:39:22.172897');
INSERT INTO django_admin_log VALUES(50,'15','Tcfbvygh',3,'',9,1,'2024-02-03 01:39:22.178872');
INSERT INTO django_admin_log VALUES(51,'14','Tcfbvygh',3,'',9,1,'2024-02-03 01:39:22.180400');
INSERT INTO django_admin_log VALUES(52,'1','Artist - Standard',1,'[{"added": {}}]',13,1,'2024-02-03 01:50:11.644916');
INSERT INTO django_admin_log VALUES(53,'2','Venue - Standard',1,'[{"added": {}}]',13,1,'2024-02-03 01:51:30.322209');
INSERT INTO django_admin_log VALUES(54,'3','Artist - Pro',1,'[{"added": {}}]',13,1,'2024-02-03 01:52:40.404821');
INSERT INTO django_admin_log VALUES(55,'4','Venue - Pro',1,'[{"added": {}}]',13,1,'2024-02-03 01:53:38.478672');
INSERT INTO django_admin_log VALUES(56,'17','Tugging',3,'',9,1,'2024-02-04 01:45:42.374281');
INSERT INTO django_admin_log VALUES(57,'50','Tvytbuhnim',3,'',7,1,'2024-02-06 01:13:27.089276');
INSERT INTO django_admin_log VALUES(58,'49','Tcvybuhinj',3,'',7,1,'2024-02-06 01:13:27.099471');
INSERT INTO django_admin_log VALUES(59,'48','Xyvgbuhn',3,'',7,1,'2024-02-06 01:13:27.101005');
INSERT INTO django_admin_log VALUES(60,'47','Xcvfygbuhnijmt',3,'',7,1,'2024-02-06 01:13:27.102639');
INSERT INTO django_admin_log VALUES(61,'46','Rfjctvygbuhni',3,'',7,1,'2024-02-06 01:13:27.104419');
INSERT INTO django_admin_log VALUES(62,'45','Xtcgubhinjomfyv',3,'',7,1,'2024-02-06 01:13:27.106519');
INSERT INTO django_admin_log VALUES(63,'44','Ctubnyv',3,'',7,1,'2024-02-06 01:13:27.108408');
INSERT INTO django_admin_log VALUES(64,'43','Xrdctfvygbhn',3,'',7,1,'2024-02-06 01:13:27.109806');
INSERT INTO django_admin_log VALUES(65,'42','Rxctvybu',3,'',7,1,'2024-02-06 01:13:27.111175');
INSERT INTO django_admin_log VALUES(66,'41','Rctfbuhnj',3,'',7,1,'2024-02-06 01:13:27.112568');
INSERT INTO django_admin_log VALUES(67,'40','Rxctbvyu',3,'',7,1,'2024-02-06 01:13:27.114367');
INSERT INTO django_admin_log VALUES(68,'39','Rxctbvyu',3,'',7,1,'2024-02-06 01:13:27.116616');
INSERT INTO django_admin_log VALUES(69,'38','Rxctbvyu',3,'',7,1,'2024-02-06 01:13:27.118106');
INSERT INTO django_admin_log VALUES(70,'37','Rxctbvyu',3,'',7,1,'2024-02-06 01:13:27.119311');
INSERT INTO django_admin_log VALUES(71,'36','Rxctbvyu',3,'',7,1,'2024-02-06 01:13:27.120606');
INSERT INTO django_admin_log VALUES(72,'35','Ecbtvyguhn',3,'',7,1,'2024-02-06 01:13:27.122031');
INSERT INTO django_admin_log VALUES(73,'34','Xctvybguhn',3,'',7,1,'2024-02-06 01:13:27.123504');
INSERT INTO django_admin_log VALUES(74,'33','Thinhjm',3,'',7,1,'2024-02-06 01:13:27.124875');
INSERT INTO django_admin_log VALUES(75,'32','Thinhjm',3,'',7,1,'2024-02-06 01:13:27.126132');
INSERT INTO django_admin_log VALUES(76,'31','Thinhjm',3,'',7,1,'2024-02-06 01:13:27.127427');
INSERT INTO django_admin_log VALUES(77,'30','Thinhjm',3,'',7,1,'2024-02-06 01:13:27.128708');
INSERT INTO django_admin_log VALUES(78,'29','Rxrvygbuhn',3,'',7,1,'2024-02-06 01:13:27.129946');
INSERT INTO django_admin_log VALUES(79,'28','Dtfcvygubhinj',3,'',7,1,'2024-02-06 01:13:27.131226');
INSERT INTO django_admin_log VALUES(80,'27','Trcvybguhn',3,'',7,1,'2024-02-06 01:13:27.132744');
INSERT INTO django_admin_log VALUES(81,'26','Rtvgbuhn',3,'',7,1,'2024-02-06 01:13:27.134123');
INSERT INTO django_admin_log VALUES(82,'25','Cvbtyunim',3,'',7,1,'2024-02-06 01:13:27.135274');
INSERT INTO django_admin_log VALUES(83,'24','Tyvtubinjm',3,'',7,1,'2024-02-06 01:13:27.136572');
INSERT INTO django_admin_log VALUES(84,'23','Rtcgbuhinj',3,'',7,1,'2024-02-06 01:13:27.138331');
INSERT INTO django_admin_log VALUES(85,'22','Rtcgbuhinj',3,'',7,1,'2024-02-06 01:13:27.139827');
INSERT INTO django_admin_log VALUES(86,'21','Rtcgbuhinj',3,'',7,1,'2024-02-06 01:13:27.141174');
INSERT INTO django_admin_log VALUES(87,'20','Tvygubhinj',3,'',7,1,'2024-02-06 01:13:27.142463');
INSERT INTO django_admin_log VALUES(88,'19','Tyubhijnmkv',3,'',7,1,'2024-02-06 01:13:27.143726');
INSERT INTO django_admin_log VALUES(89,'18','Rtcfvygbuhinjm',3,'',7,1,'2024-02-06 01:13:27.144981');
INSERT INTO django_admin_log VALUES(90,'17','Ctbyvuhinj',3,'',7,1,'2024-02-06 01:13:27.146251');
INSERT INTO django_admin_log VALUES(91,'16','Tynjkvgbuh',3,'',7,1,'2024-02-06 01:13:27.147649');
INSERT INTO django_admin_log VALUES(92,'15','Ctgyvubhnj',3,'',7,1,'2024-02-06 01:13:27.149139');
INSERT INTO django_admin_log VALUES(93,'14','Tyvgubhnjk',3,'',7,1,'2024-02-06 01:13:27.150541');
INSERT INTO django_admin_log VALUES(94,'13','Tubhn',3,'',7,1,'2024-02-06 01:13:27.151757');
INSERT INTO django_admin_log VALUES(95,'12','Test Artist',3,'',7,1,'2024-02-06 01:13:27.153015');
INSERT INTO django_admin_log VALUES(96,'11','Tvfygbuhn',3,'',7,1,'2024-02-06 01:13:27.154972');
INSERT INTO django_admin_log VALUES(97,'10','Cygbhu',3,'',7,1,'2024-02-06 01:13:27.156473');
INSERT INTO django_admin_log VALUES(98,'9','Cygbhu',3,'',7,1,'2024-02-06 01:13:27.157703');
INSERT INTO django_admin_log VALUES(99,'8','App artist',3,'',7,1,'2024-02-06 01:13:27.158942');
INSERT INTO django_admin_log VALUES(100,'3','App artist',3,'',7,1,'2024-02-06 01:13:27.160272');
INSERT INTO django_admin_log VALUES(101,'53','Xctvybun',3,'',7,1,'2024-02-06 22:54:35.498568');
INSERT INTO django_admin_log VALUES(102,'52','Tchyvubin',3,'',7,1,'2024-02-06 22:54:35.509653');
INSERT INTO django_admin_log VALUES(103,'54','Keane',1,'[{"added": {}}]',7,1,'2024-02-06 23:10:39.395022');
INSERT INTO django_admin_log VALUES(104,'55','The Struts',1,'[{"added": {}}]',7,1,'2024-02-06 23:16:12.102172');
INSERT INTO django_admin_log VALUES(105,'56','Those Damn Crows',1,'[{"added": {}}]',7,1,'2024-02-06 23:21:34.331075');
INSERT INTO django_admin_log VALUES(106,'2','Joshua.thomas98@hotmail.co.uk',3,'',12,1,'2024-02-07 01:10:28.045066');
INSERT INTO django_admin_log VALUES(107,'1','Joshua.thomas98@hotmail.co.uk',3,'',12,1,'2024-02-07 01:10:28.052440');
INSERT INTO django_admin_log VALUES(108,'57','Rob Is Gay',1,'[{"added": {}}]',7,1,'2024-02-07 21:48:03.811879');
INSERT INTO django_admin_log VALUES(109,'4','robisgay@gmail.com',3,'',12,1,'2024-02-07 23:08:48.093401');
INSERT INTO django_admin_log VALUES(110,'57','Rob Is Gay',3,'',7,1,'2024-02-08 00:07:06.235950');
INSERT INTO django_admin_log VALUES(111,'9','cancelthetransmissionuk@outlook.com',3,'',12,1,'2024-02-08 00:25:40.351520');
INSERT INTO django_admin_log VALUES(112,'8','cancelthetransmissionuk@outlook.com',3,'',12,1,'2024-02-08 00:25:40.360897');
INSERT INTO django_admin_log VALUES(113,'7','cancelthetransmissionuk@outlook.com',3,'',12,1,'2024-02-08 00:25:40.362346');
INSERT INTO django_admin_log VALUES(114,'6','cancelthetransmissionuk@outlook.com',3,'',12,1,'2024-02-08 00:25:40.363568');
INSERT INTO django_admin_log VALUES(115,'5','cancelthetransmissionuk@outlook.com',3,'',12,1,'2024-02-08 00:25:40.365752');
INSERT INTO django_admin_log VALUES(116,'11','cancelthetransmissionuk@outlook.com',3,'',12,1,'2024-02-08 00:31:11.081110');
INSERT INTO django_admin_log VALUES(117,'10','cancelthetransmissionuk@outlook.com',3,'',12,1,'2024-02-08 00:31:11.086877');
INSERT INTO django_admin_log VALUES(118,'2','Cancel The Transmission',2,'[{"changed": {"fields": ["Summary", "Image"]}}]',7,1,'2024-02-10 02:12:50.625521');
INSERT INTO django_admin_log VALUES(119,'2','Cancel The Transmission',2,'[{"changed": {"fields": ["Image"]}}]',7,1,'2024-02-10 02:23:26.501567');
INSERT INTO django_admin_log VALUES(120,'2','Cancel The Transmission',2,'[{"changed": {"fields": ["Image"]}}]',7,1,'2024-02-10 02:23:58.522216');
INSERT INTO django_admin_log VALUES(121,'2','Cancel The Transmission',2,'[{"changed": {"fields": ["Bio", "Summary"]}}]',7,1,'2024-02-13 00:14:50.910415');
INSERT INTO django_admin_log VALUES(122,'1','Cancel The Transmission - 2024-02-28',1,'[{"added": {}}]',8,1,'2024-02-24 01:44:39.979085');
INSERT INTO django_admin_log VALUES(123,'2','Cancel The Transmissionyhjngvjbk',2,'[{"changed": {"fields": ["Email"]}}]',7,1,'2024-03-08 01:01:54.054183');
INSERT INTO django_admin_log VALUES(124,'2','Cancel The Transmission',2,'[{"changed": {"fields": ["Artist name", "Password"]}}]',7,1,'2024-03-08 01:02:10.359442');
INSERT INTO django_admin_log VALUES(125,'2','Cancel The Transmissionnnnn',2,'[{"changed": {"fields": ["Email", "Password", "Phone number", "Bio", "Summary", "Genre", "Country", "County", "Image"]}}]',7,1,'2024-03-10 01:35:55.081194');
INSERT INTO django_admin_log VALUES(126,'2','Cancel The Transmission',2,'[{"changed": {"fields": ["Email", "Bio"]}}]',7,1,'2024-03-10 01:42:30.731981');
INSERT INTO django_admin_log VALUES(127,'2','Cancel The Transmission',2,'[{"changed": {"fields": ["Email"]}}]',7,1,'2024-03-10 01:43:23.211803');
INSERT INTO django_admin_log VALUES(128,'2','Cancel The Transmission',2,'[{"changed": {"fields": ["Artist name"]}}]',7,1,'2024-03-10 01:46:45.717264');
INSERT INTO django_admin_log VALUES(129,'1','Cancel The Transmission - The Patriot - 20 Apr 2024',1,'[{"added": {}}]',10,1,'2024-03-15 00:02:49.518057');
INSERT INTO django_admin_log VALUES(130,'1','Cancel The Transmission - The Patriot - 20 Apr 2024',2,'[{"changed": {"fields": ["Status"]}}]',10,1,'2024-03-15 01:42:38.720418');
INSERT INTO django_admin_log VALUES(131,'2','Cancel The Transmission - The Dolls House - 25 Apr 2024',1,'[{"added": {}}]',10,1,'2024-03-16 00:42:30.040947');
INSERT INTO django_admin_log VALUES(132,'3','Cancel The Transmission - Llangewydd Arms - 04 May 2024',1,'[{"added": {}}]',10,1,'2024-03-16 00:53:23.482886');
INSERT INTO django_admin_log VALUES(133,'6','Cancel The Transmission - Bedwas RFC - 12 Jun 2024',3,'',10,1,'2024-03-17 02:23:58.066337');
INSERT INTO django_admin_log VALUES(134,'5','Cancel The Transmission - Bedwas RFC - 12 Jun 2024',3,'',10,1,'2024-03-17 02:23:58.072416');
INSERT INTO django_admin_log VALUES(135,'4','Cancel The Transmission - Bedwas RFC - 12 Jun 2024',3,'',10,1,'2024-03-17 02:23:58.073984');
INSERT INTO django_admin_log VALUES(136,'7','Cancel The Transmission - Bedwas RFC - 12 Jun 2024',2,'[{"changed": {"fields": ["Type of artist", "Description", "Status"]}}]',10,1,'2024-03-17 02:24:57.826318');
INSERT INTO django_admin_log VALUES(137,'7','Cancel The Transmission - Bedwas RFC - 12 Jun 2024',3,'',10,1,'2024-03-17 02:27:44.339639');
INSERT INTO django_admin_log VALUES(138,'8','Cancel The Transmission - Bedwas RFC - 06 Jun 2024',3,'',10,1,'2024-03-17 02:32:13.796935');
INSERT INTO django_admin_log VALUES(139,'10','Cancel The Transmission - ,howhjh - 24 Jun 2024',2,'[{"changed": {"fields": ["Status"]}}]',10,1,'2024-03-18 03:45:25.503047');
INSERT INTO django_admin_log VALUES(140,'2','Cancel The Transmission',2,'[{"changed": {"fields": ["Password"]}}]',7,1,'2024-03-21 01:50:18.764686');
INSERT INTO django_admin_log VALUES(141,'11','Cancel The Transmission - Taffs Well RFC - 13 Apr 2024',1,'[{"added": {}}]',10,1,'2024-03-30 01:00:34.201857');
INSERT INTO django_admin_log VALUES(142,'12','Cancel The Transmission - The Leigh - 20 Apr 2024',1,'[{"added": {}}]',10,1,'2024-03-30 01:05:29.975981');
INSERT INTO django_admin_log VALUES(143,'13','Cancel The Transmission - yvubhn - 20 Apr 2024',1,'[{"added": {}}]',10,1,'2024-03-30 01:15:38.233836');
INSERT INTO django_admin_log VALUES(144,'14','Cancel The Transmission - tfyguhijn - 20 Apr 2024',1,'[{"added": {}}]',10,1,'2024-03-30 01:17:38.387901');
INSERT INTO django_admin_log VALUES(145,'15','Cancel The Transmission - fghvbjn - 20 Apr 2024',1,'[{"added": {}}]',10,1,'2024-03-30 01:23:42.662614');
INSERT INTO django_admin_log VALUES(146,'16','Cancel The Transmission - fyvgbhnj - 06 Apr 2024',1,'[{"added": {}}]',10,1,'2024-04-02 01:33:51.979898');
INSERT INTO django_admin_log VALUES(147,'17','Cancel The Transmission - Jacs - 04 Apr 2024',1,'[{"added": {}}]',10,1,'2024-05-10 00:54:29.543073');
INSERT INTO django_admin_log VALUES(148,'3','Artist - Pro',2,'[{"changed": {"fields": ["Description"]}}]',13,1,'2024-06-21 13:11:31.681279');
INSERT INTO django_admin_log VALUES(149,'3','Artist - Pro',2,'[{"changed": {"fields": ["Description"]}}]',13,1,'2024-06-21 13:12:43.761224');
INSERT INTO django_admin_log VALUES(150,'4','Venue - Pro',2,'[{"changed": {"fields": ["Description"]}}]',13,1,'2024-06-21 13:13:10.623677');
INSERT INTO django_admin_log VALUES(151,'18','Those Damn Crows - Bedwas RFC - 24 Jun 2024',1,'[{"added": {}}]',10,1,'2024-06-22 15:34:57.259603');
INSERT INTO django_admin_log VALUES(152,'18','Those Damn Crows - Bedwas RFC - 24 Jun 2024',2,'[{"changed": {"fields": ["Description"]}}]',10,1,'2024-06-22 15:47:21.877353');
INSERT INTO django_admin_log VALUES(153,'1','Cancel The Transmission applied for Those Damn Crows - Bedwas RFC - 24 Jun 2024',3,'',16,1,'2024-06-23 16:59:26.416043');
INSERT INTO django_admin_log VALUES(154,'3','Cancel The Transmission applied for Those Damn Crows - Bedwas RFC - 24 Jun 2024',3,'',16,1,'2024-06-24 00:03:54.622979');
INSERT INTO django_admin_log VALUES(155,'2','Cancel The Transmission applied for Those Damn Crows - Bedwas RFC - 24 Jun 2024',3,'',16,1,'2024-06-24 00:03:54.630609');
INSERT INTO django_admin_log VALUES(156,'4','Cancel The Transmission applied for Those Damn Crows - Bedwas RFC - 24 Jun 2024',2,'[{"changed": {"fields": ["Original artist", "Venue", "Message", "Status"]}}]',16,1,'2024-06-28 22:00:36.775682');
INSERT INTO django_admin_log VALUES(157,'18','Those Damn Crows - Bedwas Workmen''s Hall - 24 Jun 2024',2,'[{"changed": {"fields": ["Venue name"]}}]',10,1,'2024-06-28 22:00:58.021540');
INSERT INTO django_admin_log VALUES(158,'18','Those Damn Crows - Bedwas Workmen''s Hall - 30 Jul 2024',2,'[{"changed": {"fields": ["Date of gig"]}}]',10,1,'2024-06-28 22:01:14.146483');
INSERT INTO django_admin_log VALUES(159,'9','Cancel The Transmission applied for Those Damn Crows - Bedwas Workmen''s Hall - 30 Jul 2024',3,'',16,1,'2024-06-29 01:03:21.732514');
INSERT INTO django_admin_log VALUES(160,'8','Cancel The Transmission applied for Those Damn Crows - Bedwas Workmen''s Hall - 30 Jul 2024',3,'',16,1,'2024-06-29 01:03:21.735362');
INSERT INTO django_admin_log VALUES(161,'7','Cancel The Transmission applied for Those Damn Crows - Bedwas Workmen''s Hall - 30 Jul 2024',3,'',16,1,'2024-06-29 01:03:21.736457');
INSERT INTO django_admin_log VALUES(162,'6','Cancel The Transmission applied for Those Damn Crows - Bedwas Workmen''s Hall - 30 Jul 2024',3,'',16,1,'2024-06-29 01:03:21.737260');
INSERT INTO django_admin_log VALUES(163,'5','Cancel The Transmission applied for Those Damn Crows - Bedwas Workmen''s Hall - 30 Jul 2024',3,'',16,1,'2024-06-29 01:03:21.738057');
INSERT INTO django_admin_log VALUES(164,'4','Cancel The Transmission applied for Those Damn Crows - Bedwas Workmen''s Hall - 30 Jul 2024',3,'',16,1,'2024-06-29 01:03:21.739024');
INSERT INTO django_admin_log VALUES(165,'13','Cancel The Transmission applied for Those Damn Crows - Bedwas Workmen''s Hall - 30 Jul 2024',3,'',16,1,'2024-06-29 01:24:15.361122');
INSERT INTO django_admin_log VALUES(166,'12','Cancel The Transmission applied for Those Damn Crows - Bedwas Workmen''s Hall - 30 Jul 2024',3,'',16,1,'2024-06-29 01:24:15.362591');
INSERT INTO django_admin_log VALUES(167,'11','Cancel The Transmission applied for Those Damn Crows - Bedwas Workmen''s Hall - 30 Jul 2024',3,'',16,1,'2024-06-29 01:24:15.363167');
INSERT INTO django_admin_log VALUES(168,'10','Cancel The Transmission applied for Those Damn Crows - Bedwas Workmen''s Hall - 30 Jul 2024',3,'',16,1,'2024-06-29 01:24:15.363617');
INSERT INTO django_admin_log VALUES(169,'14','Cancel The Transmission applied for Those Damn Crows - Bedwas Workmen''s Hall - 30 Jul 2024',2,'[{"changed": {"fields": ["Status"]}}]',16,1,'2024-06-29 01:38:38.048854');
INSERT INTO django_admin_log VALUES(170,'16','Keane applied for Cancel The Transmission - The Dolls House - 25 Apr 2024',1,'[{"added": {}}]',16,1,'2024-06-29 01:50:03.320741');
INSERT INTO django_admin_log VALUES(171,'17','Keane applied for Cancel The Transmission - The Dolls House - 25 Apr 2024',1,'[{"added": {}}]',16,1,'2024-06-29 01:50:09.074619');
INSERT INTO django_admin_log VALUES(172,'16','Keane applied for Cancel The Transmission - The Dolls House - 25 Apr 2024',3,'',16,1,'2024-06-29 01:50:29.481131');
INSERT INTO django_admin_log VALUES(173,'18','Cancel The Transmission applied for Those Damn Crows - Bedwas Workmen''s Hall - 30 Jul 2024',3,'',16,1,'2024-07-01 01:40:49.918726');
INSERT INTO django_admin_log VALUES(174,'15','Cancel The Transmission applied for Those Damn Crows - Bedwas Workmen''s Hall - 30 Jul 2024',3,'',16,1,'2024-07-01 01:40:49.920484');
INSERT INTO django_admin_log VALUES(175,'14','Cancel The Transmission applied for Those Damn Crows - Bedwas Workmen''s Hall - 30 Jul 2024',3,'',16,1,'2024-07-01 01:40:49.921169');
INSERT INTO django_admin_log VALUES(176,'18','Those Damn Crows - Bedwas Workmen''s Hall - 30 Jul 2024',2,'[{"changed": {"fields": ["Venue"]}}]',10,1,'2024-07-01 01:51:11.684468');
INSERT INTO django_admin_log VALUES(177,'18','Those Damn Crows - Bedwas Workmen''s Hall - 30 Jul 2024',2,'[]',10,1,'2024-07-01 01:53:02.289955');
INSERT INTO django_admin_log VALUES(178,'19','Cancel The Transmission applied for Those Damn Crows - Bedwas Workmen''s Hall - 30 Jul 2024',3,'',16,1,'2024-07-02 02:15:55.051940');
INSERT INTO django_admin_log VALUES(179,'19','Bedwas Workmen’s Hall',2,'[{"changed": {"fields": ["Image", "Facebook", "Twitter", "Youtube"]}}]',9,1,'2024-07-12 01:22:15.872428');
INSERT INTO django_admin_log VALUES(180,'19','Cancel The Transmission - None - 28 Jul 2024',3,'',10,1,'2024-07-13 01:27:55.007868');
INSERT INTO django_admin_log VALUES(181,'20','Cancel The Transmission - Bedwas Workmen’s Hall - 28 Jul 2024',3,'',10,1,'2024-07-13 01:31:05.570974');
INSERT INTO django_admin_log VALUES(182,'22','Cancel The Transmission - Bedwas Workmen’s Hall - 28 Jul 2024',3,'',10,1,'2024-07-13 01:34:55.641214');
INSERT INTO django_admin_log VALUES(183,'21','Cancel The Transmission - Bedwas Workmen’s Hall - 28 Jul 2024',3,'',10,1,'2024-07-13 01:34:55.645688');
INSERT INTO django_admin_log VALUES(184,'23','Cancel The Transmission - Bedwas Workmen’s Hall - 28 Jul 2024',3,'',10,1,'2024-07-13 01:38:01.169405');
INSERT INTO django_admin_log VALUES(185,'4','Notification for venue Bedwas Workmen’s Hall - The artist Cancel The Transmission has advertised a gig on 2024-07-28.',3,'',19,1,'2024-07-14 00:46:38.054987');
INSERT INTO django_admin_log VALUES(186,'3','Notification for venue Bedwas Workmen’s Hall - The artist Cancel The Transmission has advertised a gig on 2024-07-28.',3,'',19,1,'2024-07-14 00:46:38.061309');
INSERT INTO django_admin_log VALUES(187,'2','Notification for venue Bedwas Workmen’s Hall - The artist Cancel The Transmission has advertised a gig on 2024-07-28.',3,'',19,1,'2024-07-14 00:46:38.062442');
INSERT INTO django_admin_log VALUES(188,'1','Notification for venue Bedwas Workmen’s Hall - The artist Cancel The Transmission has advertised a gig on 2024-07-28.',3,'',19,1,'2024-07-14 00:46:38.063170');
INSERT INTO django_admin_log VALUES(189,'25','Cancel The Transmission - Bedwas Workmen’s Hall - 28 Jul 2024',3,'',10,1,'2024-07-14 00:47:03.996520');
INSERT INTO django_admin_log VALUES(190,'24','Cancel The Transmission - Bedwas Workmen’s Hall - 28 Jul 2024',3,'',10,1,'2024-07-14 00:47:04.002587');
INSERT INTO django_admin_log VALUES(191,'17','Cancel The Transmission - None - 04 Apr 2024',3,'',10,1,'2024-07-14 00:47:04.003358');
INSERT INTO django_admin_log VALUES(192,'10','Cancel The Transmission - None - 24 Jun 2024',3,'',10,1,'2024-07-14 00:47:04.003950');
INSERT INTO django_admin_log VALUES(193,'3','Cancel The Transmission - None - 04 May 2024',3,'',10,1,'2024-07-14 00:47:04.004510');
INSERT INTO django_admin_log VALUES(194,'2','Cancel The Transmission - None - 25 Apr 2024',3,'',10,1,'2024-07-14 00:47:04.005049');
INSERT INTO django_admin_log VALUES(195,'38','Cancel The Transmission - Bedwas Workmen’s Hall - 28 Jul 2024',3,'',10,1,'2024-07-14 01:25:53.018129');
INSERT INTO django_admin_log VALUES(196,'37','Cancel The Transmission - Bedwas Workmen’s Hall - 28 Jul 2024',3,'',10,1,'2024-07-14 01:25:53.026746');
INSERT INTO django_admin_log VALUES(197,'36','Cancel The Transmission - Bedwas Workmen’s Hall - 28 Jul 2024',3,'',10,1,'2024-07-14 01:25:53.027767');
INSERT INTO django_admin_log VALUES(198,'35','Cancel The Transmission - Bedwas Workmen’s Hall - 28 Jul 2024',3,'',10,1,'2024-07-14 01:25:53.028557');
INSERT INTO django_admin_log VALUES(199,'34','Cancel The Transmission - Bedwas Workmen’s Hall - 28 Jul 2024',3,'',10,1,'2024-07-14 01:25:53.029376');
INSERT INTO django_admin_log VALUES(200,'33','Cancel The Transmission - Bedwas Workmen’s Hall - 28 Jul 2024',3,'',10,1,'2024-07-14 01:25:53.030059');
INSERT INTO django_admin_log VALUES(201,'32','Cancel The Transmission - Bedwas Workmen’s Hall - 28 Jul 2024',3,'',10,1,'2024-07-14 01:25:53.030731');
INSERT INTO django_admin_log VALUES(202,'31','Cancel The Transmission - Bedwas Workmen’s Hall - 28 Jul 2024',3,'',10,1,'2024-07-14 01:25:53.033130');
INSERT INTO django_admin_log VALUES(203,'30','Cancel The Transmission - Bedwas Workmen’s Hall - 28 Jul 2024',3,'',10,1,'2024-07-14 01:25:53.033819');
INSERT INTO django_admin_log VALUES(204,'29','Cancel The Transmission - Bedwas Workmen’s Hall - 28 Jul 2024',3,'',10,1,'2024-07-14 01:25:53.034599');
INSERT INTO django_admin_log VALUES(205,'28','Cancel The Transmission - Bedwas Workmen’s Hall - 28 Jul 2024',3,'',10,1,'2024-07-14 01:25:53.035290');
INSERT INTO django_admin_log VALUES(206,'27','Cancel The Transmission - Bedwas Workmen’s Hall - 28 Jul 2024',3,'',10,1,'2024-07-14 01:25:53.036299');
INSERT INTO django_admin_log VALUES(207,'26','Cancel The Transmission - Bedwas Workmen’s Hall - 28 Jul 2024',3,'',10,1,'2024-07-14 01:25:53.036868');
INSERT INTO django_admin_log VALUES(208,'17','Notification for venue Bedwas Workmen’s Hall - The artist Cancel The Transmission has advertised a gig on 2024-07-28.',3,'',19,1,'2024-07-14 01:26:38.485820');
INSERT INTO django_admin_log VALUES(209,'16','Notification for venue Bedwas Workmen’s Hall - The artist Cancel The Transmission has advertised a gig on 2024-07-28.',3,'',19,1,'2024-07-14 01:26:38.489057');
INSERT INTO django_admin_log VALUES(210,'15','Notification for venue Bedwas Workmen’s Hall - The artist Cancel The Transmission has advertised a gig on 2024-07-28.',3,'',19,1,'2024-07-14 01:26:38.489871');
INSERT INTO django_admin_log VALUES(211,'14','Notification for venue Bedwas Workmen’s Hall - The artist Cancel The Transmission has advertised a gig on 2024-07-28.',3,'',19,1,'2024-07-14 01:26:38.490466');
INSERT INTO django_admin_log VALUES(212,'13','Notification for venue Bedwas Workmen’s Hall - The artist Cancel The Transmission has advertised a gig on 2024-07-28.',3,'',19,1,'2024-07-14 01:26:38.490982');
INSERT INTO django_admin_log VALUES(213,'12','Notification for venue Bedwas Workmen’s Hall - The artist Cancel The Transmission has advertised a gig on 2024-07-28.',3,'',19,1,'2024-07-14 01:26:38.491542');
INSERT INTO django_admin_log VALUES(214,'11','Notification for venue Bedwas Workmen’s Hall - The artist Cancel The Transmission has advertised a gig on 2024-07-28.',3,'',19,1,'2024-07-14 01:26:38.492186');
INSERT INTO django_admin_log VALUES(215,'10','Notification for venue Bedwas Workmen’s Hall - The artist Cancel The Transmission has advertised a gig on 2024-07-28.',3,'',19,1,'2024-07-14 01:26:38.492720');
INSERT INTO django_admin_log VALUES(216,'9','Notification for venue Bedwas Workmen’s Hall - The artist Cancel The Transmission has advertised a gig on 2024-07-28.',3,'',19,1,'2024-07-14 01:26:38.493253');
INSERT INTO django_admin_log VALUES(217,'8','Notification for venue Bedwas Workmen’s Hall - The artist Cancel The Transmission has advertised a gig on 2024-07-28.',3,'',19,1,'2024-07-14 01:26:38.493767');
INSERT INTO django_admin_log VALUES(218,'7','Notification for venue Bedwas Workmen’s Hall - The artist Cancel The Transmission has advertised a gig on 2024-07-28.',3,'',19,1,'2024-07-14 01:26:38.494358');
INSERT INTO django_admin_log VALUES(219,'6','Notification for venue Bedwas Workmen’s Hall - The artist Cancel The Transmission has advertised a gig on 2024-07-28.',3,'',19,1,'2024-07-14 01:26:38.495135');
INSERT INTO django_admin_log VALUES(220,'5','Notification for venue Bedwas Workmen’s Hall - The artist Cancel The Transmission has advertised a gig on 2024-07-28.',3,'',19,1,'2024-07-14 01:26:38.495919');
INSERT INTO django_admin_log VALUES(221,'18','Notification for venue Bedwas Workmen’s Hall - The artist Cancel The Transmission has advertised their gig on 2024-07-28.',2,'[{"changed": {"fields": ["Message"]}}]',19,1,'2024-07-14 02:07:39.800759');
INSERT INTO django_admin_log VALUES(222,'18','Those Damn Crows - None - 30 Jul 2024',3,'',10,1,'2024-07-14 02:07:56.222083');
INSERT INTO django_admin_log VALUES(223,'19','Notification for venue Bedwas Workmen’s Hall - Test',1,'[{"added": {}}]',19,1,'2024-07-15 00:19:32.225468');
INSERT INTO django_admin_log VALUES(224,'19','Notification for venue Bedwas Workmen’s Hall - Test',3,'',19,1,'2024-07-15 00:21:01.509100');
INSERT INTO django_admin_log VALUES(225,'20','Notification for venue Bedwas Workmen’s Hall - Test',1,'[{"added": {}}]',19,1,'2024-07-15 00:21:42.672611');
INSERT INTO django_admin_log VALUES(226,'20','Notification for venue Bedwas Workmen’s Hall - Test',3,'',19,1,'2024-07-15 00:21:58.402349');
INSERT INTO django_admin_log VALUES(227,'21','Notification for venue Bedwas Workmen’s Hall - Test 1',1,'[{"added": {}}]',19,1,'2024-07-15 00:29:13.036529');
INSERT INTO django_admin_log VALUES(228,'22','Notification for venue Bedwas Workmen’s Hall - Test 2',1,'[{"added": {}}]',19,1,'2024-07-15 00:29:26.894983');
INSERT INTO django_admin_log VALUES(229,'23','Notification for venue Bedwas Workmen’s Hall - Test 3',1,'[{"added": {}}]',19,1,'2024-07-15 00:30:25.686370');
INSERT INTO django_admin_log VALUES(230,'24','Notification for venue Bedwas Workmen’s Hall - Test 4',1,'[{"added": {}}]',19,1,'2024-07-15 00:42:44.906382');
INSERT INTO django_admin_log VALUES(231,'25','Notification for venue Bedwas Workmen’s Hall - Test 5',1,'[{"added": {}}]',19,1,'2024-07-15 00:43:00.020745');
INSERT INTO django_admin_log VALUES(232,'25','Notification for venue Bedwas Workmen’s Hall - Test 5',3,'',19,1,'2024-07-15 00:46:54.838441');
INSERT INTO django_admin_log VALUES(233,'26','Notification for venue Bedwas Workmen’s Hall - Test 5',1,'[{"added": {}}]',19,1,'2024-07-15 00:47:05.351662');
INSERT INTO django_admin_log VALUES(234,'21','Those Damn Crows applied for Cancel The Transmission - Bedwas Workmen’s Hall - 28 Jul 2024',1,'[{"added": {}}]',16,1,'2024-07-15 23:51:10.217691');
INSERT INTO django_admin_log VALUES(235,'22','Notification for venue Bedwas Workmen’s Hall - Test 2',2,'[{"changed": {"fields": ["Notification type"]}}]',19,1,'2024-07-16 01:29:02.303261');
INSERT INTO django_admin_log VALUES(236,'21','Notification for venue Bedwas Workmen’s Hall - Test 1',2,'[{"changed": {"fields": ["Notification type"]}}]',19,1,'2024-07-16 01:29:08.660319');
INSERT INTO django_admin_log VALUES(237,'26','Notification for venue Bedwas Workmen’s Hall - Test 5',2,'[{"changed": {"fields": ["Notification type"]}}]',19,1,'2024-07-16 01:29:16.469380');
INSERT INTO django_admin_log VALUES(238,'24','Notification for venue Bedwas Workmen’s Hall - Test 4',2,'[{"changed": {"fields": ["Notification type"]}}]',19,1,'2024-07-16 01:29:20.627423');
INSERT INTO django_admin_log VALUES(239,'23','Notification for venue Bedwas Workmen’s Hall - Test 3',2,'[{"changed": {"fields": ["Notification type"]}}]',19,1,'2024-07-16 01:29:24.590534');
INSERT INTO django_admin_log VALUES(240,'22','Keane applied for Cancel The Transmission - Bedwas Workmen’s Hall - 01 Aug 2024',1,'[{"added": {}}]',16,1,'2024-07-17 23:00:45.840057');
INSERT INTO django_admin_log VALUES(241,'23','The Struts applied for Cancel The Transmission - Bedwas Workmen’s Hall - 01 Aug 2024',1,'[{"added": {}}]',16,1,'2024-07-17 23:03:10.142064');
INSERT INTO django_admin_log VALUES(242,'21','Those Damn Crows applied for Cancel The Transmission - Bedwas Workmen’s Hall - 28 Jul 2024',3,'',16,1,'2024-07-18 01:17:04.929531');
INSERT INTO django_admin_log VALUES(243,'24','Those Damn Crows applied for Cancel The Transmission - Bedwas Workmen’s Hall - 01 Aug 2024',1,'[{"added": {}}]',16,1,'2024-07-18 01:17:24.878879');
INSERT INTO django_admin_log VALUES(244,'40','Cancel The Transmission - Bedwas Workmen’s Hall - 01 Aug 2024',2,'[{"changed": {"fields": ["Description"]}}]',10,1,'2024-07-19 17:52:51.780863');
INSERT INTO django_admin_log VALUES(245,'40','Cancel The Transmission - Bedwas Workmen’s Hall - 01 Aug 2024',2,'[{"changed": {"fields": ["Description"]}}]',10,1,'2024-07-19 17:53:25.326782');
INSERT INTO django_admin_log VALUES(246,'42','Cancel The Transmission - The Leigh - 06 Sep 2024',3,'',10,1,'2024-07-20 00:16:11.513799');
INSERT INTO django_admin_log VALUES(247,'41','Cancel The Transmission - Bedwas Workmen’s Hall - 07 Sep 2024',3,'',10,1,'2024-07-20 00:16:11.520402');
INSERT INTO django_admin_log VALUES(248,'39','Cancel The Transmission - Bedwas Workmen’s Hall - 28 Jul 2024',3,'',10,1,'2024-07-20 00:16:11.521497');
INSERT INTO django_admin_log VALUES(249,'28','Notification for venue Bedwas Workmen’s Hall - The artist Cancel The Transmission has advertised their gig on 2024-09-07.',3,'',19,1,'2024-07-20 00:49:31.473167');
INSERT INTO django_admin_log VALUES(250,'43','Keane - The Dolls House - 12 Dec 2024',1,'[{"added": {}}]',10,1,'2024-07-20 00:50:46.561311');
INSERT INTO django_admin_log VALUES(251,'43','Keane - The Dolls House - 12 Dec 2024',3,'',10,1,'2024-07-20 00:58:08.291051');
INSERT INTO django_admin_log VALUES(252,'44','Keane - The Dolls House - 13 Dec 2024',1,'[{"added": {}}]',10,1,'2024-07-20 00:58:50.993820');
CREATE TABLE IF NOT EXISTS "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTO_INCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);
INSERT INTO django_content_type VALUES(1,'admin','logentry');
INSERT INTO django_content_type VALUES(2,'auth','permission');
INSERT INTO django_content_type VALUES(3,'auth','group');
INSERT INTO django_content_type VALUES(4,'auth','user');
INSERT INTO django_content_type VALUES(5,'contenttypes','contenttype');
INSERT INTO django_content_type VALUES(6,'sessions','session');
INSERT INTO django_content_type VALUES(7,'gigsweep_django_backend','artist');
INSERT INTO django_content_type VALUES(8,'gigsweep_django_backend','unavailability');
INSERT INTO django_content_type VALUES(9,'gigsweep_django_backend','venue');
INSERT INTO django_content_type VALUES(10,'gigsweep_django_backend','artistlistedgig');
INSERT INTO django_content_type VALUES(11,'gigsweep_django_backend','venuelistedgig');
INSERT INTO django_content_type VALUES(12,'gigsweep_django_backend','newslettersignup');
INSERT INTO django_content_type VALUES(13,'gigsweep_django_backend','membershipoptions');
INSERT INTO django_content_type VALUES(14,'gigsweep_django_backend','artistwrittenreview');
INSERT INTO django_content_type VALUES(15,'gigsweep_django_backend','venuewrittenreview');
INSERT INTO django_content_type VALUES(16,'gigsweep_django_backend','artistgigapplication');
INSERT INTO django_content_type VALUES(17,'gigsweep_django_backend','venuegigapplication');
INSERT INTO django_content_type VALUES(18,'gigsweep_django_backend','chatmessage');
INSERT INTO django_content_type VALUES(19,'gigsweep_django_backend','venuenotification');
INSERT INTO django_content_type VALUES(20,'gigsweep_django_backend','artistnotification');
CREATE TABLE IF NOT EXISTS "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTO_INCREMENT, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL);
INSERT INTO auth_permission VALUES(1,1,'add_logentry','Can add log entry');
INSERT INTO auth_permission VALUES(2,1,'change_logentry','Can change log entry');
INSERT INTO auth_permission VALUES(3,1,'delete_logentry','Can delete log entry');
INSERT INTO auth_permission VALUES(4,1,'view_logentry','Can view log entry');
INSERT INTO auth_permission VALUES(5,2,'add_permission','Can add permission');
INSERT INTO auth_permission VALUES(6,2,'change_permission','Can change permission');
INSERT INTO auth_permission VALUES(7,2,'delete_permission','Can delete permission');
INSERT INTO auth_permission VALUES(8,2,'view_permission','Can view permission');
INSERT INTO auth_permission VALUES(9,3,'add_group','Can add group');
INSERT INTO auth_permission VALUES(10,3,'change_group','Can change group');
INSERT INTO auth_permission VALUES(11,3,'delete_group','Can delete group');
INSERT INTO auth_permission VALUES(12,3,'view_group','Can view group');
INSERT INTO auth_permission VALUES(13,4,'add_user','Can add user');
INSERT INTO auth_permission VALUES(14,4,'change_user','Can change user');
INSERT INTO auth_permission VALUES(15,4,'delete_user','Can delete user');
INSERT INTO auth_permission VALUES(16,4,'view_user','Can view user');
INSERT INTO auth_permission VALUES(17,5,'add_contenttype','Can add content type');
INSERT INTO auth_permission VALUES(18,5,'change_contenttype','Can change content type');
INSERT INTO auth_permission VALUES(19,5,'delete_contenttype','Can delete content type');
INSERT INTO auth_permission VALUES(20,5,'view_contenttype','Can view content type');
INSERT INTO auth_permission VALUES(21,6,'add_session','Can add session');
INSERT INTO auth_permission VALUES(22,6,'change_session','Can change session');
INSERT INTO auth_permission VALUES(23,6,'delete_session','Can delete session');
INSERT INTO auth_permission VALUES(24,6,'view_session','Can view session');
INSERT INTO auth_permission VALUES(25,7,'add_artist','Can add artist');
INSERT INTO auth_permission VALUES(26,7,'change_artist','Can change artist');
INSERT INTO auth_permission VALUES(27,7,'delete_artist','Can delete artist');
INSERT INTO auth_permission VALUES(28,7,'view_artist','Can view artist');
INSERT INTO auth_permission VALUES(29,8,'add_unavailability','Can add unavailability');
INSERT INTO auth_permission VALUES(30,8,'change_unavailability','Can change unavailability');
INSERT INTO auth_permission VALUES(31,8,'delete_unavailability','Can delete unavailability');
INSERT INTO auth_permission VALUES(32,8,'view_unavailability','Can view unavailability');
INSERT INTO auth_permission VALUES(33,9,'add_venue','Can add venue');
INSERT INTO auth_permission VALUES(34,9,'change_venue','Can change venue');
INSERT INTO auth_permission VALUES(35,9,'delete_venue','Can delete venue');
INSERT INTO auth_permission VALUES(36,9,'view_venue','Can view venue');
INSERT INTO auth_permission VALUES(37,10,'add_artistlistedgig','Can add artist listed gig');
INSERT INTO auth_permission VALUES(38,10,'change_artistlistedgig','Can change artist listed gig');
INSERT INTO auth_permission VALUES(39,10,'delete_artistlistedgig','Can delete artist listed gig');
INSERT INTO auth_permission VALUES(40,10,'view_artistlistedgig','Can view artist listed gig');
INSERT INTO auth_permission VALUES(41,11,'add_venuelistedgig','Can add venue listed gig');
INSERT INTO auth_permission VALUES(42,11,'change_venuelistedgig','Can change venue listed gig');
INSERT INTO auth_permission VALUES(43,11,'delete_venuelistedgig','Can delete venue listed gig');
INSERT INTO auth_permission VALUES(44,11,'view_venuelistedgig','Can view venue listed gig');
INSERT INTO auth_permission VALUES(45,12,'add_newslettersignup','Can add newsletter signup');
INSERT INTO auth_permission VALUES(46,12,'change_newslettersignup','Can change newsletter signup');
INSERT INTO auth_permission VALUES(47,12,'delete_newslettersignup','Can delete newsletter signup');
INSERT INTO auth_permission VALUES(48,12,'view_newslettersignup','Can view newsletter signup');
INSERT INTO auth_permission VALUES(49,13,'add_membershipoptions','Can add membership options');
INSERT INTO auth_permission VALUES(50,13,'change_membershipoptions','Can change membership options');
INSERT INTO auth_permission VALUES(51,13,'delete_membershipoptions','Can delete membership options');
INSERT INTO auth_permission VALUES(52,13,'view_membershipoptions','Can view membership options');
INSERT INTO auth_permission VALUES(53,14,'add_artistwrittenreview','Can add artist written review');
INSERT INTO auth_permission VALUES(54,14,'change_artistwrittenreview','Can change artist written review');
INSERT INTO auth_permission VALUES(55,14,'delete_artistwrittenreview','Can delete artist written review');
INSERT INTO auth_permission VALUES(56,14,'view_artistwrittenreview','Can view artist written review');
INSERT INTO auth_permission VALUES(57,15,'add_venuewrittenreview','Can add venue written review');
INSERT INTO auth_permission VALUES(58,15,'change_venuewrittenreview','Can change venue written review');
INSERT INTO auth_permission VALUES(59,15,'delete_venuewrittenreview','Can delete venue written review');
INSERT INTO auth_permission VALUES(60,15,'view_venuewrittenreview','Can view venue written review');
INSERT INTO auth_permission VALUES(61,16,'add_artistgigapplication','Can add artist gig application');
INSERT INTO auth_permission VALUES(62,16,'change_artistgigapplication','Can change artist gig application');
INSERT INTO auth_permission VALUES(63,16,'delete_artistgigapplication','Can delete artist gig application');
INSERT INTO auth_permission VALUES(64,16,'view_artistgigapplication','Can view artist gig application');
INSERT INTO auth_permission VALUES(65,17,'add_venuegigapplication','Can add venue gig application');
INSERT INTO auth_permission VALUES(66,17,'change_venuegigapplication','Can change venue gig application');
INSERT INTO auth_permission VALUES(67,17,'delete_venuegigapplication','Can delete venue gig application');
INSERT INTO auth_permission VALUES(68,17,'view_venuegigapplication','Can view venue gig application');
INSERT INTO auth_permission VALUES(69,18,'add_chatmessage','Can add chat message');
INSERT INTO auth_permission VALUES(70,18,'change_chatmessage','Can change chat message');
INSERT INTO auth_permission VALUES(71,18,'delete_chatmessage','Can delete chat message');
INSERT INTO auth_permission VALUES(72,18,'view_chatmessage','Can view chat message');
INSERT INTO auth_permission VALUES(73,19,'add_venuenotification','Can add venue notification');
INSERT INTO auth_permission VALUES(74,19,'change_venuenotification','Can change venue notification');
INSERT INTO auth_permission VALUES(75,19,'delete_venuenotification','Can delete venue notification');
INSERT INTO auth_permission VALUES(76,19,'view_venuenotification','Can view venue notification');
INSERT INTO auth_permission VALUES(77,20,'add_artistnotification','Can add artist notification');
INSERT INTO auth_permission VALUES(78,20,'change_artistnotification','Can change artist notification');
INSERT INTO auth_permission VALUES(79,20,'delete_artistnotification','Can delete artist notification');
INSERT INTO auth_permission VALUES(80,20,'view_artistnotification','Can view artist notification');
CREATE TABLE IF NOT EXISTS auth_group (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS auth_user (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    password VARCHAR(128) NOT NULL,
    last_login DATETIME NULL,
    is_superuser BOOLEAN NOT NULL,
    username VARCHAR(150) NOT NULL UNIQUE,
    last_name VARCHAR(150) NOT NULL,
    email VARCHAR(254) NOT NULL,
    is_staff BOOLEAN NOT NULL,
    is_active BOOLEAN NOT NULL,
    date_joined DATETIME NOT NULL,
    first_name VARCHAR(150) NOT NULL
);
INSERT INTO auth_user VALUES(1,'pbkdf2_sha256$600000$JarGUbkyxhtpmQUwarFzpE$g8wFImGhRQqG2GyhlH5G+C0U6voVMBYbAyHxr2X5xOo=','2024-07-10 01:20:55.038908',1,'joshthomas','','gigsweepmusic@gmail.com',1,1,'2023-10-16 23:18:38.817694','');
CREATE TABLE IF NOT EXISTS django_session (
    session_key VARCHAR(40) NOT NULL PRIMARY KEY,
    session_data TEXT NOT NULL,
    expire_date DATETIME NOT NULL
);
INSERT INTO django_session VALUES('r07w60j81f9hrhnwk4a715ui2grleyv5','.eJxVjEEOwiAQRe_C2hDoACMu3fcMZIBBqqYkpV0Z765NutDtf-_9lwi0rTVsnZcwZXERWpx-t0jpwfMO8p3mW5OpzesyRbkr8qBdji3z83q4fweVev3WQNqis4MpoCMhYGLD4G1WZxcjsYJBWUjoXUFbEImBmPWQIRnvkxPvD857N6c:1qsWu1:Uoc9v_XMp1HZQhaANh8bEIecUWHBY5qY1vNfGRNXoSE','2023-10-30 23:21:37.786546');
INSERT INTO django_session VALUES('mhcablevc4qfel8vey9xqx2fyc6vahxd','.eJxVjEEOwiAQRe_C2hDoACMu3fcMZIBBqqYkpV0Z765NutDtf-_9lwi0rTVsnZcwZXERWpx-t0jpwfMO8p3mW5OpzesyRbkr8qBdji3z83q4fweVev3WQNqis4MpoCMhYGLD4G1WZxcjsYJBWUjoXUFbEImBmPWQIRnvkxPvD857N6c:1qstaS:SGqtVQMtzNU7vd3w-0A1wjKtRmV2aGUV2JZz_q8FRk4','2023-10-31 23:34:56.601533');
INSERT INTO django_session VALUES('4m47e30l6sjplgfk7znxsi9ya6q650lx','.eJxVjEEOwiAQRe_C2hDoACMu3fcMZIBBqqYkpV0Z765NutDtf-_9lwi0rTVsnZcwZXERWpx-t0jpwfMO8p3mW5OpzesyRbkr8qBdji3z83q4fweVev3WQNqis4MpoCMhYGLD4G1WZxcjsYJBWUjoXUFbEImBmPWQIRnvkxPvD857N6c:1qtcdY:IELULzZ8eJzSEmoWxD_W_ISE51mxOs-jSiof5YRDlyU','2023-11-02 23:41:08.374045');
INSERT INTO django_session VALUES('506txnylj66764t3rhgc4tsv1677zc58','.eJxVjEEOwiAQRe_C2hDoACMu3fcMZIBBqqYkpV0Z765NutDtf-_9lwi0rTVsnZcwZXERWpx-t0jpwfMO8p3mW5OpzesyRbkr8qBdji3z83q4fweVev3WQNqis4MpoCMhYGLD4G1WZxcjsYJBWUjoXUFbEImBmPWQIRnvkxPvD857N6c:1rLBjs:Oq0MOSSQgyb3rMwPJCPiCRbccHyQUz96CY_xeqhV3xQ','2024-01-18 00:37:36.998476');
INSERT INTO django_session VALUES('herb7gkqvq7n9je7ynoltdt8umodjq7z','.eJxVjEEOwiAQRe_C2hDoACMu3fcMZIBBqqYkpV0Z765NutDtf-_9lwi0rTVsnZcwZXERWpx-t0jpwfMO8p3mW5OpzesyRbkr8qBdji3z83q4fweVev3WQNqis4MpoCMhYGLD4G1WZxcjsYJBWUjoXUFbEImBmPWQIRnvkxPvD857N6c:1rMdOR:Lm2MHkbKv64TNM26zL6lnqr7KCd2-tgPBN_Da3fE57w','2024-01-22 00:21:27.284295');
INSERT INTO django_session VALUES('0e75okgampmujht1po00x780tvysb349','.eJxVjEEOwiAQRe_C2hDoACMu3fcMZIBBqqYkpV0Z765NutDtf-_9lwi0rTVsnZcwZXERWpx-t0jpwfMO8p3mW5OpzesyRbkr8qBdji3z83q4fweVev3WQNqis4MpoCMhYGLD4G1WZxcjsYJBWUjoXUFbEImBmPWQIRnvkxPvD857N6c:1rSRFq:qW-gr6P4nZJgJRBq-5djx2NjEl6Mr866J3TD9g9KbFk','2024-02-07 00:36:34.880355');
INSERT INTO django_session VALUES('qeavt5z57lqykiqg6s9mk8bibqpejryj','.eJxVjEEOwiAQRe_C2hDoACMu3fcMZIBBqqYkpV0Z765NutDtf-_9lwi0rTVsnZcwZXERWpx-t0jpwfMO8p3mW5OpzesyRbkr8qBdji3z83q4fweVev3WQNqis4MpoCMhYGLD4G1WZxcjsYJBWUjoXUFbEImBmPWQIRnvkxPvD857N6c:1rTC2y:qgvIVcf2wJE0uSu8Zc_bKtZIK0RZoQ2DDZCcpSu8ols','2024-02-09 02:34:24.329170');
INSERT INTO django_session VALUES('5bgk14wuw6kbajlodgvkrze79pb2e8zk','.eJxVjEEOwiAQRe_C2hDoACMu3fcMZIBBqqYkpV0Z765NutDtf-_9lwi0rTVsnZcwZXERWpx-t0jpwfMO8p3mW5OpzesyRbkr8qBdji3z83q4fweVev3WQNqis4MpoCMhYGLD4G1WZxcjsYJBWUjoXUFbEImBmPWQIRnvkxPvD857N6c:1rYcZs:wr-6IzpPSp0Y_xTm8IlBrfHde5UBmKL1-jYhQHYWgZI','2024-02-24 01:54:48.671078');
INSERT INTO django_session VALUES('j7596pgi9hvc75129mawgi78dn7e233p','.eJxVjEEOwiAQRe_C2hDoACMu3fcMZIBBqqYkpV0Z765NutDtf-_9lwi0rTVsnZcwZXERWpx-t0jpwfMO8p3mW5OpzesyRbkr8qBdji3z83q4fweVev3WQNqis4MpoCMhYGLD4G1WZxcjsYJBWUjoXUFbEImBmPWQIRnvkxPvD857N6c:1rdhMA:X7B_EFQtz141hz8JVNE6JYdCf-8AvNic9IWWP71TZEo','2024-03-09 02:01:38.741760');
INSERT INTO django_session VALUES('67xibz2jjxun3uhqapcdtik895ikqf6k','.eJxVjEEOwiAQRe_C2hDoACMu3fcMZIBBqqYkpV0Z765NutDtf-_9lwi0rTVsnZcwZXERWpx-t0jpwfMO8p3mW5OpzesyRbkr8qBdji3z83q4fweVev3WQNqis4MpoCMhYGLD4G1WZxcjsYJBWUjoXUFbEImBmPWQIRnvkxPvD857N6c:1rdhMB:vEeYVyx-hsBUvXhKGbnAZg6H-w-KFcmGDliBbCFJ4N4','2024-03-09 02:01:39.050947');
INSERT INTO django_session VALUES('dmzxa9urxbwx46e1y48sm3kfy1qnjcca','.eJxVjEEOwiAQRe_C2hDoACMu3fcMZIBBqqYkpV0Z765NutDtf-_9lwi0rTVsnZcwZXERWpx-t0jpwfMO8p3mW5OpzesyRbkr8qBdji3z83q4fweVev3WQNqis4MpoCMhYGLD4G1WZxcjsYJBWUjoXUFbEImBmPWQIRnvkxPvD857N6c:1rj7vG:VPpEoHXdz7poggaeviDr1H4xHB8mFe-9InIZkecYvrs','2024-03-24 01:24:18.592904');
INSERT INTO django_session VALUES('ix9icnzzu11v57u2upxyiap27nyc87mz','.eJxVjEEOwiAQRe_C2hDoACMu3fcMZIBBqqYkpV0Z765NutDtf-_9lwi0rTVsnZcwZXERWpx-t0jpwfMO8p3mW5OpzesyRbkr8qBdji3z83q4fweVev3WQNqis4MpoCMhYGLD4G1WZxcjsYJBWUjoXUFbEImBmPWQIRnvkxPvD857N6c:1roZ7E:AKLswKR46bB3rDGMIcvErMVcRUksYdMnWhQY-NEvVdU','2024-04-08 01:27:08.385803');
INSERT INTO django_session VALUES('u8d8i5nui56zba3l9s5e8hu9txeftiu0','.eJxVjEEOwiAQRe_C2hDoACMu3fcMZIBBqqYkpV0Z765NutDtf-_9lwi0rTVsnZcwZXERWpx-t0jpwfMO8p3mW5OpzesyRbkr8qBdji3z83q4fweVev3WQNqis4MpoCMhYGLD4G1WZxcjsYJBWUjoXUFbEImBmPWQIRnvkxPvD857N6c:1s5EL9:FjKYHRFlq5Hp58J-Tzbl4hB0rY2U5q25Cwu3zQRqwYA','2024-05-24 00:42:23.076728');
INSERT INTO django_session VALUES('u6rpch32sqs56pjwjkd8o3n8c42il7nt','.eJxVjEEOwiAQRe_C2hDoACMu3fcMZIBBqqYkpV0Z765NutDtf-_9lwi0rTVsnZcwZXERWpx-t0jpwfMO8p3mW5OpzesyRbkr8qBdji3z83q4fweVev3WQNqis4MpoCMhYGLD4G1WZxcjsYJBWUjoXUFbEImBmPWQIRnvkxPvD857N6c:1sC6B2:suK5gEcl6-u8QqyXedNIE5GFZpydPO4awRKXP3kh_7k','2024-06-11 23:24:20.814623');
INSERT INTO django_session VALUES('r5zzdg2ami4w9ylfpsfwy8pinb1h2v0k','.eJxVjEEOwiAQRe_C2hDoACMu3fcMZIBBqqYkpV0Z765NutDtf-_9lwi0rTVsnZcwZXERWpx-t0jpwfMO8p3mW5OpzesyRbkr8qBdji3z83q4fweVev3WQNqis4MpoCMhYGLD4G1WZxcjsYJBWUjoXUFbEImBmPWQIRnvkxPvD857N6c:1sKe2O:vOGLzYVUy-Y7QgprhSLMUvLKK90mXmsSAJ6xlwb3hxY','2024-07-05 13:10:44.993816');
INSERT INTO django_session VALUES('ob5rki9zrlyteirnriqtjnvi8wuqhxjr','.eJxVjEEOwiAQRe_C2hDoACMu3fcMZIBBqqYkpV0Z765NutDtf-_9lwi0rTVsnZcwZXERWpx-t0jpwfMO8p3mW5OpzesyRbkr8qBdji3z83q4fweVev3WQNqis4MpoCMhYGLD4G1WZxcjsYJBWUjoXUFbEImBmPWQIRnvkxPvD857N6c:1sRM0t:GRmce_q6rG4F4y1kxTTR8S3OheytrFKWHRZZgBr6cW8','2024-07-24 01:20:55.039862');
CREATE TABLE IF NOT EXISTS gigsweep_django_backend_artistwrittenreview (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    date_of_performance DATE NULL,
    artist_name VARCHAR(100) NULL,
    venue_name VARCHAR(100) NULL,
    review TEXT NULL,
    rating INT NULL,
    is_approved VARCHAR(100) NULL
);
CREATE TABLE IF NOT EXISTS gigsweep_django_backend_membershipoptions (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    membership_id INT NULL,
    type_of_user VARCHAR(50) NULL,
    title VARCHAR(100) NOT NULL,
    description TEXT NULL,
    price VARCHAR(50) NULL,
    disclosure VARCHAR(500) NULL,
    is_active BOOLEAN NOT NULL
);
INSERT INTO gigsweep_django_backend_membershipoptions VALUES(1,1,'Artist','Standard',replace(replace('<ul>\r\n  <li>Advertise unplayable gigs for other artists to pick up</li>\r\n  <li>Search and apply for gigs based on your criteria</li>\r\n  <li>Promote music, connect with other artists</li>\r\n  <li>See reviews of venues before you agree to play</li>\r\n  <li>Manage gig records and prevent double booking</li>\r\n  <li>Time-saving booking process</li>\r\n</ul>','\r',char(13)),'\n',char(10)),'Price: FREE','No contracts, no commitments, cancel at anytime. Membership is in the form of a rolling monthly subscription.',1);
INSERT INTO gigsweep_django_backend_membershipoptions VALUES(2,2,'Venue','Standard',replace(replace('<ul>\r\n  <li>List gigs and let artists apply to play.</li>\r\n  <li>Discover local and national talent easily.</li>\r\n  <li>Contact artists and notify fans of upcoming gigs.</li>\r\n  <li>Provide feedback on artists you''ve had perform.</li>\r\n  <li>Record-keeping system to prevent double booking.</li>\r\n  <li>Time-saving booking process.</li>\r\n</ul>','\r',char(13)),'\n',char(10)),'Price: FREE','No contracts, no commitments, cancel at anytime. Membership is in the form of a rolling monthly subscription.',1);
INSERT INTO gigsweep_django_backend_membershipoptions VALUES(3,3,'Artist','Pro',replace(replace('<ul>\r\n  <li>Early email notifications for new gigs.</li>\r\n  <li>Increased homepage exposure as a featured artist.</li>\r\n  <li>Verified bluetick for credibility and more visits.</li>\r\n  <li>Improved chances of getting booked.</li>\r\n  <li>Increased exposure for your music.</li>\r\n  <li>Exclusive access to premium promotional tools.</li>\r\n</ul>','\r',char(13)),'\n',char(10)),'Price: £4.49 per month','No contracts, no commitments, cancel at anytime. Membership is in the form of a rolling monthly subscription.',1);
INSERT INTO gigsweep_django_backend_membershipoptions VALUES(4,4,'Venue','Pro',replace(replace('<ul>\r\n  <li>Email notifications about local artists and availability.</li>\r\n  <li>Priority placement in artist search results.</li>\r\n  <li>Verified bluetick for credibility and more visits.</li>\r\n  <li>Recommendations of artists you may want to book.</li>\r\n  <li>Increased exposure for your venue.</li>\r\n  <li>Exclusive access to premium promotional tools.</li>\r\n</ul>','\r',char(13)),'\n',char(10)),'Price: £7.49 per month','No contracts, no commitments, cancel at anytime. Membership is in the form of a rolling monthly subscription.',1);
CREATE TABLE IF NOT EXISTS gigsweep_django_backend_newslettersignup (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(200) NOT NULL
);
INSERT INTO gigsweep_django_backend_newslettersignup VALUES(3,'Joshua.thomas98@hotmail.co.uk');
INSERT INTO gigsweep_django_backend_newslettersignup VALUES(12,'Josh@email.com');
INSERT INTO gigsweep_django_backend_newslettersignup VALUES(13,'Josh@email.com');
CREATE TABLE IF NOT EXISTS gigsweep_django_backend_venuewrittenreview (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    date_of_performance DATE NULL,
    venue_name VARCHAR(100) NULL,
    artist_name VARCHAR(100) NULL,
    review TEXT NULL,
    rating INT NULL,
    is_approved VARCHAR(100) NULL
);
CREATE TABLE IF NOT EXISTS gigsweep_django_backend_venuelistedgig (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    date_of_gig DATE NULL,
    country_of_venue VARCHAR(100) NULL,
    genre_of_gig VARCHAR(50) NULL,
    type_of_gig VARCHAR(50) NULL,
    artist_type VARCHAR(50) NULL,
    payment INT NULL,
    user_type VARCHAR(50) NULL,
    num_applications INT UNSIGNED NOT NULL,
    description TEXT NULL,
    venue_id BIGINT NULL,
    FOREIGN KEY (venue_id) REFERENCES gigsweep_django_backend_venue(id)
);
CREATE TABLE IF NOT EXISTS gigsweep_django_backend_venuegigapplication (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    artist_id BIGINT NULL,
    venue_gig_id BIGINT NULL,
    FOREIGN KEY (artist_id) REFERENCES gigsweep_django_backend_artist(id),
    FOREIGN KEY (venue_gig_id) REFERENCES gigsweep_django_backend_venuelistedgig(id)
);
CREATE TABLE IF NOT EXISTS gigsweep_django_backend_unavailability (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    status VARCHAR(50) NULL,
    reason VARCHAR(150) NULL,
    artist_id BIGINT NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES gigsweep_django_backend_artist(id)
);
INSERT INTO gigsweep_django_backend_unavailability VALUES(1,'2024-02-28','Unavailable','Holiday',2);
CREATE TABLE IF NOT EXISTS gigsweep_django_backend_artist (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) NULL,
    password VARCHAR(50) NULL,
    phone_number VARCHAR(20) NULL,
    bio TEXT NULL,
    summary VARCHAR(100) NULL,
    genre VARCHAR(50) NULL,
    country VARCHAR(50) NULL,
    county VARCHAR(100) NULL,
    type_of_artist VARCHAR(50) NULL,
    user_type VARCHAR(50) NULL,
    image VARCHAR(100) NULL,
    featured_artist BOOLEAN NOT NULL,
    facebook VARCHAR(200) NULL,
    twitter VARCHAR(200) NULL,
    youtube VARCHAR(200) NULL,
    artist_membership_type INT NULL,
    gigging_distance VARCHAR(200) NOT NULL,
    upcoming_gigs TEXT NULL,
    artist_name VARCHAR(200) NULL,
    CHECK (JSON_VALID(upcoming_gigs) OR upcoming_gigs IS NULL)
);
INSERT INTO gigsweep_django_backend_artist VALUES(2,'cancelthetransmissionuk@outlook.com','ctt123456','07902598774',replace(replace('Cancel The Transmission are a Welsh hard rock band, formed in Caerphilly in 2015. The band consists of lead vocalist and rhythm guitarist Justin Crowe, lead guitarist Josh Thomas, bassist Carl Oag and drummer Ash Preece.\r\n\r\nWith their goal from the very beginning of bringing rock music back to the mainstream, Cancel The Transmission are poised to rip the veil from the face of today’s air-brushed music scene. By taking cues from classic rock icons such as Guns N'' Roses, AC/DC and Aerosmith, as well as pulling from modern rock heavyweights such as The Darkness, Alter Bridge, and The Treatment, Cancel The Transmission have developed a style and sound that expresses feel-good hard rock anthems, loaded with raunchy riffs and infectious hooks.','\r',char(13)),'\n',char(10)),'Rock and roll, simple as that.','Rock','Wales','Caerphilly','Full band','Artist','user_profile_images/artist_profile_images/LIVE_IT_UP_ARTWORK_ijQRpxq.png',0,'https://www.facebook.com/CancelTheTransmissionUK','https://mobile.twitter.com/CTTBANDUK','https://www.youtube.com/@cancelthetransmissionoffic4551',1,'',NULL,'Cancel The Transmission');
INSERT INTO gigsweep_django_backend_artist VALUES(51,'Testartist123@email.com','testartistrock','07902598774','Txvybguhni vfybguhexcrtvybguh xe crdtfvybgu drdctfvygb txrctrctvyb','Erdctfvygbuhn',NULL,'Wales','Caerphilly','Full band','Artist','',0,'Xerctvynbu','E45drf6tg7yh8','Xerctvybgu',1,'',NULL,'Test Artist');
INSERT INTO gigsweep_django_backend_artist VALUES(54,'keaneband@gmail.com','keaneband','07989123123','Keane are an English alternative rock band from Battle, East Sussex, formed in 1995. They met while at Tonbridge School together. The band currently comprises Tom Chaplin (lead vocals, electric/acoustic guitar, piano), Tim Rice-Oxley (piano, synthesisers, bass guitar, backing vocals), Richard Hughes (drums, percussion, backing vocals), and Jesse Quin (bass guitar, acoustic/electric guitar, backing vocals). Their original line-up included founder and guitarist Dominic Scott, who left in 2001.','English alternative rock band from Battle, East Sussex, formed in 1995.','Rock','England','East Sussex','Full band','Artist','user_profile_images/artist_profile_images/keane.jpeg',1,'https://www.facebook.com/keane','https://twitter.com/keaneofficial/status/1738167513903722691','https://www.youtube.com/channel/UC_5iLk7KvfsHW4CIWFyzasg',1,'',NULL,'Keane');
INSERT INTO gigsweep_django_backend_artist VALUES(55,'thestruts@gmail.com','thestrutsband','07890123123',replace(replace('The Struts are a British rock band formed in Derby, Derbyshire in 2012. The band consists of lead vocalist Luke Spiller, guitarist Adam Slack, bassist Jed Elliott, and drummer Gethin Davies.\r\n\r\nThe band has cited its influences as: Queen, The Darkness, The Rolling Stones, Aerosmith, Def Leppard, The Killers, The Smiths, Oasis, the Libertines, Michael Jackson, The Strokes, The Vaccines and My Chemical Romance.','\r',char(13)),'\n',char(10)),'The Struts are a British rock band formed in Derby, Derbyshire in 2012.','Rock','England','Derbyshire','Full band','Artist','user_profile_images/artist_profile_images/thestrutspp.jpeg',1,'https://www.facebook.com/thestruts','https://twitter.com/TheStruts?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor','https://www.youtube.com/channel/UCfoba7dC3rJrEirb70tS8UA',1,'',NULL,'The Struts');
INSERT INTO gigsweep_django_backend_artist VALUES(56,'tdc@gmail.com','tdcrockband','07567123123','Those Damn Crows are a Welsh rock band formed in 2014 in Bridgend, Wales. The band quickly started building a loyal following and gaining traction through appearances at the likes of Steelhouse Festival,[2] and receiving airplay on BBC Radio Wales[3] as well as being declared "Ones to Watch" by the UK''s Planet Rock radio station in November 2017[4] and "New Band of the Week" in Metal Hammer magazine in 2018.[5] The band signed a worldwide, multi-album deal with Nottingham-based independent record label Earache Records[1] on 14 May 2018 and released their debut album Murder and the Motive on 5 October 2018. The album landed at number 5 on the Official UK Rock & Metal Albums Chart[6] and number 5 on the Independent Album Breakers Chart.[7] (The album had previously been released by the band in 2016 as a self-financed project with several different tracks. This copy is highly sought after by fans.)','Those Damn Crows are a Welsh rock band formed in 2014 in Bridgend, Wales.','Rock','Wales','Bridgend','Full band','Artist','user_profile_images/artist_profile_images/tdcpp.jpeg',1,'https://www.facebook.com/thosedamncrows','https://twitter.com/ThoseDamnCrows','https://www.youtube.com/channel/UCHO76bPOIXQERW6k1XVbUXA',1,'',NULL,'Those Damn Crows');
CREATE TABLE IF NOT EXISTS gigsweep_django_backend_venue (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) NULL,
    password VARCHAR(50) NULL,
    phone_number VARCHAR(20) NULL,
    address TEXT NULL,
    bio TEXT NULL,
    country VARCHAR(50) NULL,
    county VARCHAR(100) NULL,
    type_of_act VARCHAR(100) NULL,
    user_type VARCHAR(50) NULL,
    facebook VARCHAR(200) NULL,
    twitter VARCHAR(200) NULL,
    youtube VARCHAR(200) NULL,
    venue_membership_type INT NULL,
    image VARCHAR(100) NULL,
    venue_name VARCHAR(100) NULL
);
INSERT INTO gigsweep_django_backend_venue VALUES(1,'thedollshouse@gmail.com','dollshouserock','01495 213300','The Dolls House, Alma St, Abertillery, United Kingdom, NP13 1QA','The Dolls House Wales is a Pub in Abertillery with live music every weekend and a great atmosphere! Home of the legendary SlugFest.','Wales','Blaenau Gwent','Original Music','Venue','https://www.facebook.com/TheDollsHouseAbertillery/','https://twitter.com/dollshousewales','www.youtube.com/thedollshouse',2,'user_profile_images/venue_profile_images/dollshousepp.jpg','The Dolls House');
INSERT INTO gigsweep_django_backend_venue VALUES(18,'Ctyuhn@email.com','crtvvtyu','098767','Defvygbuhnijscribe','Crauhnijmb','England','Berkshire','Original Music','Venue','Rctybguhn','Xcbtvyguhn','Rctvyhnbgu',2,'','Rctvfygbuh');
INSERT INTO gigsweep_django_backend_venue VALUES(19,'Bwh@email.com','bwhbedwas','09876234234','1 Street, Bedwas','Hjguygikghbjkhiukjnkhghjh','Wales','Caerphilly','Both','Venue','https://www.facebook.com/BedwasHall','https://x.com/bedwashall','https://www.youtube.com/results?search_query=bedwas+workmen%27s+hall',2,'user_profile_images/venue_profile_images/Bedwas-Workmens-Hall.jpg','Bedwas Workmen’s Hall');
CREATE TABLE IF NOT EXISTS gigsweep_django_backend_artistgigapplication (
    id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    artist_id BIGINT NULL,
    artist_gig_id BIGINT NULL,
    message TEXT NULL,
    original_artist_id BIGINT NULL,
    venue_id BIGINT NULL,
    status VARCHAR(200) NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES gigsweep_django_backend_artist(id),
    FOREIGN KEY (artist_gig_id) REFERENCES gigsweep_django_backend_artistlistedgig(id),
    FOREIGN KEY (original_artist_id) REFERENCES gigsweep_django_backend_artist(id),
    FOREIGN KEY (venue_id) REFERENCES gigsweep_django_backend_venue(id)
);
INSERT INTO gigsweep_django_backend_artistgigapplication VALUES(22,54,40,'jyguytguifyukfvyujgv',2,19,'Active');
INSERT INTO gigsweep_django_backend_artistgigapplication VALUES(23,55,40,'pioiyufuhbkgkujh',2,19,'Active');
INSERT INTO gigsweep_django_backend_artistgigapplication VALUES(24,56,40,'qqqwrtdfginytugyhuyh',2,19,'Active');
CREATE TABLE IF NOT EXISTS "gigsweep_django_backend_artistnotification" (
    "id" integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    "message" text NOT NULL,
    "is_read" bool NOT NULL,
    "created_at" datetime NOT NULL,
    "artist_id" bigint NOT NULL REFERENCES "gigsweep_django_backend_artist" ("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "gigsweep_django_backend_artistlistedgig" (
    "id" integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    "date_of_gig" date NULL,
    "country_of_venue" varchar(100) NOT NULL,
    "genre_of_gig" varchar(50) NULL,
    "type_of_gig" varchar(50) NULL,
    "type_of_artist" varchar(50) NULL,
    "payment" integer NULL,
    "user_type" varchar(50) NULL,
    "num_applications" integer unsigned NOT NULL CHECK ("num_applications" >= 0),
    "description" text NULL,
    "artist_id" bigint NULL REFERENCES "gigsweep_django_backend_artist" ("id") DEFERRABLE INITIALLY DEFERRED,
    "venue_name" varchar(100) NULL,
    "venue_id" bigint NULL REFERENCES "gigsweep_django_backend_venue" ("id") DEFERRABLE INITIALLY DEFERRED,
    "status" varchar(200) NOT NULL
);
INSERT INTO gigsweep_django_backend_artistlistedgig VALUES(40,'2024-08-01','Wales','Rock','Covers','Full band',300,'Artist',3,'Due to a scheduling conflict, our band can no longer perform at this event. We’re looking for another band to take our place and deliver a great performance. It’s a fantastic opportunity to play at a renowned venue. If your band is interested, please apply!',2,'Bedwas Workmen’s Hall',19,'Active');
INSERT INTO gigsweep_django_backend_artistlistedgig VALUES(44,'2024-12-13','Wales','Rock','Original Music','Full band',300,'Artist',0,'poiuytfghjklkjhfvbjnk',54,'The Dolls House',1,'Active');
CREATE TABLE IF NOT EXISTS "gigsweep_django_backend_venuenotification" ("id" integer NOT NULL PRIMARY KEY AUTO_INCREMENT, "message" text NOT NULL, "is_read" bool NOT NULL, "created_at" datetime NOT NULL, "venue_id" bigint NOT NULL REFERENCES "gigsweep_django_backend_venue" ("id") DEFERRABLE INITIALLY DEFERRED, "notification_type" varchar(200) NOT NULL, "if_gig_advertised_by_artist" integer NULL, "if_venue_made_gig" integer NULL);
INSERT INTO gigsweep_django_backend_venuenotification VALUES(18,'The artist Cancel The Transmission has advertised their gig on 2024-07-28.',0,'2024-07-14 01:42:47.551867',19,'GIG_TRANSFER',NULL,NULL);
INSERT INTO gigsweep_django_backend_venuenotification VALUES(21,'Test 1',0,'2024-07-15 00:29:13.034655',19,'TEST',NULL,NULL);
INSERT INTO gigsweep_django_backend_venuenotification VALUES(22,'Test 2',0,'2024-07-15 00:29:26.894342',19,'TEST',NULL,NULL);
INSERT INTO gigsweep_django_backend_venuenotification VALUES(23,'Test 3',0,'2024-07-15 00:30:25.685122',19,'TEST',NULL,NULL);
INSERT INTO gigsweep_django_backend_venuenotification VALUES(24,'Test 4',0,'2024-07-15 00:42:44.903488',19,'TEST',NULL,NULL);
INSERT INTO gigsweep_django_backend_venuenotification VALUES(26,'Test 5',0,'2024-07-15 00:47:05.349047',19,'TEST',NULL,NULL);
INSERT INTO gigsweep_django_backend_venuenotification VALUES(27,'The artist Cancel The Transmission has advertised their gig on 2024-08-01.',0,'2024-07-17 16:51:31.952631',19,'GIG_TRANSFER',40,NULL);
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('django_migrations',56);
INSERT INTO sqlite_sequence VALUES('django_admin_log',252);
INSERT INTO sqlite_sequence VALUES('django_content_type',20);
INSERT INTO sqlite_sequence VALUES('auth_permission',80);
INSERT INTO sqlite_sequence VALUES('auth_group',0);
INSERT INTO sqlite_sequence VALUES('auth_user',1);
INSERT INTO sqlite_sequence VALUES('gigsweep_django_backend_membershipoptions',4);
INSERT INTO sqlite_sequence VALUES('gigsweep_django_backend_newslettersignup',13);
INSERT INTO sqlite_sequence VALUES('gigsweep_django_backend_unavailability',1);
INSERT INTO sqlite_sequence VALUES('gigsweep_django_backend_artist',56);
INSERT INTO sqlite_sequence VALUES('gigsweep_django_backend_venue',19);
INSERT INTO sqlite_sequence VALUES('gigsweep_django_backend_artistgigapplication',24);
INSERT INTO sqlite_sequence VALUES('gigsweep_django_backend_artistlistedgig',44);
INSERT INTO sqlite_sequence VALUES('gigsweep_django_backend_venuenotification',28);
CREATE UNIQUE INDEX auth_group_permissions_group_id_permission_id_uniq ON auth_group_permissions (group_id, permission_id);
CREATE INDEX auth_group_permissions_group_id ON auth_group_permissions (group_id);
CREATE INDEX auth_group_permissions_permission_id ON auth_group_permissions (permission_id);
CREATE UNIQUE INDEX auth_user_groups_user_id_group_id_uniq ON auth_user_groups (user_id, group_id);
CREATE INDEX auth_user_groups_user_id ON auth_user_groups (user_id);
CREATE INDEX auth_user_groups_group_id ON auth_user_groups (group_id);
CREATE UNIQUE INDEX auth_user_user_permissions_user_id_permission_id_uniq ON auth_user_user_permissions (user_id, permission_id);
CREATE INDEX auth_user_user_permissions_user_id ON auth_user_user_permissions (user_id);
CREATE INDEX auth_user_user_permissions_permission_id ON auth_user_user_permissions (permission_id);
CREATE INDEX django_admin_log_content_type_id ON django_admin_log (content_type_id);
CREATE INDEX django_admin_log_user_id ON django_admin_log (user_id);
CREATE UNIQUE INDEX django_content_type_app_label_model_uniq ON django_content_type (app_label, model);
CREATE UNIQUE INDEX auth_permission_content_type_id_codename_uniq ON auth_permission (content_type_id, codename);
CREATE INDEX auth_permission_content_type_id ON auth_permission (content_type_id);
CREATE INDEX django_session_expire_date ON django_session (expire_date);
CREATE INDEX gigsweep_django_backend_venuelistedgig_venue_id ON gigsweep_django_backend_venuelistedgig (venue_id);
CREATE INDEX gigsweep_django_backend_venuegigapplication_artist_id ON gigsweep_django_backend_venuegigapplication (artist_id);
CREATE INDEX gigsweep_django_backend_venuegigapplication_venue_gig_id ON gigsweep_django_backend_venuegigapplication (venue_gig_id);
CREATE INDEX gigsweep_django_backend_unavailability_artist_id ON gigsweep_django_backend_unavailability (artist_id);
CREATE INDEX gigsweep_django_backend_artistgigapplication_artist_id ON gigsweep_django_backend_artistgigapplication (artist_id);
CREATE INDEX gigsweep_django_backend_artistgigapplication_artist_gig_id ON gigsweep_django_backend_artistgigapplication (artist_gig_id);
CREATE INDEX gigsweep_django_backend_artistgigapplication_original_artist_id ON gigsweep_django_backend_artistgigapplication (original_artist_id);
CREATE INDEX gigsweep_django_backend_artistgigapplication_venue_id ON gigsweep_django_backend_artistgigapplication (venue_id);
CREATE INDEX gigsweep_django_backend_artistnotification_artist_id ON gigsweep_django_backend_artistnotification (artist_id);
CREATE INDEX gigsweep_django_backend_artistlistedgig_artist_id ON gigsweep_django_backend_artistlistedgig (artist_id);
CREATE INDEX gigsweep_django_backend_artistlistedgig_venue_id ON gigsweep_django_backend_artistlistedgig (venue_id);
CREATE INDEX gigsweep_django_backend_venuenotification_venue_id ON gigsweep_django_backend_venuenotification (venue_id);
COMMIT;
