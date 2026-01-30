import text_encryption_function

#Uppgift 1
"""
def copy_text_file(in_file, out_file):
    with open(in_file, "r") as infile:
        content = infile.read()

    with open(out_file, "w") as outfile:
        outfile.write(content)

copy_text_file("namn.csv", "my_copy.csv")

with open('out_file.csv', 'r') as f:
    print(f.read())

"""

#Uppgift 2

def encrypt_file(in_file, out_file):
    with open(in_file, "r") as infile:
        content = infile.read()

    encrypted = text_encryption_function.offset_encrypt(content, 1)

    with open(out_file, "w") as outfile:
        outfile.write(encrypted)

encrypt_file("namn.csv", "secret_names.csv")
