from django.contrib.auth.decorators import login_required
from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from meetings.models import Meeting, Room


# Create your views here.
def welcome(request):
    if  request.user.is_authenticated:
        context = {"meetings": Meeting.objects.all()}
    else:
        context ={}
    return render(request, "website/welcome.html", context)


def about(request):
    return HttpResponse("I'm Loyce and i'm currently learning django!")

@login_required
def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "website/detail.html", {"meeting": meeting})


def rooms(request):
    return render(request, "website/rooms.html",
                  {"rooms": Room.objects.all()})


MeetingForm = modelform_factory(Meeting, exclude=[])

@login_required
def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, "website/new.html", {"form": form})

@login_required
def edit(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    if request.method == "POST":
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            return redirect("detail", id)
    else:
        form = MeetingForm(instance=meeting)
    return render(request, "website/edit.html", {"form": form})

@login_required
def delete(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    if request.method == "POST":
        meeting.delete()
        return redirect("welcome")
    else:
        return render(request, "website/delete.html", {"meeting": meeting})



