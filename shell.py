from email.mime import application
import basic
zefvr = "1.02"

print("ZEFROIN VERSION " + zefvr)
while True:
	text = input('Zefroin > ')
	if text.strip() == "": continue
	result, error = basic.run('<stdin>', text)
	if text.strip() == "exit":
		quit()
	if text.strip() == "help":
		print(" statements \n statement \n expr \n comp-expr \n arith-expr \n term \n factor \n power \n call \n atomlist-expr \n if-expr \n if-expr-b \n if-expr-c \n for-expr \n while-expr \n func-def")
		error = False
	if text.strip() == "WMT":
		print("Creator is Azureian")
		error = False
	if text.strip() == "version":
		print(zefvr)
		error = False



	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))
