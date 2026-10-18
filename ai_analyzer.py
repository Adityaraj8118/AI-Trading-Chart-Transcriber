import os
import json
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

# -----------------------------------------
# Gemini Client
# -----------------------------------------

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise Exception("❌ GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=API_KEY)


# -----------------------------------------
# Load Prompt
# -----------------------------------------

PROMPT_FILE = os.path.join(
    os.path.dirname(__file__),
    "prompts",
    "analysis_prompt.txt"
)

with open(PROMPT_FILE, "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()


# -----------------------------------------
# Analyze One Image
# -----------------------------------------

def analyze_image(image_path):

    print(f"Analyzing : {os.path.basename(image_path)}")

    with open(image_path, "rb") as img:
        image_bytes = img.read()

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            types.Part.from_bytes(
                data=image_bytes,
                mime_type="image/png"
            ),
            SYSTEM_PROMPT
        ]
    )

    text = response.text.strip()

    # Remove markdown if Gemini wraps JSON
    if text.startswith("```json"):
        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

    try:
        data = json.loads(text)

    except Exception:

        data = {
            "Price": "",
            "Trend": "",
            "Pattern": "",
            "RSI_14D": "",
            "Relation_to_20_SMA": "",
            "Volume_Analysis": "",
            "Immediate_Support": "",
            "Immediate_Resistance": "",
            "RSI": "",
            "BB_Status": "",
            "Divergence": "",
            "Confidence": "",
            "Raw_Output": text
        }

    return data


# -----------------------------------------
# Test
# -----------------------------------------

if __name__ == "__main__":

    image = input("Enter image path : ")

    result = analyze_image(image)

    print(json.dumps(result, indent=4))