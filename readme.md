# Finance Data Processing and Access Control Backend

## Overview

This project is a backend system designed to manage financial data with structured APIs, role-based access design, and analytical dashboard capabilities.

It simulates a real-world finance dashboard backend where users can manage transactions and retrieve meaningful financial insights.

---

## Key Features

### User Management

* Create and manage users
* Assign roles: Admin, Analyst, Viewer (currently stored, not enforced via middleware)
* Prevent duplicate email registration
* Track user status (active/inactive)

---

### Financial Records Management

* Add financial transactions (income and expense)
* Store details: amount, category, date, and notes
* Retrieve all records
* Filter records dynamically:

  * By type (income or expense)
  * By category

---

### Dashboard Analytics

* Total income calculation
* Total expense calculation
* Net balance computation
* Category-wise financial summary

These APIs simulate real dashboard data aggregation logic.

---

### Validation and Error Handling

* Input validation using Pydantic
* Custom error responses for invalid data
* Type enforcement (income or expense)
* Duplicate user prevention

---

## Design Approach

The system is designed with clear separation of concerns:

* Models: Define database structure using SQLAlchemy
* Schemas: Handle data validation using Pydantic
* Routes: Define API endpoints
* Database Layer: SQLite integration using ORM

Focus was on:

* Clean architecture
* Maintainable code structure
* Logical API design

---

## Tech Stack

* FastAPI – Backend framework
* SQLite – Lightweight database
* SQLAlchemy – ORM for database operations
* Pydantic – Data validation

---

## API Endpoints

### Users

* POST /users/ → Create user
* GET /users/ → Get all users

---

### Records

* POST /records/ → Add transaction
* GET /records/ → Get all records
* GET /records/?type=expense → Filter by type
* GET /records/?category=food → Filter by category

---

### Dashboard

* GET /dashboard/summary → Income, Expense, Balance
* GET /dashboard/category-summary → Category-wise totals

---

## How to Run

```bash
pip install fastapi uvicorn sqlalchemy pydantic
uvicorn app.main:app --reload
```
After running the server, you can verify the application using the root endpoint:

http://127.0.0.1:8000/

To explore and test all available APIs, use the interactive API documentation provided by FastAPI:

http://127.0.0.1:8000/docs

---

## Assumptions

* Authentication is not implemented in this version
* Financial records are associated with a default user (user_id = 1)
* SQLite is used for simplicity and quick setup

---

## Future Improvements

* JWT-based authentication
* Full role-based access control enforcement (currently roles are not enforced at API level)
* Pagination for large datasets
* Advanced analytics such as monthly trends
* Deployment to a cloud platform
* Complete role-based access control enforcement (RBAC)

---

## Highlights

* Designed beyond basic CRUD operations
* Includes real-world financial analytics logic
* Clean and modular backend architecture
* Scalable and extendable design

---

## Conclusion

This project demonstrates backend development skills including API design, data modeling, validation, and business logic implementation. It reflects a practical approach to building scalable backend systems for real-world applications.
