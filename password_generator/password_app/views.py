from django.shortcuts import render
from django.http import HttpResponse
from django.utils.crypto import get_random_string
from .models import SecurityQuestion, GeneratedPassword



# Create your views here.

'''
def index(request):
    if request.method == 'POST':
        # Generate passwords
        answers = [request.POST.get(f'answer{i}') for i in range(1, 11)]
        passwords = [get_random_string(16) for _ in range(3)]
        for password in passwords:
            GeneratedPassword.objects.create(password=password)
        return render(request, 'recovery.html', {'passwords': passwords, 'answers': answers})
    else:
        # Show security questions
        questions = SecurityQuestion.objects.all()
        return render(request, 'index.html', {'questions': questions})

def recovery(request):
    if request.method == 'POST':
        # Recover passwords
        answers = [request.POST.get(f'answer{i}') for i in range(1, 11)]
        passwords = [gp.password for gp in GeneratedPassword.objects.all()]
        if answers == SecurityQuestion.objects.values_list('answer', flat=True):
            return render(request, 'passwords.html', {'passwords': passwords})
        else:
            return HttpResponse('Incorrect answers.')
    else:
        # Show recovery form
        return render(request, 'recovery.html')
'''
'''
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.crypto import get_random_string
from .models import SecurityQuestion, GeneratedPassword

def index(request):
    if request.method == 'POST':
        answers = [request.POST.get(f'answer{i}') for i in range(1, 11)]
        passwords = [get_random_string(16) for _ in range(3)]
        for password in passwords:
            GeneratedPassword.objects.create(password=password)
        return render(request, 'recovery.html', {'passwords': passwords, 'answers': answers})
    else:
        questions = SecurityQuestion.objects.all()
        return render(request, 'index.html', {'questions': questions})

def recovery(request):
    if request.method == 'POST':
        answers = [request.POST.get(f'answer{i}') for i in range(1, 11)]
        passwords = [gp.password for gp in GeneratedPassword.objects.all()]
        if answers == list(SecurityQuestion.objects.values_list('answer', flat=True)):
            return render(request, 'passwords.html', {'passwords': passwords})
        else:
            return HttpResponse('Incorrect answers.')
    else:
        return render(request, 'recovery.html')
'''
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.crypto import get_random_string

from .models import SecurityQuestion, GeneratedPassword


# Create your views here.

QUESTIONS = [
    {
        'question': 'What is your favorite hobby?',
        'answers': ['Sleeping', 'Eating', 'Biking', 'Football']
    },
    {
        'question': 'What is your favorite weather?',
        'answers': ['Summer', 'Winter', 'Autumn', 'Spring']
    },
    {
        'question': 'What is your favorite animal?',
        'answers': ['Dog', 'Cat', 'Fish', 'Bird']
    },
    {
        'question': 'What is your favourite sport?',
        'answers': ['Soccer', 'Basketball', 'Football', 'Cricket']
    },
    {
        'question': 'What is your favourite social media platform?',
        'answers': ['Instagram', 'Twitter', 'TikTok', 'WhatsApp']
    }
]


def index(request):
    if request.method == 'POST':
        # Generate passwords
        answers = [request.POST.get(f'answer{i}') for i in range(1, 6)]
        if all(answers):
            passwords = [get_random_string(16) for _ in range(3)]
            return render(request, 'recovery.html', {'passwords': passwords, 'answers': answers})
        else:
            return HttpResponse('Please answer all questions.')
    else:
        # Show security questions
        return render(request, 'index.html', {'questions': QUESTIONS})


def recovery(request):
    if request.method == 'POST':
        # Recover passwords
        answers = [request.POST.get(f'answer{i}') for i in range(1, 6)]
        if answers == request.session.get('answers'):
            passwords = [gp.password for gp in GeneratedPassword.objects.all()]
            return render(request, 'passwords.html', {'passwords': passwords})
        else:
            return HttpResponse('Incorrect answers.')
    else:
        # Show recovery form
        request.session['answers'] = request.GET.getlist('a')
        return render(request, 'recovery.html')
