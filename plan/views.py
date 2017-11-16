from django.shortcuts import get_object_or_404, render, redirect, reverse, HttpResponseRedirect
from django.utils import timezone
from django.http import FileResponse
from django.forms import inlineformset_factory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post, Participant
from .forms import PostForm, ParticipantForm
# Create your views here.
'''
def post_list(request):
    posts = Post.objects.order_by('published_date')[:5]
    context = {'posts': posts}
    return render(request, 'plan/post_list.html', context)
'''
def post_list(request):
    posts = Post.objects.order_by('published_date')
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    try:
        post_col = paginator.page(page)
    except PageNotAnInteger:
        post_col = paginator.page(1)
    except EmptyPage:
        post_col = paginator.page(paginator.num_pages)
    context = {'post_col': post_col}
    return render(request, 'plan/post_list.html', context)

def participant_list(request):
    participants = Participant.objects.order_by('name')
    paginator = Paginator(participants, 10)
    page = request.GET.get('page')
    try:
        part_col = paginator.page(page)
    except PageNotAnInteger:
        part_col = paginator.page(1)
    except EmptyPage:
        part_col = paginator.page(paginator.num_pages)
    context = {'part_col': part_col}
    return render(request, 'plan/participant_list.html', context)

def participant_detail(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    return render(request, 'plan/participant_detail.html', {'participant': participant})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'plan/post_detail.html', {'post': post})

def post_new(request):
    ParticipantFormSet = inlineformset_factory(Post, Participant, form = ParticipantForm)
    if request.method == "POST":
        form = PostForm(request.POST)
        formset = ParticipantFormSet(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            formset.save(commit=False)
            post.save()
            return redirect('plan:post_detail', pk=post.pk)
        else:
            return render(request, 'plan/post_edit.html', {
                'form':form,
                'formset':formset,
        })
    else:
        form = PostForm()
        formset = ParticipantFormSet()
        return render(request, 'plan/post_edit.html', {'form': form, 'formset':formset,})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    ParticipantFormSet = inlineformset_factory(Post, Participant, form = ParticipantForm)
    if request.method == "POST":
        formset = ParticipantFormSet(request.POST, request.FILES, instance=post)
        if formset.is_valid():
            formset.save()
            return redirect('plan:post_detail', pk)
    else:
        formset = ParticipantFormSet(instance=post)
    return render(request, 'plan/post_edit.html', {'formset': formset})

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)
