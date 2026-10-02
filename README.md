# README.md
# Python Phone Emulator

A lightweight, text-based smartphone emulator written in Python. It simulates a phone with:

- battery status
- signal strength
- memory/storage
- apps
- a simple event loop
- a basic command-line UI

This project is intentionally beginner-friendly and designed as a fun emulator prototype.

## Quick Start

```bash
python main.py
```

## Features

- Virtual phone device with configurable battery, storage, and signal
- Built-in apps: `messages`, `contacts`, `calculator`, and `settings`
- Simple command-based interface
- App launcher and status display
- "Notification" and "battery drain" simulation

## Project Structure

- `main.py` – entry point
- `phone.py` – phone/device logic
- `apps.py` – app definitions
- `README.md` – usage docs

## Example Commands

- `help`
- `status`
- `apps`
- `open messages`
- `open calculator`
- `charge`
- `quit`

## License

MIT
