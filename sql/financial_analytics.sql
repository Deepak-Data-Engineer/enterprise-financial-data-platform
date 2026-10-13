
-- Enterprise Financial Data Integration & Analytics Platform
-- Banking-inspired SQL analytics
-- Source table: clean_transactions
-- SQL dialect: SQLite-compatible

-- 1. Completed transaction summary by customer
SELECT
    customer_id,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount), 2) AS total_transaction_amount
FROM clean_transactions
WHERE status = 'COMPLETED'
GROUP BY customer_id
ORDER BY total_transaction_amount DESC;


-- 2. Transaction volume by transaction type
SELECT
    transaction_type,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount), 2) AS total_amount
FROM clean_transactions
GROUP BY transaction_type
ORDER BY transaction_count DESC;


-- 3. Daily completed transaction trends
SELECT
    transaction_date,
    COUNT(*) AS daily_transaction_count,
    ROUND(SUM(amount), 2) AS daily_transaction_amount
FROM clean_transactions
WHERE status = 'COMPLETED'
GROUP BY transaction_date
ORDER BY transaction_date;


-- 4. Transaction status monitoring
SELECT
    status,
    COUNT(*) AS transaction_count,
    ROUND(
        100.0 * COUNT(*) /
        (SELECT COUNT(*) FROM clean_transactions),
        2
    ) AS percentage
FROM clean_transactions
GROUP BY status
ORDER BY transaction_count DESC;


-- 5. Customer transaction ranking
SELECT
    customer_id,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount), 2) AS total_transaction_amount,
    DENSE_RANK() OVER (
        ORDER BY SUM(amount) DESC
    ) AS customer_rank
FROM clean_transactions
WHERE status = 'COMPLETED'
GROUP BY customer_id;
