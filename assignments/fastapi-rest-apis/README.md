# 📘 Assignment: FastAPI REST APIs

## 🎯 Objective

Build a REST API using the FastAPI framework that exposes endpoints for creating, reading, updating, and deleting items. Students will learn API routing, request handling, response modeling, and simple data storage in Python.

## 📝 Tasks

### 🛠️	Create the FastAPI Application

#### Description

Set up a FastAPI app with endpoints to manage a list of sample items. Implement routes for adding new items, retrieving all items, retrieving a single item by ID, updating an item, and deleting an item.

#### Requirements
Completed program should:

- Define a FastAPI app in `starter-code.py`.
- Create the following routes:
  - `GET /items` to return all items.
  - `GET /items/{item_id}` to return a single item by ID.
  - `POST /items` to add a new item.
  - `PUT /items/{item_id}` to update an existing item.
  - `DELETE /items/{item_id}` to remove an item.
- Use Python data structures (e.g., list or dict) to store items in memory.
- Validate input data with Pydantic models.
- Return appropriate HTTP status codes for success and error cases.

### 🛠️	Test the API Endpoints

#### Description

Verify the FastAPI application by sending example requests and checking the responses.

#### Requirements
Completed program should:

- Include sample cURL or HTTP requests in comments or documentation.
- Confirm that `GET /items` returns the current item list.
- Confirm that `POST /items` creates a new item with valid request data.
- Confirm that `PUT /items/{item_id}` updates an item field and returns the updated item.
- Confirm that `DELETE /items/{item_id}` removes the item and returns a confirmation.
