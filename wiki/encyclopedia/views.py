from django.shortcuts import render
from random import choice

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def getpage(request, title):

    content = util.get_entry(title)

    if content:
        message = None
    else:
        message = "Error 404: Entry not found for {}.".format(title)

    return render(request, "encyclopedia/getpage.html", {
        "title": title,
        "content": content,
        "message": message
    })

def search(request):
    if request.method == "GET":
        query = request.GET.get('q')
        entries = util.list_entries()
        results = []

        for entry in entries:
            if query.lower() in entry.lower():
                results.append(entry)

        return render(request, "encyclopedia/searchresults.html", {
            "query": query,
            "results": results
        })

    else:
        return index(request)

    return index(request)

def newpage(request):
    if request.method == "GET":
        return render(request, "encyclopedia/newpage.html")
    else:
        title = request.POST.get('title')
        content = request.POST.get('content')

        entries = util.list_entries()
        if title in entries:
            message = "Error: Page already exists."
        else:
            util.save_entry(title, content)

        return render(request, "encyclopedia/getpage.html", {
            "title": title,
            "content": content,
            "message": message
        })

    return index(request)

def editpage(request, title):
    if request.method == "GET":
        return render(request, "encyclopedia/editpage.html", {
            "entry": title,
            "content": util.get_entry(title)
        })
    else:
        newcontent = request.POST.get('content')
        util.save_entry(title, newcontent)

        return getpage(request, title)

    return index(request)

def random(request):
    entries = util.list_entries()

    return getpage(request, choice(entries))

