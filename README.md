# AI Trading Chart Transcriber

AI-powered Trading Chart Transcriber built with Python and Google Gemini Vision API.

## Features

- Extracts trading information from:
  - PowerPoint (.ppt/.pptx)
  - PDF (.pdf)
  - Images (.png/.jpg/.jpeg)
- Uses AI Vision instead of OCR
- Generates Excel reports automatically
- Supports batch processing
- Clean and modular Python architecture

## Technologies Used

- Python
- Google Gemini Vision API
- OpenCV
- OpenPyXL
- PyMuPDF
- python-pptx
- Pillow

## Project Structure

```
AI-Trading-Chart-Transcriber
│
├── images
├── input
├── prompts
├── ai_analyzer.py
├── config.py
├── excel_writer.py
├── extract_pdf.py
├── extract_ppt.py
├── logger.py
├── main.py
├── utils.py
├── requirements.txt
```

## Installation

```bash
git clone https://github.com/Adityaraj8118/AI-Trading-Chart-Transcriber.git

cd AI-Trading-Chart-Transcriber

pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Author

Aditya Raj Gupta