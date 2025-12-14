# Blockchain for Python Developers

A small learning project exploring basic blockchain concepts implemented in Python.

## Project

This repository contains a minimal implementation of blockchain-related code intended for educational purposes. It's designed to help Python developers understand blocks, hashing, and simple chain mechanics.

## Files & Directories

- `Block.py` — main script demonstrating block structure and chaining.
- `verify_message.py` — RSA signature verification example using cryptography.
- `mariakey.pub`, `nelsonkey.pub`, `skykey.pub` — example public key files used in exercises or examples.
- `Python Fast API example/` — FastAPI web application learning project with a basic counter server.

## Requirements

- Python 3.8 or newer
- `cryptography` (used for key handling and cryptographic examples)
- `fastapi` and `uvicorn` (for the FastAPI web example)

Install all dependencies:

```sh
pip install cryptography fastapi uvicorn
```

## Quick start

### Blockchain examples

1. (Optional) Create and activate a virtual environment:

```sh
python3 -m venv .venv
. .venv/bin/activate
```

2. Install dependencies:

```sh
pip install cryptography fastapi uvicorn
```

3. Run blockchain scripts:

```sh
python3 Block.py
python3 verify_message.py
```

### FastAPI web example

1. Navigate to the FastAPI example directory:

```sh
cd "Python Fast API example"
```

2. Start the development server:

```sh
uvicorn main:app --reload
```

3. Visit the API docs:
   - Swagger UI: `http://127.0.0.1:8000/docs`
   - ReDoc: `http://127.0.0.1:8000/redoc`

## Learning goals

- Understand what a block is and what data it contains
- See how hashing links blocks together
- Explore simple validation rules for a chain

## Contributing

This is a personal learning project. Feel free to open issues or send pull requests with improvements or exercises.

## License

No license specified. Use for learning and personal experiments.
