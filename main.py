"""
Given a string as input. Input string got some additional '$' characters by mistake. Print the original string by removing these extra '$' characters.
Input-> "$dollar$"
Output-> Original=dollar
"""

st = "$dollar$"
ln = len(st)
strn = ""
for i in range(0,ln):
  ch = st[i]
  if (ch!="$"):
    strn = strn + ch
print(f"Original:{strn}")

