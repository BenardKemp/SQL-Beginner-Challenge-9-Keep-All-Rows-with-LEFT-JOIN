# SQL Beginner Challenge #9: Keep All Rows with LEFT JOIN

**Difficulty:** Beginner  
**Estimated time:** 15–20 minutes  
**Concepts:** `LEFT JOIN`, preserving rows, missing relationships  

This challenge explains how to keep all rows from one table when joining tables—even when related data is missing.

---

## 🧠 The Problem

After joining products with suppliers using an `INNER JOIN`, a product manager notices:

> “Some products don’t have a supplier yet. I still want to see **all products**, even if the supplier is missing.”

To solve this, you need to use a `LEFT JOIN`.

---

## 📊 Table Schemas

### `products`

| Column Name | Type | Description |
|------------|------|-------------|
| product_id | INTEGER | Unique product ID |
| name | TEXT | Product name |
| category | TEXT | Product category |
| price | DECIMAL | Product price |
| supplier_id | INTEGER | References `suppliers.supplier_id` (can be NULL) |

---

### `suppliers`

| Column Name | Type | Description |
|------------|------|-------------|
| supplier_id | INTEGER | Unique supplier ID |
| supplier_name | TEXT | Supplier name |

---

## 🧪 Sample Data

### `products`

| product_id | name | category | price | supplier_id |
|-----------:|------|----------|------:|------------:|
| 101 | Wireless Mouse | Accessories | 24.99 | 1 |
| 102 | Mechanical Keyboard | Accessories | 89.00 | 1 |
| 103 | 27-inch Monitor | Displays | 229.99 | 2 |
| 104 | USB-C Hub | Accessories | 34.50 | NULL |

