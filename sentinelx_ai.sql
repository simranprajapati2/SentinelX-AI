-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3307
-- Generation Time: Jun 30, 2026 at 08:11 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sentinelx_ai`
--

-- --------------------------------------------------------

--
-- Table structure for table `activity_logs`
--

CREATE TABLE `activity_logs` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `activity` text DEFAULT NULL,
  `ip_address` varchar(100) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `activity_logs`
--

INSERT INTO `activity_logs` (`id`, `user_id`, `activity`, `ip_address`, `created_at`) VALUES
(5, 7, 'User Logged In', NULL, '2026-06-24 03:23:20'),
(6, 7, 'User Logged In', NULL, '2026-06-24 05:12:07'),
(7, 7, 'User Logged In', NULL, '2026-06-24 05:30:47'),
(8, 7, 'User Logged In', NULL, '2026-06-24 05:42:43'),
(9, 7, 'User Logged In', NULL, '2026-06-24 06:25:39'),
(10, 7, 'User Logged Out', NULL, '2026-06-24 06:28:52'),
(11, 7, 'User Logged In', NULL, '2026-06-24 06:33:08'),
(12, 7, 'User Logged In', NULL, '2026-06-24 06:51:08'),
(13, 7, 'User Logged In', NULL, '2026-06-24 10:20:35'),
(14, 7, 'User Logged Out', NULL, '2026-06-24 10:29:55'),
(15, 7, 'User Logged In', NULL, '2026-06-24 12:00:32'),
(16, 7, 'User Logged In', NULL, '2026-06-24 12:11:09'),
(17, 7, 'User Logged In', NULL, '2026-06-24 12:41:28'),
(18, 7, 'User Logged In', NULL, '2026-06-24 13:01:16'),
(19, 7, 'User Logged In', NULL, '2026-06-25 11:35:20'),
(20, 7, 'User Logged In', NULL, '2026-06-25 12:25:56'),
(21, 7, 'User Logged In', NULL, '2026-06-25 12:40:24'),
(22, 7, 'Failed Login Attempt', NULL, '2026-06-26 00:27:57'),
(23, 7, 'User Logged In', NULL, '2026-06-26 00:28:21'),
(24, 7, 'User Logged In', NULL, '2026-06-26 01:08:14'),
(25, 7, 'User Logged In', NULL, '2026-06-26 01:10:47'),
(26, 7, 'User Logged In', NULL, '2026-06-26 01:12:55'),
(27, 7, 'User Logged In', NULL, '2026-06-26 01:19:59'),
(30, 7, 'User Logged In', NULL, '2026-06-26 01:28:53'),
(31, 7, 'User Logged In', NULL, '2026-06-27 01:22:01'),
(32, 7, 'User Logged In', NULL, '2026-06-27 01:40:24'),
(33, 7, 'User Logged In', NULL, '2026-06-27 01:43:29'),
(36, 7, 'Failed Login Attempt', NULL, '2026-06-27 03:44:33'),
(37, 7, 'User Logged In', NULL, '2026-06-27 03:45:25'),
(39, 7, 'User Logged In', NULL, '2026-06-27 03:46:42'),
(41, 7, 'User Logged In', NULL, '2026-06-29 03:11:10'),
(47, 7, 'User Logged In', NULL, '2026-06-29 03:49:26'),
(50, 7, 'Deleted User simran@gmail.com', NULL, '2026-06-29 03:51:46'),
(51, 7, 'Deleted User admin@gmail.com', NULL, '2026-06-29 03:51:52'),
(52, 7, 'User Logged In', NULL, '2026-06-29 03:57:40'),
(53, 7, 'Deleted User prajapatisimran532@gmail.com', NULL, '2026-06-29 03:57:52'),
(54, 7, 'User Logged Out', NULL, '2026-06-29 03:58:04'),
(55, 7, 'User Logged In', NULL, '2026-06-29 04:02:58'),
(56, 7, 'Deleted User prajapatisimran532@gmail.com', NULL, '2026-06-29 04:04:38'),
(57, 7, 'User Logged In', NULL, '2026-06-29 04:35:20'),
(58, 7, 'User Logged In', NULL, '2026-06-29 07:55:45'),
(59, 7, 'User Logged In', NULL, '2026-06-29 12:07:18'),
(60, 7, 'User Logged In', NULL, '2026-06-29 12:10:28'),
(61, 7, 'Failed Login Attempt', NULL, '2026-06-29 12:30:24'),
(62, 7, 'User Logged In', NULL, '2026-06-29 12:30:48'),
(63, 7, 'User Logged Out', NULL, '2026-06-29 12:49:03'),
(64, 7, 'User Logged In', NULL, '2026-06-29 12:49:30'),
(65, 7, 'User Logged In', NULL, '2026-06-29 13:21:23'),
(66, 7, 'User Logged In', NULL, '2026-06-30 00:26:17');

-- --------------------------------------------------------

--
-- Table structure for table `admin_users`
--

CREATE TABLE `admin_users` (
  `id` int(11) NOT NULL,
  `username` varchar(100) DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  `password_hash` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin_users`
