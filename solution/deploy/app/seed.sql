-- Create Table
CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    reviews_date DATE,
    product_name VARCHAR(255),
    asins VARCHAR(255),
    category VARCHAR(255),
    categories VARCHAR(255),
    rating INT,
    reviews_title VARCHAR(255),
    reviews_text TEXT,
    summary TEXT,
    sentiment VARCHAR(50)
);

-- Example data
INSERT INTO reviews (reviews_date, product_name, asins, category, categories, rating, reviews_title, reviews_text, summary, sentiment) VALUES
('2023-01-01', 'Wireless Mouse', 'B01M8L5Z3Y', 'Electronics', 'Computer Accessories', 5, 'Great Mouse', 'I absolutely love this product! It exceeded my expectations in every way. The quality is top-notch and it works perfectly for my needs. I would highly recommend this to anyone looking for a reliable and high-quality option. Definitely worth the price!', 'Highly recommended', 'positive'),
('2023-02-15', 'Laptop', 'B06X3QKWLG', 'Electronics', 'Computers', 3, 'Average Laptop', 'This product is okay, nothing special. It works as advertised but not great.', 'It works but not impressive', 'neutral'),
('2023-03-20', 'Headphones', 'B07PJV3JPR', 'Electronics', 'Audio', 1, 'Terrible Headphones', 'This is the worst product I have ever purchased. It broke within a week of use and the quality is absolutely terrible. The description was completely misleading and the customer service was unhelpful when I tried to get a refund. I would never recommend this to anyone. A complete waste of money.', 'Do not buy', 'negative');
