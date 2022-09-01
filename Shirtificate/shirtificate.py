from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 15)
        self.cell(80)
        self.cell(30, 10, "CS50 Shirtificate", border=0, align="C")
        self.ln(20)


name = input("Name: ")
pdf = PDF()
pdf.add_page()
pdf.image("Shirtificate/shirtificate.png", x=0, y=60)
pdf.set_font("helvetica", size=35)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 230, f"{name} took CS50", border=0, align='C')
pdf.output("Shirtificate/shirtificate.pdf")
