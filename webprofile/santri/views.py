from django.shortcuts import render


def santri_home(request):
    return render(request, "profile_home.html")


def biodata(request):
    return render(request, "biodata.html")


def jadwal(request):
    return render(request, "jadwal.html")


def galeri(request):
    return render(request, "galeri.html")


def feedback(request):
    context = {}

    if request.method == "POST":
        context["success_message"] = "Feedback berhasil dikirim. Terima kasih atas masukannya."

    return render(request, "feedback.html", context)
