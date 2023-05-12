from pyfiglet import figlet
figlet = Figlet()
fi = input("Input: ")
figlet.getFonts()
figlet.setFonts(font = f)
print(figlet.renderText(s))