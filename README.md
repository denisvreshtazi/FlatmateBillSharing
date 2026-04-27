# 💸 FlatmateBillSharing

> A small **command-line tool** that splits a bill between two flatmates **proportionally to the days each one stayed at home** during the period — and emits a printable **PDF report**.

[![Python](https://img.shields.io/badge/python-3.7%2B-blue)]()
[![FPDF](https://img.shields.io/badge/pdf-fpdf-red)]()
[![Try it](https://img.shields.io/badge/try-Replit-orange)](https://replit.com/@DenisVreshtazi/FlatmateSharingBill?embed=1)

---

## 📌 Overview

Splitting a utility bill 50/50 isn't fair if one flatmate was on holiday for two weeks. This script asks for:

- The total bill amount and its period
- Each flatmate's name + days spent at home

…and computes the proportional share each one owes:

```
flatmate_pays = bill.amount · (own_days / (own_days + other_days))
```

Then it generates a clean PDF report named after the period (e.g. `January2023.pdf`).

> 🔁 Companion **web version**: [WebApp-Flatmates-Bill-Share](https://github.com/denisvreshtazi/WebApp-Flatmates-Bill-Share)
> 🚀 **Live demo (Replit):** https://replit.com/@DenisVreshtazi/FlatmateSharingBill?embed=1

## 🧱 Architecture

```
┌─────────────┐
│   main.py   │   ── prompts the user
└──────┬──────┘
       │
       ▼
┌────────────┐    ┌────────────┐
│    Bill    │    │  Flatmate  │
│ (amount,   │    │ (name,     │
│  period)   │    │  days)     │
└────────────┘    └─────┬──────┘
                        │
                        ▼
                  pays(bill, other)
                        │
                        ▼
                  ┌───────────────┐
                  │  PdfReport    │
                  │  .generate()  │
                  └───────┬───────┘
                          │
                          ▼
                    PeriodName.pdf
```

## 🗂️ Project Structure

```
FlatmateBillSharing/
├── main.py            # CLI entry point
├── bill.py            # Bill class
├── flatmate.py        # Flatmate class — pays() math
├── PdfReport.py       # PDF generation (FPDF)
├── design.txt         # Design notes
└── requirements.txt
```

## 🚀 Setup & Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

Key deps:
```
fpdf==1.7.2
filestack-python==3.2.1
requests==2.23.0
```

### 2. Run
```bash
python main.py
```

### 3. Example session
```
What is the total bill amount? 120
What is the bill's period? January 2023
What is the name of the first flatmate? Alice
What is the total number of days of Alice? 25
What is the name of the second flatmate? Bob
What is the total number of days of Bob? 15

Alice pays:  75.0
Bob pays:    45.0
```

→ A file `January2023.pdf` is written to the working directory.

## 🧩 Core Classes

### `Bill` (`bill.py`)
```python
class Bill:
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period
```

### `Flatmate` (`flatmate.py`)
Implements the proportional-pay formula:
```python
flatmate1.pays(bill, flatmate2)
# → bill.amount * (self.days / (self.days + other.days))
```

### `PdfReport` (`PdfReport.py`)
Wraps FPDF to generate a styled report with:
- The period title
- Each flatmate's name and amount due
- Total

Filename is derived from the period (spaces stripped).

## 💡 Possible Extensions

- Support **3+ flatmates** dynamically (loop until "done")
- Email the PDF directly to both flatmates
- Persist past bills locally (JSON or SQLite) and add a `history` command
- Add a **share-via-Filestack** option (already a dependency in `requirements.txt`)
- Wrap in a **simple GUI** (Tkinter / PySimpleGUI)

## 👤 Author

**Denis Vreshtazi** — [GitHub](https://github.com/denisvreshtazi)
