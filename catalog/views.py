from django.shortcuts import render
from django.views import generic
from .models import Tool, Host, ToolInstance, ToolType
from django.shortcuts import get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_tools = Tool.objects.all().count()
    num_instances = ToolInstance.objects.all().count()

    # Available tools (status = 'a')
    num_instances_available = ToolInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_hosts = Host.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_tools': num_tools,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_hosts,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class HostListView(generic.ListView):
    model = Host
    paginate_by = 12
    # ==============


class HostDetailView(generic.DetailView):
    model = Host


def host_detail_view(request, primary_key):
    try:
        host = Host.objects.get(pk=primary_key)
    except Host.DoesNotExist:
        raise Http404('Host does not exist')

    return render(request, 'catalog/host_detail.html', context={'host': host})


class ToolListView(generic.ListView):
    model = Tool
    paginate_by = 12


class ToolDetailView(generic.DetailView):
    model = Tool


def tool_detail_view(request, primary_key):
    try:
        tool = Tool.objects.get(pk=primary_key)
    except Tool.DoesNotExist:
        raise Http404('Tool does not exist')

    return render(request, 'catalog/tool_detail.html', context={'tool': tool})

class LoanedToolsByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing tools on loan to current user."""
    model = ToolInstance
    template_name ='catalog/toolinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return ToolInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
