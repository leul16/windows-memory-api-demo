# Windows Memory API Demo

A Python project exploring Windows process creation and native API interaction using `ctypes`.

The project demonstrates how Python can interact with Windows system libraries, create a process, retrieve process information, and locate native Windows API functions.

## Features

* Windows API interaction
* Process creation
* Process handles
* Process IDs
* `kernel32.dll` interaction
* `GetModuleHandleA`
* `GetProcAddress`
* `STARTUPINFO`
* `PROCESS_INFORMATION`
* Python `ctypes`

## Requirements

* Windows
* Python 3

No external Python packages are required.

## Run

```bash
python memory_api_demo.py
```

The script creates a temporary Notepad process, retrieves its process information, locates Windows API functions inside `kernel32.dll`, and then closes the process.

## Project Structure

```text
windows-memory-api-demo/
├── memory_api_demo.py
├── .gitignore
└── README.md
```

## Notes

This project is an educational demonstration of Windows process and memory API concepts.

The original research project involved shellcode injection. This public version does not contain shellcode, inject code into another process, modify executable memory, or execute injected payloads.
