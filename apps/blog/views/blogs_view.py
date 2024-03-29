from django.http import HttpResponse
from django.views import View  # import the View parent class

class BlogsView(View):  # create a view class
    # change the function-based view to be called get and add the self param
    def get(self, request):
        html = '<html><body>Blogs page works!</body></html>'
        return HttpResponse(html)