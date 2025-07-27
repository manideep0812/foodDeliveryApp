# Food Delivery App

## Overview

This is a Python-based simulation of a food delivery application, designed as a learning project to explore and implement core software engineering concepts using object-oriented programming and design patterns. The application models the essential features of a modern food delivery platform, demonstrating how various components interact and can be extended in a scalable way.

## Purpose

- **Learning Design Patterns:** The project’s primary goal is to gain hands-on experience with key design patterns such as Strategy, Template Method, and Decorator.
- **System Design Practice:** Practice breaking down a real-world problem (food delivery) into modules, classes, and interfaces with clean abstractions.
- **Python Proficiency:** Improve proficiency in Python, especially with OOP and abstract base classes (ABC).

## Features

### 1. Restaurant Management
- **Admin Operations:** Restaurant admins can add or remove menu items.
- **Dynamic Availability:** Restaurants and menu items can be toggled between available/unavailable.

### 2. Menu and Customization
- **Menu Items:** Each menu item has attributes like price, rating, description, category, etc.
- **Decorator Pattern:** Customizations (like extra cheese) are implemented as decorators, allowing flexible extension of core menu items.

### 3. Food Browsing
- **Strategy Pattern:** Users can browse menu items with different sorting strategies (by price, rating, delivery time).

### 4. Cart and Order
- **Cart Management:** Add or remove items, dynamic calculation of total.
- **Order Lifecycle:** Supports order placement, status updates (Placed, Prepared, Out-for-Delivery, Delivered, Cancelled).

### 5. Payment Processing
- **Template Method & Strategy Patterns:**
  - Payment methods (UPI, Credit Card) are implemented using the Template Method pattern.
  - Payment strategy can be selected dynamically.
- **Status Tracking:** Payment status updates and user notifications.

## Architecture Highlights (Design Patterns Used)

- **Strategy:** For food browsing (sort by price, rating, delivery time) and payment processing (UPI, Credit Card).
- **Template Method:** For payment operations (validate, authenticate, deduct, notify).
- **Decorator:** For menu item customization (e.g., adding cheese).

## Main Learnings

- **Applying OOP Concepts:** Encapsulation, inheritance, and abstraction are used extensively.
- **Design Patterns in Practice:** Real-world use cases for common design patterns.
- **Separation of Concerns:** Each module (customer, restaurant, menu, cart, order, payment) has a single responsibility.
- **Extensibility:** The system is designed for easy addition of new features (e.g., new payment strategies, menu customizations).
- **Testability:** The modular structure allows for easy unit testing.

## Code Structure

```
foodDeliveryApp/
│
├── customer/           # Customer management
├── restaurent/         # Restaurant and admin management
├── menu/               # Menu items and decorators
├── foodBrowsing/       # Browsing and sorting strategies
├── order/              # Order lifecycle and status
├── cart/               # Cart management
├── payment/            # Payment processing, strategies, templates
├── enums.py            # Enum definitions for order and payment status
├── main.py             # Example usage and app workflow
├── generateID.py       # Utility for unique ID generation
└── README.md           # This file
```

## Example Workflow

1. **Restaurant Admin adds menu items.**
2. **Customer browses and sorts menu.**
3. **Customer customizes order and adds to cart.**
4. **Order is placed and status updated through lifecycle.**
5. **Payment is processed using selected strategy.**

## How to Run

This is a simulation for learning purposes, not a production-ready web or mobile app. To see the flow, run `main.py` and follow the code comments for the sequence of operations.

```bash
python main.py
```

## Potential Future Extensions

- User authentication and authorization
- Integration with a database for persistent storage
- REST API or web UI
- More payment and browsing strategies
- Real-time order tracking

## Author

- [manideep0812](https://github.com/manideep0812)

---

> **Note:** This project is for educational purposes, focusing on design and code structure over production-readiness.
