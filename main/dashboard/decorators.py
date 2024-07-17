from main import models
from django.shortcuts import redirect

def isOwner(objmodels):
    def decorator(funk):
        def wrapper(request, id):
            if request.user == objmodels.objects.get(id=id).author:
                return funk(request, id)
            else:
                return redirect('index')
        return wrapper
    return decorator