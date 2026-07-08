"""
==============================================
TradingVisionAI
Configuration File
==============================================
"""

import os
from dotenv import load_dotenv

# Load .env
load_dotenv()

# -----------------------------
# API
# -----------------------------

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MODEL_NAME = "gpt-4.1-mini"

# -----------------------------
# Folder Paths
# -----------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_FOLDER = os.path.join(BASE_DIR, "input")

OUTPUT_FOLDER = os.path.join(BASE_DIR, "output")

IMAGE_FOLDER = os.path.join(BASE_DIR, "images")

LOG_FOLDER = os.path.join(BASE_DIR, "logs")

PROMPT_FOLDER = os.path.join(BASE_DIR, "prompts")

# -----------------------------
# Output Excel
# -----------------------------

EXCEL_FILE = os.path.join(
    OUTPUT_FOLDER,
    "Trading_Report.xlsx"
)

# -----------------------------
# Retry
# -----------------------------

MAX_RETRIES = 3

WAIT_TIME = 5

# -----------------------------
# Supported Files
# -----------------------------

SUPPORTED_PPT = [
    ".ppt",
    ".pptx"
]

SUPPORTED_PDF = [
    ".pdf"
]