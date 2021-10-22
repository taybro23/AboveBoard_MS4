from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator

from .models import HelpGuidance
from .forms import PostForm


def all_posts(request):
    """ A view to return all posts """

    help_guidance_posts = HelpGuidance.objects.all()

    paginator_posts = Paginator(help_guidance_posts, 4)
    page = request.GET.get('page')
    post_pages = paginator_posts.get_page(page)
    nums = 'a' * post_pages.paginator.num_pages

    context = {
        'help_guidance_posts': help_guidance_posts,
        'post_pages': post_pages,
        'nums': nums,
    }

    return render(request, 'help/help.html', context)


def post_detail(request, post_id):
    """ A view to return post details """

    post = get_object_or_404(HelpGuidance, pk=post_id)

    context = {
        'post': post,
    }

    return render(request, 'help/post_detail.html', context)


# @login_required
# def add_post(request):
#     """ A view to add posts """

#     if not request.user.is_superuser:
#         messages.error(request, 'Sorry, only store owners \
#             and admins can access this page!')
#         return redirect(reverse('home'))

#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save()
#             messages.success(request, 'Successfully added Post!')
#             return redirect(reverse('post_detail', args=[post.id]))
#         else:
#             messages.error(request, 'Failed to add Product, please \
#                            ensure the form is valid.')
#     else:
#         form = PostForm()

#     template = 'help/add_post.html'
#     context = {
#         'form': form
#     }

#     return render(request, template, context)


@login_required
def add_post(request):
    """ Add a post to the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners \
            and admins can access this page!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Successfully added post!')
            return redirect(reverse('post_detail', args=[post.id]))
        else:
            messages.error(request, 'Failed to add post, please \
                           ensure the form is valid.')
    else:
        form = PostForm()

    template = 'help/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_post(request, post_id):
    """ A view to edit post """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners \
                       can access this page.')
        return redirect(reverse('home'))

    post = get_object_or_404(HelpGuidance, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Post!')
            return redirect(reverse('post_detail', args=[post_id]))
        else:
            messages.error(request, 'Failed to update post, please \
                           ensure the form is valid.')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'help/edit_post.html'

    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_post(request, post_id):
    """ A view to delete post """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can \
                       access this page.')
        return redirect(reverse('home'))

    post = get_object_or_404(HelpGuidance, pk=post_id)
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('all_posts'))