--

INSERT INTO `admin_users` (`id`, `username`, `email`, `password_hash`, `created_at`) VALUES
(1, 'admin', 'admin@gmail.com', 'admin123', '2026-06-22 16:53:35');

-- --------------------------------------------------------

--
-- Table structure for table `analysis_history`
--

CREATE TABLE `analysis_history` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `text_analyzed` longtext DEFAULT NULL,
  `prediction` varchar(50) DEFAULT NULL,
  `confidence` float DEFAULT NULL,
  `risk_score` int(11) DEFAULT NULL,
  `file_name` varchar(255) DEFAULT NULL,
  `file_type` varchar(50) DEFAULT NULL,
  `analysis_date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `blocked_domains`
--

CREATE TABLE `blocked_domains` (
  `id` int(11) NOT NULL,
  `domain` varchar(255) DEFAULT NULL,
  `reason` text DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `blocked_domains`
--

INSERT INTO `blocked_domains` (`id`, `domain`, `reason`, `created_at`) VALUES
(1, 'fakejobportal.com', 'Fraud website', '2026-06-21 18:26:19'),
(2, 'scam-bank-login.com', 'Phishing website', '2026-06-21 18:26:19');

-- --------------------------------------------------------

--
-- Table structure for table `notifications`
--

CREATE TABLE `notifications` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `message` text DEFAULT NULL,
  `status` varchar(20) DEFAULT 'Unread',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `is_read` tinyint(1) DEFAULT 0,
  `title` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `notifications`
--

INSERT INTO `notifications` (`id`, `user_id`, `message`, `status`, `created_at`, `is_read`, `title`) VALUES
(4, 7, 'Hello Simran', 'Unread', '2026-06-29 18:50:51', 1, 'Test Notification'),
(5, 7, 'Hello Simran', 'Unread', '2026-06-29 19:12:50', 1, 'Test Notification'),
(6, 7, 'You logged in successfully.', 'Unread', '2026-06-30 00:26:17', 1, 'Login Successful');

-- --------------------------------------------------------

--
-- Table structure for table `otp_codes`
--

CREATE TABLE `otp_codes` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `otp_code` varchar(6) NOT NULL,
  `expires_at` datetime NOT NULL,
  `created_at` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `otp_codes`
--

INSERT INTO `otp_codes` (`id`, `user_id`, `otp_code`, `expires_at`, `created_at`) VALUES
(17, 7, '292271', '2026-06-30 06:13:29', '2026-06-30 06:08:29');

-- --------------------------------------------------------

--
-- Table structure for table `password_reset_tokens`
--

CREATE TABLE `password_reset_tokens` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `token` varchar(255) DEFAULT NULL,
  `expires_at` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `password_reset_tokens`
--

INSERT INTO `password_reset_tokens` (`id`, `user_id`, `token`, `expires_at`, `created_at`) VALUES
(2, 7, 'JDne5LdntzJaGKGhDqg0czbYyTgOzlP7pJHy1CbLUV0', '2026-06-24 09:49:23', '2026-06-24 08:49:23');

-- --------------------------------------------------------

--
-- Table structure for table `prediction_history`
--

CREATE TABLE `prediction_history` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `input_text` text NOT NULL,
  `prediction` varchar(50) DEFAULT NULL,
  `confidence` float DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `prediction_history`
--

INSERT INTO `prediction_history` (`id`, `user_id`, `input_text`, `prediction`, `confidence`, `created_at`) VALUES
(1, 2, '        Work from home.\r\nEarn ₹50,000 per day.\r\nNo experience required.\r\nPay registration fee ₹500.', 'Fraud', 61.24, '2026-06-23 07:32:45'),
(2, 2, '        Work from home.\r\nEarn ₹50,000 per day.\r\nNo experience required.\r\nPay registration fee ₹500.', 'Fraud', 61.24, '2026-06-23 07:42:09'),
(3, 2, '        Software Developer required.\r\n\r\nLocation: Pune.\r\nExperience: 2 years.\r\nSalary: ₹6 LPA.\r\n\r\nSend your resume to hr@company.com', 'Genuine', 55.4, '2026-06-23 07:43:24'),
(4, 2, '        Part time job.\r\nEarn ₹1 lakh per week.\r\nNo interview.\r\nPay ₹1000 registration fee.', 'Fraud', 60.38, '2026-06-23 07:43:43');

-- --------------------------------------------------------

--
-- Table structure for table `reports`
--

CREATE TABLE `reports` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `report_name` varchar(255) DEFAULT NULL,
  `report_path` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reports`
