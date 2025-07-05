# 📦 Python Generators – `python-generators-0x00`

## 📚 Project Overview

This project focuses on advanced Python programming, especially **generators**, to build memory-efficient data pipelines. By simulating real-world data processing tasks—like streaming, batch loading, pagination, and aggregation—you'll learn how to handle large datasets with minimal memory usage, improve performance, and write clean, reusable generator-based logic.

---

## 🎯 Learning Objectives

- Understand and implement **Python generator functions** using `yield`
- Process **large datasets** using **lazy evaluation**
- Fetch rows **one by one** or in **batches** from an SQL database
- Simulate **live data feeds** and **pagination**
- Compute aggregate data like **averages** without loading all values into memory
- Use **MySQL** with Python for data-driven applications
- Integrate generator logic with **file streaming**, **SQL queries**, and **batch processing**

---

## 🛠️ Technologies

- Python 3.x
- MySQL
- `mysql-connector-python`
- SQL (DDL & DML)
- `.env` configuration (with `dotenv`)
- Git & GitHub

---

## 📁 Directory Structure

```

python-generators-0x00/
│
├── seed.py                  # Database setup, table creation, and CSV data ingestion
├── 0-main.py                # Initializes DB and inserts sample data
├── 0-stream\_users.py        # Streams user rows one-by-one using a generator
├── 1-main.py                # Uses `islice` to print first 6 users from generator
├── 1-batch\_processing.py    # Streams users in batches & filters by age
├── 2-main.py                # Tests batch processing logic
├── 2-lazy\_paginate.py       # Implements lazy pagination using offset and LIMIT
├── 3-main.py                # Fetches paginated data and prints results
├── 4-stream\_ages.py         # Streams user ages and calculates average
├── user\_data.csv            # Sample data file (UUID, name, email, age)
└── README.md                # Project documentation

````

---

## 🔧 Setup & Usage

1. Install dependencies:
   ```bash
   pip install mysql-connector-python python-dotenv
````

2. Configure `.env` file:

   ```
   HOST=localhost
   PORT=3306
   DB_USER=your_mysql_user
   PASSWORD=your_mysql_password
   ```

3. Seed database and insert CSV data:

   ```bash
   ./0-main.py
   ```

4. Test streaming, batching, and pagination:

   ```bash
   ./1-main.py
   ./2-main.py
   ./3-main.py
   python3 4-stream_ages.py
   ```

---

## 🧪 Tasks Summary

| Task | File                    | Description                                            |
| ---- | ----------------------- | ------------------------------------------------------ |
| 0    | `seed.py`               | Set up the MySQL database and populate it from CSV     |
| 1    | `0-stream_users.py`     | Stream rows from database one-by-one using a generator |
| 2    | `1-batch_processing.py` | Fetch users in batches and process users over age 25   |
| 3    | `2-lazy_paginate.py`    | Implement lazy pagination with offset and yield        |
| 4    | `4-stream_ages.py`      | Stream user ages and compute average using a generator |

---

## ✅ Example Output

```bash
$ ./1-main.py
{'user_id': 'abc...', 'name': 'Jane Doe', 'email': 'jane@example.com', 'age': 32}
...
```

```bash
$ python3 4-stream_ages.py
Average age of users: 49.56
```

---

## 👨🏾‍💻 Author

**Daniel Kwasi Dzrekey**
ALX Software Engineering Program – Backend Track

---

## 📜 License

This project is part of the **ALX Pro Backend Curriculum**.
All rights reserved © 2025 ALX Africa.
