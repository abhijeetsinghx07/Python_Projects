
___

### QR Code Generator using Python and Gradio
___

![chrome_75BGIHWHza](https://user-images.githubusercontent.com/108348003/236662600-f35175c9-0c2a-4f03-b849-c31ae3e83d2c.png)


```
import gradio as gr
import qrcode
from PIL import Image

def generate_qr_code(name):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(name)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img = img.convert('RGB')
    img_bytes = img.tobytes()
    return img_bytes

def display_qr_code(name):
    img_bytes = generate_qr_code(name)
    img = Image.frombytes('RGB', (len(name)*15, len(name)*15), img_bytes)
    return img

iface = gr.Interface(
    fn=display_qr_code,
    inputs="text",
    outputs="image",
    title="QR Code Generator",
    description="Generate a QR code for a given name.",
)

# Add an image field to the input interface to display the generated QR code
input_image = gr.inputs.Image(shape=(len("example")*15, len("example")*15))

# Modify the `fn` argument of the interface to accept an image as input and pass it to the `display_qr_code` function
iface.fn = lambda img: display_qr_code(img.getdata())

# Launch the interface with the updated function argument and input fields
iface.launch()
```
