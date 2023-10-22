# PDF to Speech Converter

This script converts the text content of a PDF file into speech and saves it as an MP3 file using the Google Text-to-Speech (gTTS) library.

## Prerequisites

- Python 3.x
- Install the required libraries using the following command:

```bash
pip install PyPDF2 gTTS
```

## Usage
1. Clone or download this repository to your local machine.
2. Place the PDF file you want to convert in the same directory as the script.
3. Open a terminal or command prompt and navigate to the directory containing the script.
4. Run the script by executing the following command:
```bash
python PDF-to-Speech-Converter.py
```
5. The script will extract the text content from the PDF, convert it to speech, and save it as an MP3 file in the same directory.

## Customization
You can customize the script by modifying the following:

pdf_path: Update this variable to point to the location of the PDF file you want to convert.
output_file: Change the name of the output MP3 file.

## Troubleshooting
If the script encounters any errors while extracting text or converting to speech, it will print an error message. You can refer to these messages to identify and troubleshoot issues.

## Disclaimer
This script relies on external libraries and services for PDF extraction and text-to-speech conversion. Make sure to review and comply with the terms of use for the libraries and services being utilized.

## License
This project is licensed under the GNU License.
