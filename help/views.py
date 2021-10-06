from django.shortcuts import render


def help_guidance(request):
    """ A view to return the help and guidance page """

    return render(request, 'help/help.html')
