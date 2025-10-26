# diffuser.py
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from io import BytesIO
from PIL import Image
import numpy as np
import cv2

load_dotenv()

client = InferenceClient(
    provider="hf-inference",
    api_key=os.environ["HUGGINGFACE_TOKEN"],
)
print("Client initialized.")

def generate_blueprint(prompt):
    """
    Generate an engineering-style blueprint from spoken text using Hugging Face Inference Client.
    """
    print(f"Generating blueprint for prompt: '{prompt}'...")

    # Refine prompt for blueprint-style generation
    blueprint_prompt = (
        f"technical engineering blueprint, schematic line drawing of {prompt}, "
        "monochrome background, detailed sketch, CAD-style design, architectural plan view"
    )

    result = client.text_to_image(blueprint_prompt, model="stabilityai/stable-diffusion-xl-base-1.0")

    # Check if result is already a PIL Image or bytes
    if isinstance(result, Image.Image):
        img = result
    else:
        img = Image.open(BytesIO(result))

    output_path = "generated_blueprint.png"
    img.save(output_path)
    print(f"Blueprint saved as {output_path}")

    # Convert PIL to OpenCV format for viewing
    '''img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    cv2.imshow("Generated Blueprint", img_cv)
    print("Press any key in the image window to exit.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''

if __name__ == "__main__":
    prompt = input("Enter a description (e.g., bridge design): ")
    generate_blueprint(prompt)
