from parser2 import LT2Parser

def read_lt2_file(filename):
    """Reads a .lt2 file and returns its content as a string."""
    with open(filename, "r") as file:
        return file.read()

def write_python_file(python_code, output_filename="output.py"):
    """Writes the generated Python code to a file."""
    with open(output_filename, "w") as file:
        file.write("\n".join(python_code))
def main():
    lt2_filename = "test1.lt2"  # Replace with the actual .lt2 file path
    program = read_lt2_file(lt2_filename)

    # Parse the program and generate Python code
    parser = LT2Parser(program)
    parser.parse_program()

    # Output the result in terminal
    print("\n=== Output in Terminal ===")
    for var, value in parser.variables.items():
        print(f"{var} = {value}")

    # Write the generated Python code to output.py
    write_python_file(parser.python_code)
    print("\nGenerated Python code is saved to 'output.py'")

if __name__ == "__main__":
    main()