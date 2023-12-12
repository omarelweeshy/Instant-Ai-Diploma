import re
with open('names.txt', 'r') as file:
    content = file.read()


names_pattern = re.compile(r'^\b[A-Za-z]+(?: [A-Za-z]+)?(?: [A-Za-z]+)?\b',re.MULTILINE)
names = names_pattern.finditer(content)
for match in names:
    print("Name:",match.group())

email_patterns = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
matches = email_patterns.finditer(content)
for match in matches:
    print("Email:",match.group())

numbers_pattern = re.compile(r"\d{11}",re.MULTILINE)
numbers = numbers_pattern.finditer(content)
for match in numbers:
    print("Number:",match.group())


