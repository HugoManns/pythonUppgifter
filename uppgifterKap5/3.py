# Skapa en funktion som tar in en string som argument och retunerar strängen men bara stora bokstäver

def uppercase_converter(name):
    uppercase_name = name.upper()
    return uppercase_name

name = uppercase_converter("Hugo")
print(name)