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

def generate_image(prompt):
    """
    Generate an image using Hugging Face Inference Client
    and display it in an OpenCV window.
    """
    print(f"Generating image for prompt: '{prompt}'...")

    
    result = client.text_to_image(prompt, model="stabilityai/stable-diffusion-xl-base-1.0")

    # Check if result is already a PIL Image or bytes
    if isinstance(result, Image.Image):
        img = result
    else:
        img = Image.open(BytesIO(result))

    
    output_path = "generated_image.png"
    img.save(output_path)
    print(f"Image saved as {output_path}")

    # Convert PIL to OpenCV format (RGB -> BGR)
    img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    # Display image in a window
    cv2.imshow("Generated Image", img_cv)
    print("Press any key in the image window to exit.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    prompt = input("Enter a text prompt: ")
    generate_image(prompt)