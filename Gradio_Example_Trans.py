import gradio as gr

# 下面請輸入自己的API_KEY
API_KEY = "api key"
import google.generativeai as genai

model = genai.GenerativeModel('gemini-1.5-flash')
genai.configure(api_key=API_KEY)

def trans(prompt):
    system = "請將下面的中文翻譯成英文：\n"
    response = model.generate_content(system + prompt)
    return response.text


demo = gr.Interface(fn=trans, inputs=[gr.Textbox(label="中文")]
    , outputs=gr.Textbox(label="英文"),                                     
    title="中翻英系統",
    description="請輸入中文：")
    
demo.launch() 
