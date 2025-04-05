import csv
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_certificate(data):
    for intern in data:
        name = intern['Name']
        internship = intern['Internship']
        end_date = intern['End Date']

        file_name = f"certificate_{name.replace(' ', '_')}.pdf"
        c = canvas.Canvas(file_name, pagesize=A4)
        width, height = A4

        # Title
        c.setFont("Helvetica-Bold", 24)
        c.drawCentredString(width / 2, height - 100, "CODTECH")

        # Subtitle
        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(width / 2, height - 150, "INTERNSHIP COMPLETION CERTIFICATE")

        # Body Text
        c.setFont("Helvetica", 12)
        text = f"This is to certify that {name} has successfully completed their internship"
        c.drawCentredString(width / 2, height - 200, text)

        text2 = f"in the field of {internship} with CodTech. The internship ended on {end_date}."
        c.drawCentredString(width / 2, height - 220, text2)

        # Footer
        c.setFont("Helvetica-Oblique", 10)
        c.drawCentredString(width / 2, 100, "This certificate is system-generated and does not require a signature.")

        c.showPage()
        c.save()
        print(f"Generated: {file_name}")

def read_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

if __name__ == "__main__":
    data = read_csv("data.csv")
    generate_certificate(data)