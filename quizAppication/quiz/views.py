from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login, logout
from quiz.models import Question, QuizModel, QuizQuestionMap, ScoreModel



class Main(View):
    def get(self, request):
        return render(request, 'landing-page.html', context={})



class Login(View):
    def get(self, request):
        return render(request, 'login-view.html', context={})

    def post(self, request):

        if request.POST.get("call") == 'login':
            emailid = request.POST.get('email_id')
            passwod = request.POST.get('password')
            user = authenticate(email = emailid, password=passwod)

            if user is not None:
                login(user)
                return JsonResponse({"msg": "loggedin", "status":"200", "redirect":"dashboard"})
            else:
                return JsonResponse({"msg":"failed ! user not found", "status":"200", "redirect":"login"})
        else:
            logout(request)
            return JsonResponse({"msg":" user logged ! out", "status":"200", "redirect":"landing-page"})

class Dashboard(View):
    def get(self, request):
        quiz_model = QuizModel.objects.all()
        import ipdb; ipdb.set_trace()
        current_user = request.user.get_username()
        current_score = 0

        return render(request, 'dashboard.html', context={"quiz_model":quiz_model, "current_score":current_score})