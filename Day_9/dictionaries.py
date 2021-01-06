programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving items from dictionary.
programming_dictionary["Bug"]

# Adding news items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Create an empty dictionary.
empty_dict = {}

# Wipe an existing dictionary.
programming_dictionary = {}

# Edit an item in a dictionary.
programming_dictionary["Bug"] = "A moth in your computer."
programming_dictionary["Function"] = "A piece of code that you can easily call over and over again."

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary)