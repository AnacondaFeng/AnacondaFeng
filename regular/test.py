import re

pattern = re.compile(r"OH", re.I)

rest = pattern.match('oh,ye')

print(rest)

print(rest.string)