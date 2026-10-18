# AI Trading Chart Transcriber

<p align="center">
  <img src="./assets/logo/Logo.png" width="260" alt="Logo">
</p>

![Project Banner](./assets/banner/banner.png)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Gemini](https://img.shields.io/badge/Google-Gemini%20Vision-orange)
![Status](https://img.shields.io/badge/Status-Version%201-success)

A Python tool that reads trading chart screenshots and PowerPoint slides with the Google Gemini Vision API and writes the extracted indicators into an Excel report.

Instead of OCR, each chart image is sent to Gemini (`gemini-2.5-flash`) with a prompt that asks for specific fields in JSON. The answers for all charts are collected into one formatted spreadsheet.

## How it works

1. **Export slides**: every `.ppt` / `.pptx` file in `input/` is exported to PNG images (one per slide) in `images/<presentation name>/`, using Microsoft PowerPoint through `pywin32`.
2. **Collect images**: all `.png`, `.jpg` and `.jpeg` files under `images/` are picked up, including chart screenshots you put there yourself.
3. **Analyze**: each image is sent to Gemini with the prompt in `prompts/analysis_prompt.txt`. The response is parsed as JSON.
4. **Write report**: results are saved to `output/Trading_Report.xlsx`, one row per image.

![System Architecture](./assets/diagrams/Diagram_1.png)

## Extracted fields

Each row in the report contains:

Slide number, ticker, timeframe, price, trend, chart pattern, RSI (14D), relation to 20 SMA, volume analysis, immediate support, immediate resistance, RSI, Bollinger Band status, divergence, MACD, moving averages, candlestick pattern, prediction, confidence and remarks.

Any field the model cannot read with confidence is returned as `Unknown`.

## Requirements

- Windows with **Microsoft PowerPoint** installed (needed only for the slide export step)
- Python 3.11
- A Google Gemini API key ([Google AI Studio](https://aistudio.google.com/))

## Setup

```bash
git clone https://github.com/Adityaraj8118/AI-Trading-Chart-Transcriber.git
cd AI-Trading-Chart-Transcriber
pip install -r requirements.txt
```

Create a `.env` file in the project folder:

```
GEMINI_API_KEY=your_api_key_here
```

`.env` is git-ignored, so the key is never committed.

## Usage

1. Put PowerPoint files in `input/`, and/or chart images in `images/`.
2. Run:

```bash
python main.py
```

3. Open `output/Trading_Report.xlsx`.

## Project structure

```text
AI-Trading-Chart-Transcriber/
├── input/                 PowerPoint files to process
├── images/                Exported slides and chart images
├── output/                Generated Excel report (created on first run)
├── prompts/
│   └── analysis_prompt.txt   Prompt sent to Gemini with each image
├── main.py                Runs the full pipeline
├── extract_ppt.py         Exports slides to PNG via PowerPoint
├── extract_pdf.py         PDF support (not implemented yet)
├── ai_analyzer.py         Sends images to Gemini and parses the JSON response
├── excel_writer.py        Builds the formatted Excel report
├── config.py              Folder paths and settings
├── logger.py, utils.py    Placeholders (empty for now)
└── requirements.txt
```

## Limitations

- PDF input is not supported yet; `extract_pdf.py` is a placeholder.
- The PowerPoint export only works on Windows with PowerPoint installed.
- Results depend on chart quality and on the model's reading of it, so values should be checked before being used for trading decisions.

## Roadmap

- PDF support
- Better prompt and chart detection accuracy
- Improved Excel formatting
- Confidence score for each signal
- Faster processing

## Author

**Aditya Raj Gupta** · [GitHub](https://github.com/Adityaraj8118)
