-- Insert fake data into the Category table
INSERT INTO `Category` (`name`, `description`) VALUES
('Electronics', 'Electronic devices and components'),
('Clothing', 'Clothing and apparel'),
('Books', 'Books and reading materials');

-- Insert fake data into the Item table
INSERT INTO `Item` (`name`, `description`, `category_id`, `selling_price`, `quantity`) VALUES
('Laptop', 'High-performance laptop', 1, 1200.00, 10),
('T-shirt', 'Cotton T-shirt', 2, 20.00, 50),
('Smartphone', 'Latest smartphone model', 1, 800.00, 20),
('Jeans', 'Denim jeans', 2, 40.00, 30),
('Book', 'Bestseller novel', 3, 15.00, 100);

-- Insert fake data into the Transactions table
INSERT INTO `Transactions` (`item_id`, `quantity`, `transaction_type`, `transaction_date`, `profit`) VALUES
(1, 5, 'IN', '2024-03-15', NULL),
(2, 10, 'IN', '2024-03-16', NULL),
(3, 3, 'IN', '2024-03-17', NULL),
(4, 8, 'IN', '2024-03-17', NULL),
(5, 20, 'IN', '2024-03-18', NULL),
(1, 2, 'OUT', '2024-03-18', NULL),
(3, 1, 'OUT', '2024-03-18', NULL);
