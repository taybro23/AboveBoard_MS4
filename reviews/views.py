from django.shortcuts import render


def reviews(request):
    """ A view to return the reviews """

    return render(request, 'reviews/reviews.html')
