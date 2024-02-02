from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse

# converts something into a string
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None
}
# Create your views here.


def january(request):
    # HttpResponse is a class we are instantiating
    # As argument to this instructor function, we pass the response data
    return HttpResponse("Eat no meat for the entire month!")


def index(request):

    months = list(monthly_challenges.keys())

    #### THIS WAS USED WHEN THERE WAS STILL NO HTML FILE####
    # list_items = ""
    # for month in months:
    #    capitalized_month = month.capitalize()
    #    month_path = reverse("month-challenge", args=[month])
    #    list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)
    ##########################################################

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    # keys refer to the months
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = months[month-1]

    # to change url and send a new request
    # this kind of path is not dynamic, it would result to an error if there are some changes in naming of url
    # it is also harder to change the hard-coded manually
    # return HttpResponseRedirect("/challenges/"+redirect_month)

    # reverse keyword figures how to correctly build a path for the month-challenge url
    redirect_path = reverse("month-challenge", args=[redirect_month])
    # this is the dynamic way to change url
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # response_data=render_to_string("challenges/challenge.html") # read the html file and transform content to string
        # return HttpResponse(response_data)

        # shortcut of render string
        return render(request, "challenges/challenge.html", {
            # key_value pair that would be used for html;called as context for this template
            "text": challenge_text,
            "month_name": month
        })

    except:
        # not recommended since it is hard-coded
        # return HttpResponseNotFound("<h1>This month is not supported!</h1>")

        ################################################
        # can't use the render function since it always renders a success response
        # the right way is sending back a 404 page for 404 errors

        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)

        ###############################################
        # Django has another shortcut for 404 error using Http404
        # it is not a response but a class you raised as an error
        # it would look for 404 html file in templates folder
        # For this to work, set DEBUG = false in Django settings file(only works in DEPLOYMENT)

        raise Http404()
