import os,fpdf

pdf=fpdf.FPDF()
os.chdir("C:/Users/asus/Desktop/")
pdf.add_page()
pdf.set_font("Arial",size=15)
pdf.cell(100,10,txt="This PDF File was Created by Python.",ln=2,align='C')
pdf.output("Created.pdf")