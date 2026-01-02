# Fretboard Master 🎸
> A professional-grade Python GUI application for music theory visualization and fretboard mastery.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

## 🎯 Overview
Fretboard Master bridges the gap between music theory and technical execution. Built with Python and CustomTkinter, it allows guitarists to visualize complex scales across the neck using an algorithmic approach to music theory.

## ✨ Key Features
* **Algorithmic Scale Generation:** Uses interval logic to calculate scales rather than hardcoded lists.
* **Dynamic GUI:** Real-time fretboard rendering with dark-mode support.
* **MVC Architecture:** Clean separation of concerns between musical logic and UI components.
* **Interactive Learning:** Quiz mode to test note identification on the fretboard.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **GUI Framework:** CustomTkinter / PyQt6
* **Testing:** Pytest (Unit testing for scale intervals)
* **Packaging:** PyInstaller (for standalone .exe/.app creation)

## 🚀 Installation & Usage
1. Clone the repo: `git clone https://github.com/yourusername/fretboard-master.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `python main.py`

## 🏗️ Architecture
This project follows the **Model-View-Controller (MVC)** design pattern to ensure scalability and maintainability.
- **Model:** Handles interval math and fretboard coordinate mapping.
- **View:** Manages the Canvas rendering and UI event loops.
- **Controller:** Synchronizes user input with musical data output.