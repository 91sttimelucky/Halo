import os
import re

# Read the header and footer files
with open('header.html', 'r') as f:
    header_content = f.read()

with open('footer.html', 'r') as f:
    footer_content = f.read()

# Define the placeholder patterns for header and footer
header_pattern = re.compile(r'<!--.*#HEADER.*-->', re.DOTALL)
footer_pattern = re.compile(r'<!--.*#FOOTER.*-->', re.DOTALL)


# Go through each file in the current directory
for file_name in os.listdir():
    if file_name.endswith('.html') and file_name not in ['header.html', 'footer.html']:
        print(f"Processing file: {file_name}")

        with open(file_name, 'r') as f:
            content = f.read()

        # Replace header and footer placeholders
        new_content, header_replacements = header_pattern.subn(header_content, content)
        new_content, footer_replacements = footer_pattern.subn(footer_content, new_content)

        if header_replacements == 0:
            print(f"HEADER placeholder not found.")
        if footer_replacements == 0:
            print(f"FOOTER placeholder not found.")

        if header_replacements > 0 or footer_replacements > 0:
            # Write the file back
            with open(file_name, 'w') as f:
                f.write(new_content)
            print(f"Replacements made.")
        else:
            print(f"No replacements made.")

print("\nHeader and Footer inserted successfully!")
