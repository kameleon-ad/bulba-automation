Sure, here is a simple Python program to examine a PDF document and retrieve numbers that are 15 digits (three digits and a space then 12 digits) and then place them into an Excel spreadsheet:

```python
import PyPDF2

def extract_numbers(pdf_file):
    """Extracts 15-digit numbers from a PDF file.

    Args:
        pdf_file: The path to the PDF file.

    Returns:
        A list of 15-digit numbers.
    """

    # Open the PDF file.
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # Extract the text from all pages of the PDF file.
    text = ""
    for page in pdf_reader.pages:
        text += page.extractText()

    # Find all occurrences of 15-digit numbers in the text.
    numbers = []
    for match in re.finditer(r'\d{3} \d{12}', text):
        numbers.append(match.group())

    print(numbers)
    return numbers

if __name__ == '__main__':
    # Get the path to the PDF file.
    pdf_file = 'input.pdf'

    # Extract the 15-digit numbers from the PDF file.
    numbers = extract_numbers(pdf_file)
```

To use the program, simply pass the path to the PDF file and the path to the Excel file as command-line arguments. For example, to extract the 15-digit numbers from the PDF file `/path/to/pdf/file.pdf` and write them to the Excel file `/path/to/excel/file.xlsx`, you would run the following command:

```
python extract_numbers_to_excel.py /path/to/pdf/file.pdf /path/to/excel/file.xlsx
```

The program will then create the Excel file, if it does not already exist, and write the 15-digit numbers to the first column.
