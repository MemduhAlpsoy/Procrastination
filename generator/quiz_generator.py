import random
import math

EXP_MAP = {2: "²", 3: "³", 4: "⁴", 5: "⁵", 6: "⁶", 7: "⁷", 8: "⁸", 9: "⁹"}

def derivative():
    x = random.randint(0,10)
    n = random.randint(2,4)

    question_text = ""
    question_list = []
    correct_answer = 0

    for derece in range(n,-1,-1):
        C = random.randint(0,10)
        if (C == 0):
            continue
        if (derece == 1):
            question_list.append(f"{C}x")
        elif (derece == 0):
            question_list.append(f"{C}")
        else:
            question_list.append(f"{C}x{EXP_MAP[derece]}")
        if (derece > 0):
            correct_answer += derece * C * (x ** (derece - 1))
    
    question_text = " + ".join(question_list)
    correct_answer_text = str(correct_answer)

    question = f"f(x) = {question_text} fonksiyonunun x={x} noktasındaki türevi nedir?"

    return question,correct_answer_text
