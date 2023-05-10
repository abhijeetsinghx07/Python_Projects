![Email_valid](https://github.com/abhijeetsinghx07/Python_Projects/assets/108348003/ce7070e3-4077-495a-878b-bf8685fc2803)



```python
import gradio as gr

def validate_email(email):
    
    k,j,d= 0,0,0
    
    if len(email) >= 6:
        if email[0].isalpha():
            if "@" in email and email.count("@") == 1:
                if email[-3] == "." or email[-4] == ".":
                    for i in email:
                        if i == i.isspace():
                            k = 1
                        elif i.isalpha():
                            if i == i.upper():
                                j = 1
                        elif i.isdigit():
                            continue
                        elif i == "_" or i == "." or i == "@":
                            continue
                        else:
                            d = 1
                    if k == 1 or j == 1 or d == 1:
                        return "Invalid Mail ID"
                    else:
                        return "Valid Mail ID"
                else:
                    return "Invalid Mail ID"
            else:
                return "Email address contain more that one time: '@' "
        else:
            return "First word is not alphabet, Try Again!!"
    else:
        return "Less then 6 word limit, Try Again!!"

input_text = gr.inputs.Textbox(label="Enter your email id")
output_text = gr.outputs.Textbox(label="Validation Result")

interface=gr.Interface(fn=validate_email, inputs=input_text, outputs=output_text, title="Email ID Validator",)
interface.launch()

     
```