--

INSERT INTO `reports` (`id`, `user_id`, `report_name`, `report_path`, `created_at`) VALUES
(8, 7, 'report_7.xlsx', 'uploads/reports\\report_7.xlsx', '2026-06-24 06:28:24'),
(9, 7, 'report_7.xlsx', 'uploads/reports\\report_7.xlsx', '2026-06-24 06:34:02'),
(10, 7, 'report_7.xlsx', 'uploads/reports\\report_7.xlsx', '2026-06-24 12:01:11'),
(11, 7, 'report_7.xlsx', 'uploads/reports\\report_7.xlsx', '2026-06-29 04:19:05'),
(12, 7, 'report_7.xlsx', 'uploads/reports\\report_7.xlsx', '2026-06-29 04:24:41'),
(13, 7, 'report_7.xlsx', 'uploads/reports\\report_7.xlsx', '2026-06-29 12:10:56'),
(14, 7, 'report_7.xlsx', 'uploads/reports\\report_7.xlsx', '2026-06-30 00:27:55');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `email` varchar(150) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `profile_image` varchar(255) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT 1,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `email_verified` tinyint(1) DEFAULT 0,
  `verification_token` varchar(255) DEFAULT NULL,
  `is_admin` tinyint(1) DEFAULT 0,
  `is_blocked` tinyint(1) DEFAULT 0,
  `failed_login_attempts` int(11) DEFAULT 0,
  `is_locked` tinyint(1) DEFAULT 0,
  `last_login` datetime DEFAULT NULL,
  `full_name` varchar(150) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `bio` text DEFAULT NULL,
  `locked_until` datetime DEFAULT NULL,
  `admin_verified` tinyint(1) DEFAULT 0,
  `admin_otp` varchar(6) DEFAULT NULL,
  `admin_otp_expiry` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `email`, `password_hash`, `profile_image`, `is_active`, `created_at`, `email_verified`, `verification_token`, `is_admin`, `is_blocked`, `failed_login_attempts`, `is_locked`, `last_login`, `full_name`, `phone`, `bio`, `locked_until`, `admin_verified`, `admin_otp`, `admin_otp_expiry`) VALUES
(7, 'd', 'simranprajapati42@gmail.com', '$2b$12$5NzJ8vtf9WGBMP3oW6sLOeA9tCt0Ey38igZVI9GKoDtXWxhdv7g2q', 'download.png', 1, '2026-06-24 03:17:04', 1, NULL, 1, 0, 0, 0, '2026-06-30 05:56:17', 'simran', '985225622223', 'i am simran', NULL, 0, NULL, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `activity_logs`
--
ALTER TABLE `activity_logs`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_activity_user` (`user_id`);

--
-- Indexes for table `admin_users`
--
ALTER TABLE `admin_users`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `analysis_history`
--
ALTER TABLE `analysis_history`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `blocked_domains`
--
ALTER TABLE `blocked_domains`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `domain` (`domain`);

--
-- Indexes for table `notifications`
--
ALTER TABLE `notifications`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `otp_codes`
--
ALTER TABLE `otp_codes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `password_reset_tokens`
--
ALTER TABLE `password_reset_tokens`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `prediction_history`
--
ALTER TABLE `prediction_history`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `reports`
--
ALTER TABLE `reports`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `activity_logs`
--
ALTER TABLE `activity_logs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=67;

--
-- AUTO_INCREMENT for table `admin_users`
--
ALTER TABLE `admin_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `analysis_history`
--
ALTER TABLE `analysis_history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `blocked_domains`
--
ALTER TABLE `blocked_domains`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `notifications`
--
ALTER TABLE `notifications`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `otp_codes`
--
ALTER TABLE `otp_codes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `password_reset_tokens`
--
ALTER TABLE `password_reset_tokens`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `prediction_history`
--
ALTER TABLE `prediction_history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `reports`
--
ALTER TABLE `reports`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `activity_logs`
--
ALTER TABLE `activity_logs`
  ADD CONSTRAINT `activity_logs_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `analysis_history`
--
ALTER TABLE `analysis_history`
  ADD CONSTRAINT `analysis_history_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `notifications`
--
ALTER TABLE `notifications`
  ADD CONSTRAINT `notifications_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `otp_codes`
--
ALTER TABLE `otp_codes`
  ADD CONSTRAINT `otp_codes_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `password_reset_tokens`
--
ALTER TABLE `password_reset_tokens`
  ADD CONSTRAINT `password_reset_tokens_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `reports`
--
ALTER TABLE `reports`
  ADD CONSTRAINT `reports_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
