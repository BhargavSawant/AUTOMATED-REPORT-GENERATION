# AUTOMATED-REPORT-GENERATION
 
COMPANY: CODETECH IT SOLUTION

NAME: BHARGAV SAAWANT B

INTERN ID: CT04WU190

DOMAIN: PYTHON PROGRSMMING

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH
---

## Project Overview  
This **Internship Certificate Generator** is a Python-based script that automates the creation of internship completion certificates using data from a CSV file. It utilizes the **ReportLab** library to generate PDF files and reads intern details like name, domain, and end date from a structured dataset. This project is especially useful for automating repetitive tasks in HR or training departments.

---

## Features

1. **CSV-Based Input**  
   Reads intern details from a structured CSV file (Name, Internship, End Date).

2. **Automated PDF Certificate Creation**  
   Dynamically creates personalized internship certificates in PDF format.

3. **Professional Layout**  
   Uses ReportLab to design and layout certificates with clean formatting.

4. **System-Generated Footer**  
   Adds an official note indicating that the certificate doesn’t require a physical signature.

5. **Batch Processing**  
   Generates certificates for all entries in the CSV file automatically.

---

## How It Works

1. The `read_csv()` function loads intern data from a CSV file using Python’s built-in `csv` module.

2. The `generate_certificate()` function:
   - Iterates through each intern’s record.
   - Uses the **ReportLab** canvas to design and populate a certificate layout.
   - Saves each certificate as a PDF file named after the intern.

3. When executed, the script reads the data and creates individual certificates automatically.

---

##  Breakdown of the Code

### Modules Used:
- `csv`: Reads intern data from CSV files.
- `reportlab`: Generates PDF certificates.
- `datetime`: (Imported but not used—can be utilized for date formatting if needed).

### Key Functions:
- **`read_csv(file_path)`**  
  Loads and parses CSV data into a list of dictionaries.

- **`generate_certificate(data)`**  
  Uses ReportLab to generate and save certificates in PDF format.

- **`__main__`**  
  Reads the CSV and runs the certificate generation function.

---

## Libraries Used

- **ReportLab**  
  For generating high-quality PDFs in Python.

- **CSV**  
  For reading structured intern data.

- **Datetime** *(Optional)*  
  Can be used to handle date formatting and validation.

---

## Use Cases

1. **HR Automation**  
   Automatically generate internship or training certificates in bulk.

2. **Educational Institutes**  
   Generate course completion certificates for students.

3. **Corporate Training**  
   Ideal for professional development program certification.

4. **Event Management**  
   Customize and issue participation or appreciation certificates.

---
