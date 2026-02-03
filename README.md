COMPANY: CODTECH IT SOLUTIONS 
NAME: ALTAF KHAN
INTERN ID: CTIS0967 
DOMAIN: Python Programming
DURATION: 6 Weeks
MENTOR: Neela Santhosh Kumar

# Automated Report Generator

Universal CSV data analysis and report generation tool that reads data from any CSV file, performs statistical analysis, and generates professional PDF reports. Built with Python (ReportLab) and JavaScript for both CLI and web-based usage.

## Features

- Upload and analyze any CSV file
- Automatic statistical calculations (average, min, max, pass rate)
- Generate professional PDF reports
- Web interface for easy use
- Python script for automation

## Installation

1. Clone or download the project
2. Create virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Python Version
```bash
python report_generator.py
```

### Web Version
1. Open `index.html` in your browser
2. Upload CSV file
3. View analysis and download PDF

## CSV Format

Your CSV should have headers in the first row. The tool automatically detects score columns (Score, Total_Score, Marks, etc.).

Example:
```csv
Student_ID,Name,Department,Score
1,John Doe,Computer Science,85
2,Jane Smith,Electronics,92
```

## Project Structure
```
codtech-task2/
├── report_generator.py    # Python script
├── index.html             # Web interface
├── requirements.txt       # Dependencies
├── data/                  # Input CSV files
└── output/                # Generated reports
```

## Technologies Used

- Python 3.x
- ReportLab (PDF generation)
- HTML/CSS/JavaScript
- jsPDF (Web PDF generation)

## Author

[ALTAF KHAN]  
CODTECH Internship - Task 2

## License

This project is open source and available for educational purposes.
