# 📦 Redis Queue System

This project implements a simple singleton-based Redis-backed queue system in Python.

---

## ⚙️ Requirements

- Redis server running locally or remotely
- Python 3.x
- Redis Python client

Install the required package:

```bash
pip install redis
```

---

## 🧩 Queue Class Overview

The `Queue` class is a singleton that provides simple queue management with Redis.

### Features:

- Singleton pattern ensures a single Redis connection
- Add values to named lists
- Pop values (LIFO or FIFO)
- Fetch and delete all data from all queues
- Track all list names (alerts) added

---

## 🧪 Methods

| Method | Description |
|--------|-------------|
| `push(list_name, value)` | Adds a value to the end of a named Redis list. Adds the list name to an alert set. |
| `pop(list_name, lifo=True)` | Pops a value from the Redis list. LIFO by default (uses `rpop`), FIFO uses `lpop`. |
| `get_alerts()` | Returns all list names that have been added as alerts. |
| `get_list_data(list_name)` | Gets all values from a Redis list and deletes the list. |
| `get_all_data()` | Returns a dictionary of all alerts and their data. Also deletes all lists. |

---

## 🔁 Example: `check_adv`

A sample function to demonstrate usage:

```python
def check_adv():
    for i in range(100):
        q = Queue()
        if i % 5 == 0:
            q.push('alert:1', i)
        elif i % 13 == 0:
            q.push('alert:2', i)
        elif i % 24 == 0:
            q.push('alert:3', i)
        elif i % 22 == 0:
            q.push('alert:4', i)
    print('Done')
```

This function adds numbers 0-99 into different Redis lists depending on the condition.

---

## 🏁 Running the Script

Make sure Redis is running and run the Python file:

```bash
python main.py
```

---

## 📌 Notes

- Ensure Redis is running (`sudo service redis-server start` on Ubuntu).
- This is a basic queue system suitable for lightweight task or alert tracking.
- You can use `get_all_data()` to fetch and clear all stored data in one go.

---