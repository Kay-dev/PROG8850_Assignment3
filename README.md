# PROG8850 Assignment 3
A web application with MySQL, Python, and Selenium testing.

## Prerequisites

- Python 3.x
- MySQL Server
- Chrome browser (for Selenium tests)
- ChromeDriver (compatible with your Chrome version)

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Database Setup

Start MySQL service:

```bash
sudo service mysql start
```

Create and initialize the database:

```bash
# Login to MySQL
mysql -u root -p

# Or on some systems
sudo mysql -u root
```

Run the database initialization script:

```sql
source database.sql
```

### 3. Configure MySQL Connection Parameters

Before running the application and tests, you need to modify the MySQL connection parameters in both files to match your environment:

#### In app.py:

```python
def get_db_connection():
    return mysql.connector.connect(
        user='root',           # Change to your MySQL username
        password='admin',      # Change to your MySQL password
        host='localhost',      # Change if your MySQL server is on a different host
        database='firstdatabase'  # Change if you used a different database name
    )
```

#### In seleniumtest.py:

```python
db = mysql.connector.connect(
    user='root',           # Change to your MySQL username
    password='admin',    # Change to your MySQL password
    host='localhost',      # Change if your MySQL server is on a different host
    database='firstdatabase'  # Change if you used a different database name
)
```

## Running the Application

Start the Flask application:

```bash
python app.py
```

The application will be available at http://127.0.0.1:5000/login

## Running Selenium Tests

Ensure you have Chrome and ChromeDriver installed. The ChromeDriver version should match your Chrome browser version.

To run the Selenium test:

```bash
python seleniumtest.py
```