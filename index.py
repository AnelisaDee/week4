import os

def sample_file():
    with open("input.txt", "w") as file:
            file.write("Hello, this my first sentence. \n")
            file.write("This is my second sentence which is longer than the first one. \n")
            file.write("This is the third and the last sentence. Goodbye!")

def modify_file(input_file, output_file):
        if not os.path.exists(input_file):
              print(f"The {input_file} does not exist!")
              return
        try:
            with open(input_file, "r") as file:  
                data = file.read()
                uppercase = data.upper()

            with open("output.txt", "w") as file:
                   file.write(uppercase)
                
            print(f"The file has been created: {output_file}")

        except FileNotFoundError:
               print(f"Cannot read or write the {input_file} file!")
input_file = input("Enter the file name: ")

output_file = "output.txt"
if not os.path.exists(input_file):
    print(f"{input_file} not found, creating a sample file...")
    sample_file()
modify_file(input_file, output_file)

