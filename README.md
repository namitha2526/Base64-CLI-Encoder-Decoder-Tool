# Base64 CLI Encoder/Decoder

A professional-grade Python command-line tool for encoding and decoding files using Base64.  
Designed with clean CLI interface, streaming for large files, and proper error handling.

---

## Features
- Encode any file to Base64
- Decode Base64 back to original file
- Memory-efficient chunk-based processing (handles large files)
- Clean CLI interface using argparse
- Works with both text and binary files
- Built-in error handling
- Includes basic test suite

---

## Tech Stack
- Python 3
- argparse
- base64
- File I/O

---
Decode a file
python base64_tool.py --decode encoded.txt output.txt

Example
python base64_tool.py --encode message.txt encoded.txt
python base64_tool.py --decode encoded.txt decoded.txt

Running Tests
python tests.py

What this project demonstrates

Command-line tool development

File handling (binary + text)

Encoding systems (Base64)

Memory-efficient streaming

Clean code structure

Error handling

Basic test-driven validation

Author

Namitha R
GitHub: https://github.com/namitha2526

