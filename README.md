# Cinema-booking-system
A comprehensive cinema booking and seat management system built with FastAPI backend and vanilla JavaScript frontend. The system enables online seat reservations for customers and provides management tools for cinema staff.

## 🎯 Project Overview

This project implements a distributed cinema management system that handles:
- Online seat reservations with conflict resolution
- Multi-threaded client communication
- Role-based access control (Customer, Cashier, Administrator)
- Real-time seat availability management
- Payment processing simulation
- Comprehensive reporting system

## 🏗️ Architecture

The system follows a layered client-server architecture:
- **Presentation Layer**: HTML/CSS/JavaScript frontend
- **Business Logic Layer**: FastAPI REST API
- **Data Access Layer**: SQLAlchemy ORM
- **Data Layer**: MySQL database

## 🚀 Features

### Customer Features
- User registration and authentication
- Browse movie repertoire
- Interactive seat selection
- Online reservation system
- Reservation history
- Payment processing

### Cashier Features
- Ticket sales at the counter
- Reservation management
- Sales reports
- Customer service tools

### Administrator Features
- Movie management (CRUD operations)
- Screening schedule management
- User management
- Comprehensive reporting
- System configuration

## 🛠️ Technology Stack

- **Backend**: Python 3.9+, FastAPI, SQLAlchemy
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Database**: MySQL
- **Authentication**: JWT (JSON Web Tokens)
- **Password Hashing**: bcrypt
- **Testing**: pytest

## 📁 Project Structure
```
Cinema-booking-and-seat-management-system-/
|-- backend/                 # Server code
|   |-- crud/               # CRUD operations
|   |-- routes/             # API endpoints
|   |-- tests/              # Unit tests
|   |-- main.py             # Application entry point
|   |-- models.py           # Database models
|   |-- schemas.py          # Pydantic schemas
|   +-- database.py         # Database configuration
|-- frontend/               # User interface
|   |-- imgs/               # Images and icons
|   |-- *.html              # HTML pages
|   |-- *.js                # JavaScript logic
|   +-- *.css               # CSS styles
```