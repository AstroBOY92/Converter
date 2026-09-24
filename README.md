# 🌡️ Temperature Converter

An interactive Streamlit app for converting temperatures between Fahrenheit and Celsius — single values, batches, or full CSV files.

Originally written as a simple command-line script years ago; rebuilt as a Streamlit web app to practise interactive UI patterns (sidebar controls, file upload, data validation, exports).

## Features
- Convert Fahrenheit ↔ Celsius, selectable from the sidebar
- Paste multiple values at once (comma, space, semicolon, or newline separated)
- Upload a CSV and auto-detect the numeric column to convert
- Adjustable decimal precision (0–6 places)
- Results table with summary statistics (mean, std, min/max, etc.)
- Download converted results as CSV
- Quick line chart comparing the two scales

## Tech stack
Python · Streamlit · NumPy · Pandas

## Run locally
\`\`\`bash
git clone https://github.com/AstroBOY92/Converter.git
cd Converter
pip install -r requirements.txt
streamlit run app.py
\`\`\`

## Project structure
- `temp_conv.py` — core conversion logic (the original piece of the exercise)
- `app.py` — Streamlit interface layer (UI, input handling, CSV I/O, charting)

---
A small, deliberately simple project used to practise structuring a Streamlit app end-to-end: input handling, state, file I/O, and basic data viz.
