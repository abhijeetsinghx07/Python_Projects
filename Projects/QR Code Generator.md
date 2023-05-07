
![chrome_0jqeztyepZ](https://user-images.githubusercontent.com/108348003/236662768-c039ff74-47cb-47a3-af8a-77ee2d435d1a.png)




```python
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

input_image = gr.inputs.Image(shape=(len("example")*15, len("example")*15))

iface.fn = lambda img: display_qr_code(img.getdata())

iface.launch()
```
