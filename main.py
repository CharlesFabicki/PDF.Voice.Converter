from gtts import gTTS
from PyPDF2 import PdfReader


# Convert PDF to text
def pdf_to_text(pdf_path):
    text = ""
    try:
        pdf = PdfReader(pdf_path)
        for page in pdf.pages:
            text += page.extract_text()
    except Exception as e:
        print("Error extracting text from PDF:", e)
    return text


# Convert text to speech using gTTS
def text_to_speech(text):
    tts = gTTS(text)
    return tts


# Main function
def main():
    pdf_path = r'C:\Users\Charles\Desktop\Karol\Programming\Python\Portfolio\PDF Voice Converter\Guide.pdf'
    text = pdf_to_text(pdf_path)

    if text:
        tts = text_to_speech(text)
        output_file = "output.mp3"
        tts.save(output_file)
        print("Speech generated and saved as", output_file)
    else:
        print("No text extracted from the PDF.")


if __name__ == "__main__":
    main()
