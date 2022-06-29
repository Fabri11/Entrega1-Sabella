from django.shortcuts import render, get_object_or_404
from .models import Posts
from blog.forms import PostForm

# Create your views here.
def render_posts(request):
    posts = Posts.objects.all()
    return render(request, 'posts.html', {'posts':posts})


def detalles_post(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)
    return render(request, 'detalles_post.html', {"post":post})


# formulario para publicar

def postForm(request):
    if request.method == 'POST':

        miFormulario = PostForm(request.POST)
        
        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            posts = Posts(titulo = informacion['titulo'], descripcion = informacion['descripcion'], imagen = informacion['imagen'], data = informacion['data'])
            # post = get_object_or_404(Posts, pk=post_id)
            posts.save()

            return render(request, 'blog.html', {'post':post})

        else:
            miFormulario = PostForm()
            return render(request, 'post_form.html', {'miFormulario':miFormulario})
