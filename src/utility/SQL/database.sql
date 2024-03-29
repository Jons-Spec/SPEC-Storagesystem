-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS `spec-storage`;

-- Use the database
USE `spec-storage`;

-- Create the User table
CREATE TABLE IF NOT EXISTS `User` (
    `user_id` INT AUTO_INCREMENT PRIMARY KEY,
    `username` VARCHAR(255) NOT NULL,
    `password` VARCHAR(255) NOT NULL,
    `is_admin` BOOLEAN NOT NULL DEFAULT FALSE
);

-- Create the Category table
CREATE TABLE IF NOT EXISTS `Category` (
    `category_id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `description` TEXT
);

-- Create the Item table
CREATE TABLE IF NOT EXISTS `Item` (
    `item_id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `description` TEXT,
    `category_id` INT,
    `selling_price` DECIMAL(10, 2) NOT NULL,
    `quantity` INT NOT NULL,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (`category_id`) REFERENCES `Category`(`category_id`)
);

-- Create the Transactions table
CREATE TABLE IF NOT EXISTS `Transactions` (
    `transaction_id` INT AUTO_INCREMENT PRIMARY KEY,
    `item_id` INT,
    `quantity` INT NOT NULL,
    `transaction_type` ENUM('IN', 'OUT') NOT NULL,
    `transaction_date` DATE NOT NULL,
    `profit` DECIMAL(10, 2),
    FOREIGN KEY (`item_id`) REFERENCES `Item`(`item_id`)
);
