import gradio as gr

def iris(花萼長度, 花萼寬度):
    score = -3.4*float(花萼長度) + 3.15*float(花萼寬度) + 8.44
    if score >= 0:
        return "是山鳶尾！"
    else:
        return "不是是山鳶尾！"

demo = gr.Interface(fn=iris, inputs=[gr.Textbox(label="花萼長度", value="5.1"),
                                     gr.Textbox(label="花萼寬度", value='3.5')]
    , outputs=gr.Textbox(label="結果"),                                     
    title="鳶尾花分類",
    description="請輸入鳶尾花的屬性：",)
    
demo.launch() 