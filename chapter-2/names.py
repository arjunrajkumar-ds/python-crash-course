from email import message


name = 'arjun rajkumar'

# .title() function capitalises the first letter of each space-seperated string
print(name.title())

# f-strings:
first_name = 'arjun'
last_name = 'rajkumar'

full_name = f"{first_name} {last_name}"
print(full_name)

# Exercise 2-3: Personal Message
"Use a variable to represent a person’s name, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?"
name = 'Cullen'
message = f'Hi {name}, would you like to rip a cone?'
print(message)

# 2-4: Name Cases
"Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case."
name = 'arjun rajkumar'
print(name.lower())
print(name.upper())
print(name.title())

# 2-5/6: Famous Quote
"Find a quote from a famous person you admire. Print the quote and the name of its author."
quote = "'I might have been early, but I wasnt wrong'"
author = 'Michael Burry'
message = f"{author} once said, {quote}"
print(message)