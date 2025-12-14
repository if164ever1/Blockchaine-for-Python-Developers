# Blockchain for Python Developers

A small learning project exploring basic blockchain concepts implemented in Python.

## Project

This repository contains a minimal implementation of blockchain-related code intended for educational purposes. It's designed to help Python developers understand blocks, hashing, and simple chain mechanics.

## Files

- `Block.py` — main script demonstrating block structure and chaining.
- `mariakey.pub`, `nelsonkey.pub`, `skykey.pub` — example public key files used in exercises or examples.

## Requirements

- Python 3.8 or newer
- `cryptography` (used for key handling and examples)

If you don't already have `cryptography` installed, install it with `pip`:

```sh
pip install cryptography
```

## Quick start

1. (Optional) Create and activate a virtual environment:

```sh
python3 -m venv .venv
. .venv/bin/activate
```

2. Install dependencies (only `cryptography` is required for examples that use keys):

```sh
pip install cryptography
```

3. Run the main script:

```sh
python3 Block.py
```

## Learning goals

- Understand what a block is and what data it contains
- See how hashing links blocks together
- Explore simple validation rules for a chain

## Contributing

This is a personal learning project. Feel free to open issues or send pull requests with improvements or exercises.

## License

No license specified. Use for learning and personal experiments.
