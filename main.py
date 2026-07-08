import os

from extract_ppt import export_ppt_to_images
from ai_analyzer import analyze_image
from excel_writer import save_excel
from config import IMAGE_FOLDER, OUTPUT_FOLDER


def get_all_images():

    images = []

    for root, dirs, files in os.walk(IMAGE_FOLDER):

        for file in files:

            if file.lower().endswith((".png", ".jpg", ".jpeg")):

                images.append(
                    os.path.join(root, file)
                )

    images.sort()

    return images


def main():

    print("=" * 60)
    print("Trading Vision AI")
    print("=" * 60)

    # STEP 1
    print("\nStep 1 : Exporting PPT Slides...")

    export_ppt_to_images()

    # STEP 2
    print("\nStep 2 : Searching Images...")

    images = get_all_images()

    print(f"Found {len(images)} images.\n")

    if len(images) == 0:

        print("No Images Found.")

        return

    all_results = []

    # STEP 3
    for i, image in enumerate(images, start=1):

        print(f"[{i}/{len(images)}] {os.path.basename(image)}")

        result = analyze_image(image)

        result["Slide_No"] = os.path.splitext(
            os.path.basename(image)
        )[0]

        all_results.append(result)

    # STEP 4
    output_excel = os.path.join(
        OUTPUT_FOLDER,
        "Trading_Report.xlsx"
    )

    print("\nSaving Excel...")

    save_excel(
        all_results,
        output_excel
    )

    print("\nFinished Successfully!")

    print(output_excel)


if __name__ == "__main__":

    main()