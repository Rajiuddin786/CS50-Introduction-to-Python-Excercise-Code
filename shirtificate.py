from fpdf import FPDF

name=input("What's your name: ")
logo=name+" took CS50"
pdf=FPDF()
pdf.add_page()
pdf.image("shirtificate.png",x=0,y=50)
pdf.set_font("Arial",style="B",size=50)
pdf.set_text_color(0,0,0)
pdf.cell(0,30,"CS50 Shirtificate",ln=True,align='C')
pdf.set_font("Arial", style="B", size=30)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 200, logo, ln=True, align='C')
pdf.output("shirtificate.pdf")