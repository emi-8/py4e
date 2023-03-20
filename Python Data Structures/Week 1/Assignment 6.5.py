text = "X-DSPAM-Confidence:    0.8475"

po = text.find(':')

print(float(text[po+5:]))