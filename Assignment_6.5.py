#printing the float value from the text
text = "X-DSPAM-Confidence:    0.8475"
Num = text.find('0')
z = Num + 6
finder = float(text[Num : z])
print(finder)
