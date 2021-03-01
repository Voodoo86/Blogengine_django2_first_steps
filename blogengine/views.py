from django.shortcuts import redirect


def redirect_blog(request):
     """Redirect for Second Domain Level"""
     return redirect('posts_list_url', permanent=True)
