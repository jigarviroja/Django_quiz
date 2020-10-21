from django.shortcuts import render, HttpResponse, redirect
from .forms import UserForm
from .models import FinalResult
from datetime import datetime
# Create your views here.


def viewuser(request):
    if request.method == 'GET':
        form = UserForm()
        return render(request, 'user.html', {'form': form})

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid:
            request.session['username'] = form.data['name']
            request.session['counter'] = 0
            return redirect('Question1')
        else:
            return render(request, 'user.html', {'form': form})


# def quiz(request):
#     if request.method == 'GET':

#         questions = Question.objects.all()
#         questions = questions[request.session['counter']]
#         options = Option.objects.filter(question=questions)
#         return render(request, 'question1.html', {'question': questions, 'options': options})

#     if request.method == 'POST':
#         request.session['counter'] += 1
#         print(request.session['counter'])

#         if request.session['counter'] >= Question.objects.all().count():
#             return redirect('Index')
#         else:
#             question_id = request.POST.get('id1')
#             print('-------------', question_id)
#             question = Question.objects.get(id=question_id)
#             user = Person.objects.filter(
#                 name=request.session['username']).last()
#             result = Result()
#             print('+-+-+-+', question.question_type)
#             if question.question_type == 'single':
#                 option = request.POST.get('option')
#                 print('++++++++++++++', option)
#                 result.name = user
#                 result.question = question
#                 result.option = option
#                 result.save()
#             else:
#                 option1 = request.POST.get('option1')
#                 option1 += ' '+request.POST.get('option2')
#                 option1 += ' '+request.POST.get('option3')
#                 option1 += ' '+request.POST.get('option4')
#                 print('++++', option1)
#                 result.name = user
#                 result.question = question
#                 result.option = option1
#                 result.save()

#             return redirect('Quiz')


def question1(request):

    if request.method == 'GET':
        return render(request, 'question1 copy.html')

    if request.method == 'POST':
        question = request.POST.get('question')
        option = request.POST.get('option')
        date = datetime.today()
        name = request.session['username']
        FinalResult.objects.create(
            name=name, question=question, option=option, time=date)
        return redirect('Question2')


def question2(request):
    if request.method == 'GET':
        return render(request, 'question2.html')

    if request.method == 'POST':
        ls = []
        question = request.POST.get('question')
        if request.POST.get('option1') != None:
            ls.append(request.POST.get('option1'))

        if request.POST.get('option2') != None:
            ls.append(request.POST.get('option2'))

        if request.POST.get('option3') != None:
            ls.append(request.POST.get('option3'))

        if request.POST.get('option4') != None:
            ls.append(request.POST.get('option4'))

        ls = ','.join(ls)
        name = request.session['username']
        date = datetime.today()
        print(date)
        FinalResult.objects.create(
            name=name, question=question, option=ls, time=date)

        return redirect('Summery')


# def last(request):
#     # return render(request, 'last.html')

#     if request.method == 'POST':
#         return redirect(request, "History")


def summery(request):
    result = FinalResult.objects.filter(name=request.session['username'])
    return render(request, 'summery.html', {'result': result})


def history(request):
    # result = FinalResult.objects.filter(name=request.session['username'])
    result = FinalResult.objects.all()
    return render(request, 'history.html', {'result': result})
