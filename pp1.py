from flask import Flask, request, render_template_string, redirect, url_for
import csv
import random

app = Flask(__name__)

questions = []

# Load questions from CSV file
with open('diagnosis.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    all_questions = [row[0] for row in reader]  # Extract all questions
    selected_questions = random.sample(all_questions, 10)  # Pick random 10 questions
    questions = [question.strip('[]') for question in selected_questions]  # Remove square brackets



chat_history = []
current_question_index = 0
error_message = ""  # متغير جديد لتخزين رسالة الخطأ 

def get_diagnosis(yes_count):
    # تحديد التوصية بناءً على عدد الإجابات بـ "نعم"
    if yes_count == 10:
        return "نعم: 10 لا: 0 - الطفل سليم."
    elif yes_count == 9:
        return "نعم: 9 لا: 1 - تصرفات طبيعية."
    elif yes_count == 8:
        return "نعم: 8 لا: 2 - تصرفات طبيعية لا داعي للقلق."
    elif yes_count == 7:
        return "نعم: 7 لا: 3 - حالة توحد خفيفة وينصح بدمج الطفل مع أطفال آخرين."
    elif yes_count == 6:
        return "نعم: 6 لا: 4 - حالة توحد خفيفة ويفضل مراقبة الطفل."
    elif yes_count == 5:
        return "نعم: 5 لا: 5 - حالة توحد متوسطة تستدعي مراقبة الطفل."
    elif yes_count in [3, 4]:
        return "نعم: {} لا: {} - حالة توحد متوسطة وعند تكرار التصرفات ينصح بزيارة المختص.".format(yes_count, 10 - yes_count)
    elif yes_count in [1, 2]:
        return "نعم: {} لا: {} - حالة توحد متقدمة وينصح بزيارة المختص.".format(yes_count, 10 - yes_count)
    else:
        return "نعم: 0 لا: 10 - حالة توحد متقدمة وتحتاج إلى استشارة طبية عاجلة."

@app.route('/', methods=['GET', 'POST'])
def quiz():
    global current_question_index, chat_history
    if request.method == 'POST':
        answer = request.form.get('answer', '').lower()
        if answer in ["نعم", "لا"]:
            chat_history.append({"type": "answer", "text": answer})
            current_question_index += 1
        else:
            return render_template_string(template, chat_history=chat_history, show_input=True, error_message="الرجاء الإجابة بـ 'نعم' أو 'لا' فقط.", current_question_index=current_question_index)

    if current_question_index < len(questions):
        chat_history.append({"type": "question", "text": questions[current_question_index]})
        return render_template_string(template, chat_history=chat_history, show_input=True, error_message="", current_question_index=current_question_index)
    
    yes_count = sum(1 for chat in chat_history if chat["text"] == "نعم")
    diagnosis = get_diagnosis(yes_count)
    return render_template_string(template, chat_history=chat_history, show_input=False, yes_count=yes_count, no_count=(current_question_index - yes_count), diagnosis=diagnosis)


template = r'''
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <title>MindBot</title>
    <link rel="icon" href="{{ url_for('static', filename='images/HOME_icon.png') }}" type="image/x-icon">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
        body { background-color: #f5f5f5; }
        .chat-container { 
            max-width: 600px; 
            margin: 20px auto;
            margin-top: 50px; 
            border: 1px solid #ccc;
            background-color: #fafafa; 
            padding: 15px; 
            border-radius: 15px; 
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .chat-message { 
            padding: 10px; 
            margin-bottom: 10px; 
            border-radius: 20px; 
        }
        .question, .bot-message { 
            background-color: #dddddd; 
            color: #333; 
            text-align: left; 
            margin-right: 50px;
        }
        .answer { 
            background-color: #eeeeee; 
            text-align: right; 
            margin-left: 50px;
        }
        .bot-message {
            background-color: #f0f0f0; 
            text-align: center; 
            margin: 5px 50px 10px 50px; /* تمييز رسائل البوت */
        }
        .alert-danger, .alert-success { 
            max-width: 600px; 
            margin: 20px auto; 
        }
        form { 
            max-width: 600px; 
            margin: 20px auto; 
            display: flex;
        }
        input[type="text"] { 
            flex-grow: 1; 
            margin-right: 10px; 
            margin-bottom: 10px; 
        }
        button { 
            white-space: nowrap; 
        }
        .welcome-message { 
            text-align: center; 
            margin-top: 50px;
            font-size: 24px; 
            font-weight: bold; 
        }
        .instruction { 
            text-align: center; 
            margin-top: 10px; 
            font-size: 16px; 
        }
    </style>
</head>
<body>

      <!-- Navbar (sit on top) -->
  <div class="w3-top">

    <div class="w3-bar w3-white" style="letter-spacing:4px;">
      <a href="C:\Users\الحمد لله\OneDrive\سطح المكتب\grad.project\HomePage.html" class="w3-hover-Lights w3-bar-item">
       <img src="C:\Users\الحمد لله\OneDrive\سطح المكتب\grad.project\images\HOME icon.png" alt="Logo" style="height: 40px;"> <!-- Adjust the height as needed -->
     </a>
      <!-- Right-sided navbar links -->
      <div class="w3-right w3-hide-small">
        <a href="#aboutus" class="w3-hover-pale-yellow w3-bar-item w3-button" id="ABOUT">ABOUT</a>
        <a href="#team" class="w3-hover-pale-blue w3-bar-item w3-button"id="TEAM"><i class="fa fa-user"></i> TEAM</a>
        <div class="w3-hover-pale-yellow w3-middle w3-dropdown-hover w3-hide-small">
           <button class="w3-bar-item w3-button"id="OURSERVICES" > OUR SERVICES <i class="fa fa-caret-down"></i></button>
           <div class="w3-dropdown-content w3-bar-block w3-card-4">
             <a href="C:\Users\الحمد لله\OneDrive\سطح المكتب\grad.project\scientific Articale.html"target="_blank"class="w3-hover-pale-yellow w3-bar-item w3-button"id="SpecialistCare">specialist care</a>
             <a href="#MindBot"target="_blank"class="w3-hover-pale-yellow w3-bar-item w3-button"id="MindBOT">MindBot</a>
             <a href="C:\Users\الحمد لله\OneDrive\سطح المكتب\grad.project\community.html"target="_blank" class="w3-hover-pale-yellow w3-bar-item w3-button"id="community">community</a>
           </div>

        </div>

      <a href="#contact" class="w3-hover-pale-yellow w3-bar-item w3-button"id="contact"><i class="fa fa-envelope"></i> CONTACT</a>
    </div>
    <!-- Hide right-floated links on small screens and replace them with a menu icon -->

    <a href="javascript:void(0)" class="w3-bar-item w3-button w3-right w3-hide-large w3-hide-medium" onclick="w3_open()">
      <i class="fa fa-bars"></i>
    </a>
  </div>
</div>
<div class="container w3-padding">
    <div class="chat-header">
        <div class="welcome-message ">Welcome to MindBot</div>
    </div>
    <div class="instruction">الرجاء الإجابة على جميع الأسئلة للحصول على التحليل المطلوب</div>
    <div class="chat-container">
    <img src="images/robot.png" alt="robot Icon" class="robot-icon">
        <div class="chat-message bot-message">Hi</div>
        {% for chat in chat_history %}
            <div class="chat-message {{ 'question' if chat.type == 'question' else 'answer' }}">
                {{ chat.text }}
            </div>
        {% endfor %}
        {% if show_input %}
            {% if error_message %}
                <div class="alert alert-danger">{{ error_message }}</div>
            {% endif %}
            <form method="post">
                <input type="text" class="form-control" name="answer" placeholder="اكتب إجابتك هنا..." autofocus>
                <button type="submit" class="btn btn-primary">إرسال</button>
            </form>
        {% else %}
            <div class="alert alert-success text-center">شكرا لك!</div>
            <div class="alert alert-info">
                <strong>عدد الإجابات بـ "نعم":</strong> {{ yes_count }}<br>
                <strong>عدد الإجابات بـ "لا":</strong> {{ no_count }}<br>
                <strong>التوصية:</strong> {{ diagnosis }}
            </div>
        {% endif %}
    </div>
</div>

</body>
</html>




'''

if __name__ == '__main__':
    app.run(debug=True)