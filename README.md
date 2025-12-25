# 🧩 File Type Identifier

**File Type Identifier** is a lightweight and efficient Python tool designed to automatically detect and classify file types based on their binary signatures (magic numbers) — not just their extensions.
Whether you're managing large data repositories, handling uploads, or building security workflows, this tool ensures reliable and accurate file identification.

## 🚀 Features

1. 🔍 **Accurate Detection** — Identifies file formats using file headers and byte patterns.
2. ⚙️ **Extension-Independent** — Works even if the file extension is missing or incorrect.
3. 💡 **Pythonic & Lightweight** — No heavy dependencies; fast and minimal footprint.

## 🧠 How It Works

The tool reads the first few bytes of a file (the magic number), compares it against a signature database, and returns the detected file type.
Unlike traditional methods that rely on filenames or MIME types, this approach provides higher accuracy and better security for automation pipelines.

## Installation

**Cloning Repository**

    git clone https://github.com/Cyber-XS/MagicEYE.git

**Moving to MagicEYE**

    cd MagicEYE

**Installing Requirments for Arch based Linux**

    chmod +x arch.sh
    ./arch.sh

**Installing Requirments on Debian based Linux**

    chmod +x debian.sh
    ./debian.sh

**Usage of MagicEYE**

    chmod +x magiceye.py
    python magiceye.py

Enter your file Path

## 🙏 Thanks for using MagicEYE
