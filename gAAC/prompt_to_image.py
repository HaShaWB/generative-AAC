# gAAC/prompt_to_image.py

import os

from dotenv import load_dotenv
from google import genai
from google.genai import types
from io import BytesIO


IMAGE_MODEL = "imagen-3.0-generate-002"


try:
    load_dotenv(override=True)
except FileNotFoundError:
    print("Environment file not found. Please ensure the .env file exists in the 'env' directory.")


_client = genai.Client(api_key=os.environ["GENAI_API_KEY"])


def prompt_to_image(prompt: str, num: int=2):
    response = _client.models.generate_images(
        model=IMAGE_MODEL,
        prompt=prompt,
        config=types.GenerateImagesConfig(
            number_of_images=num,
        )
    )

    return [BytesIO(generated_image.image.image_bytes) for generated_image in response.generated_images]


if __name__ == "__main__":
    from PIL import Image
    prompt = "Simple vector-style symbol illustration of a person eating an apple. One person with a round face in PeachPuff(#FFDAB9) color with thick black outline, black dots for eyes and curved line for mouth, simple curved black hair. Person wearing Blue(#0000FF) short-sleeve shirt and Black(#000000) shorts, both with thick black outlines and rounded corners made of basic geometric shapes. Person holding a Red(#FF0000) apple with thick black outline near their mouth in an eating gesture. The apple is a simple circle with a small green stem. All objects including the person's face, clothing, body parts, and apple have bold thick black outlines (32px). White background, centered composition, flat design with no shadows or gradients, minimalist AAC communication symbol style using only basic geometric shapes with rounded edges."
    images = prompt_to_image(prompt, num=2)

    for image in images:
        Image.open(image).show()
