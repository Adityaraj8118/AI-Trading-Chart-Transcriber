import os
import win32com.client
from config import INPUT_FOLDER, IMAGE_FOLDER


def export_ppt_to_images():

    ppt_files = [
        f for f in os.listdir(INPUT_FOLDER)
        if f.lower().endswith((".ppt", ".pptx"))
    ]

    if len(ppt_files) == 0:
        print("❌ No PowerPoint file found in input folder.")
        return

    powerpoint = win32com.client.Dispatch("PowerPoint.Application")
    powerpoint.Visible = 1

    for ppt in ppt_files:

        ppt_path = os.path.join(INPUT_FOLDER, ppt)

        base_name = os.path.splitext(ppt)[0]

        output_folder = os.path.join(IMAGE_FOLDER, base_name)

        os.makedirs(output_folder, exist_ok=True)

        print(f"\nProcessing : {ppt}")

        presentation = powerpoint.Presentations.Open(
            ppt_path,
            WithWindow=False
        )

        presentation.SaveAs(output_folder, 18)

        presentation.Close()

        print(f"Slides exported to : {output_folder}")

    powerpoint.Quit()


if __name__ == "__main__":
    export_ppt_to_images()