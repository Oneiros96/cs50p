from fpdf import FPDF

def main():
    create_pdf(input("Name: "))


def create_pdf(name):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_auto_page_break(False)

    pdf.ln(40)
    pdf.set_font('helvetica', 'B', 60)
    pdf.cell(40, 10, "CS50 Shirtificate", align="C", center=True)

    pdf.ln(40)
    pdf.image("shirtificate.png", keep_aspect_ratio=True, h=pdf.eph/1.5)

    pdf.set_text_color(255, 255, 255)
    pdf.set_font('helvetica',"", 30)
    pdf.cell(None, -260, f"{name} took CS50", center=True)

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()