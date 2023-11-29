To write a Python program that examines a PDF document, retrieves numbers matching a specific pattern (three digits, a space, then twelve digits), and then places them into an Excel spreadsheet, you'll need to use a few libraries: `PyPDF2` (or a similar library) to read PDF files, `re` for regular expression matching, and `openpyxl` or `pandas` to write to an Excel file.

Here's a step-by-step guide to creating such a program:

### 1. Install Necessary Libraries

You might need to install these libraries if you haven't already. You can do this using pip:

```bash
pip install PyPDF2 pandas
```

### 2. Python Program

```python
import re\nimport PyPDF2\nimport pandas as pd\n\n# Define the pattern to search for\npattern = r'\b\d{3} \d{12}\b'\n\n# Function to extract the numbers from a PDF\ndef extract_numbers_from_pdf(file_path):\n    numbers = []\n    with open(file_path, 'rb') as file:\n        reader = PyPDF2.PdfReader(file)\n        for page_num in range(len(reader.pages)):\n            page = reader.pages[page_num]\n            text = page.extract_text()\n            if text:\n                found_numbers = re.findall(pattern, text)\n                numbers.extend(found_numbers)\n    return numbers\n\n# Replace with your PDF file path\npdf_file_path = 'input.pdf'\n\n# Extract numbers from the PDF\nextracted_numbers = extract_numbers_from_pdf(pdf_file_path)\n\n# Save the numbers to an Excel file\ndf = pd.DataFrame(extracted_numbers, columns=['Numbers'])\nexcel_file_path = 'extracted_numbers.xlsx'\ndf.to_excel(excel_file_path, index=False)\n\nprint(f"Numbers extracted and saved to {excel_file_path}")
```

### Explanation

1. **Import Libraries**: `re` for regular expressions, `PyPDF2` for reading PDFs, and `pandas` for creating Excel files.
2. **Define the Regular Expression Pattern**: This matches three digits followed by a space and then twelve digits.
3. **Function to Extract Numbers**: Reads the PDF, extracts text from each page, and finds all occurrences of the pattern.
4. **Save to Excel**: The extracted numbers are stored in a DataFrame and then saved as an Excel file.

### Notes

- Ensure that the path to the PDF (`pdf_file_path`) is correctly specified.
- The program saves the Excel file in the same directory as the script unless you specify a different path for `excel_file_path`.
- This code assumes that the PDF text can be extracted easily. Some PDFs (like scanned images) may not yield text without OCR (Optical Character Recognition) processing.

Feel free to modify the code to suit your specific requirements.
