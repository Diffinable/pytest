# Pytest Testing Showcase

A demonstration of modern pytest features applied to a FastAPI + SQLAlchemy backend. This project shows how to write clean, maintainable tests for CRUD operations, using fixtures, parametrization, and test isolation.

## Purpose

This repository serves as a portfolio piece to showcase my approach to testing in Python. It covers:

- **Unit tests** – Testing individual service/repository methods.
- **Integration tests** – Verifying database interactions with a real PostgreSQL test database.
- **Pytest features** – Fixtures, conftest.py setup, custom command-line options, and parametrized tests.

## Tech Stack

- **Python** 3.11+
- **FastAPI** (for the underlying API structure, though tests focus on service layer)
- **SQLAlchemy** ORM with PostgreSQL
- **Pytest** with plugins (e.g., `pytest-cov`, `pytest-mock`)
- **Pydantic** for data validation
