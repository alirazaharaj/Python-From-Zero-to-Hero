# Regular Expression 
import re
Pattern=r"[A-Z]+ylon"
text="if a large force act on a body for short interval of time than Cylon njjoihiuhkjdsnvkd ujdhfo dv j Dylon."

doc=re.search(Pattern,text)
print(doc)
# To find all matched values
doc=re.finditer(Pattern,text)
for do in doc:
    # doc type is tuple 
    print(text[do.span()[0]:do.span()[1]])