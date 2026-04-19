import tkinter as tk

def ask_question(question,correct_answer, target_name):
    is_correct = False

    root = tk.Tk()
    root.title("Stop Procrastinating!!!")
    root.attributes('-topmost', True)
    root.attributes("-fullscreen", True)
    root.protocol("WM_DELETE_WINDOW", lambda: None)
    title_label = tk.Label(root,text=target_name, font=("Arial", 30, "bold"))
    title_label.pack(side="top")
    question_label = tk.Label(root,text=question,font=("Arial", 24))
    question_label.pack(pady=10)
    input = tk.Entry(root)
    input.pack(pady=10)
    
    def check_answer():
        nonlocal is_correct
        answer = input.get().strip()
        if (answer == correct_answer):
            is_correct = True
            print("Correct!")
            root.destroy()
    
    button = tk.Button(root,text="Check Answer", command=check_answer)
    button.pack(pady=10)

    root.mainloop()
    return is_correct