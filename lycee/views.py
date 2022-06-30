import datetime

from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Cursus
from .models import Student
from .models import CallOfRoll
from django.template import loader
from .forms import StudentForm, CallOfRollForm



# Example Simple Text Page
# def index(request):
#     return HttpResponse("Racine de lycée")

# ----------------------------------------------------------------------
# Example URL attrib. Page
def detail(request, cursus_id):
    resp = 'result for cursus {}'.format(cursus_id)
    return HttpResponse(resp)


# ----------------------------------------------------------------------
def index(request):
    result_list = Cursus.objects.order_by('name')
    # Chargement du template

    # Context
    context = {
        "liste": result_list,
    }
    return render(request, 'lycee/index.html', context)


# ----------------------------------------------------------------------
def handler404(request, exception):
    return render(request, 'error404.html')


# ----------------------------------------------------------------------
def ClassView(request, cursusId):
    cursus = Cursus.objects.get(id=cursusId)

    result_list = Student.objects.filter(cursus_id=cursusId)
    result_list = result_list.order_by('last_name')

    # Chargement du template

    # Context
    context = {
        "liste": result_list,
        "cursus_name": cursus.name
    }
    return render(request, 'lycee/ClassView.html', context)

# ----------------------------------------------------------------------
def callRollClassroomView(request, cursusId):

    if request.method == "POST":
        print(request.POST)

        # Get the last COR id and increment it by 1
        callrollList = CallOfRoll.objects.all()
        callrollList.order_by('id')
        newCORid = callrollList.last().id + 1

        # For each absent student
        for student_id in request.POST.getlist('absent'):

            date = request.POST.getlist('dateAbsence')
            sDate = "".join(date)
            print("Date input : " + sDate)

            COR = CallOfRoll(
                newCORid,
                sDate,
                True,
                "Aucun",
                Student.objects.get(pk=student_id).id
            )
            COR.save()

            newCORid = newCORid + 1 # Don t forget it !

        return redirect("/lycee")

    else:
        cursus = Cursus.objects.get(id=cursusId)
        student_list = Student.objects.filter(cursus_id=cursusId)

        date_now = str(datetime.date.today())

        # Context
        context = {
            "liste": student_list,
            "cursus_name": cursus.name,
            "date_now": date_now
        }

        return render(request, 'lycee/CallRollView.html', context)


# ----------------------------------------------------------------------
def studentView(request, studentId):
    student = Student.objects.get(id=studentId)
    cursus = Cursus.objects.get(id=student.cursus_id)

    # Chargement du template

    # Context
    context = {
        "student": student,
        "cursus_name": cursus.name
    }
    return render(request, 'lycee/studentView.html', context)


# ----------------------------------------------------------------------
def createStudentForm(request):

    form = StudentForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()

    context = {
        "form": form
    }

    return render(request, 'lycee/createStudentForm.html', context)


# ----------------------------------------------------------------------
def editStudentForm(request, studentId):

    student = Student.objects.get(id=studentId)

    form = StudentForm(request.POST or None, instance=student)

    if form.is_valid():
        form.save()

    context = {
        "form": form
    }

    return render(request, 'lycee/createStudentForm.html', context)


# ----------------------------------------------------------------------
def callOfRoll(request):
    if request.method == "POST":
        form = CallOfRollForm(request.POST).save()
        return redirect("/lycee")

    else:
        form = CallOfRollForm()

        context = {
            "form": form
        }

        return render(request, 'lycee/particularCallRollView.html', context)

# ----------------------------------------------------------------------
def lyceeManagement(request):
    resp = 'lycee management.'
    return HttpResponse(resp)
