![IL5NvIQfbM](https://user-images.githubusercontent.com/108348003/236901608-19c461d1-0d6f-40d5-93fd-ec67e408872c.png)



```python


import gradio as gr #import gradio 
def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Cannot divide by zero"
        else:
            return a / b
            
interface = gr.Interface(
    fn=calculator,
    inputs=["number", "number", gr.inputs.Dropdown(["+", "-", "*", "/"])],
    outputs="number",
    title="Calculator",
    description="Perform basic arithmetic operations",
    examples=[
        [5, 3, "+"],
        [10, 2, "*"],
        [7, 0, "/"],
    ]
)

interface.launch()

```
