def replace_commas_with_newline(input_file, output_file):
    try:
        # Open the input file in read mode
        with open(input_file, 'r') as infile:
            # Read the content of the file
            content = infile.read()

            # Replace commas with new lines
            modified_content = content.replace(',', '\n')

        # Open the output file in write mode
        with open(output_file, 'w') as outfile:
            # Write the modified content to the output file
            outfile.write(modified_content)

        print(f"Successfully replaced commas with new lines. Output saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file_path = 'input.txt'  # Replace with the path to your input file
output_file_path = 'output.txt'  # Replace with the desired output file path

replace_commas_with_newline(input_file_path, output_file_path)
