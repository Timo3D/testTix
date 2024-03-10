import os
from PIL import Image, ImageDraw, ImageFont

output_dir = r"C:\Users\bugat\Downloads\testTix\out"
original_image = Image.open(r"C:\Users\bugat\Downloads\testTix\in\Jubilance Tickets 2023.png")
font = ImageFont.truetype(r"C:\Users\bugat\Downloads\testTix\in\nourd_regular.ttf", size=60)
text_color = "#3a3e5b"
num_tix = 20 # number of tickets to generate

# use chatgpt to help u figure out how to do this

for number in range(1, num_tix + 1):
    image = original_image.copy()
    text = "Ticket no." + str(number)
    bbox = ImageDraw.Draw(image).textbbox((0, 0), text, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    textbox_width, textbox_height = 647, 70
    text_image = Image.new('RGBA', (textbox_width, textbox_height), (0, 0, 0, 0))
    text_draw = ImageDraw.Draw(text_image)
    x_position = (textbox_width - text_width) // 2
    y_position = (textbox_height - text_height) // 2
    text_draw.text((x_position, y_position), text, fill=text_color, font=font)
    rotated_text_image = text_image.rotate(90, expand=1)
    image.paste(rotated_text_image, (1860, 0), rotated_text_image)
    image = image.convert('RGB')
    output_path = os.path.join(output_dir, f"Jubilance_Ticket_{number}.jpg")
    image.save(output_path, 'JPEG')
    print("finished " + str(number) + " out of " + str(num_tix))
