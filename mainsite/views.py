from django.shortcuts import render, render_to_response, redirect
from django.template.loader import get_template
from django.http import HttpResponse
from datetime import datetime
from .models import Post
import markdown

# Create your views here.
def homepage(request):
	template = get_template('index.html')
	posts = Post.objects.all()
	now = datetime.now()
	html = template.render(locals())	
	# return HttpResponse(html)
	return render_to_response('index.html', {'posts': posts, 'now': now})

def showpost(request, id):
	template = get_template('post.html')
	try:
		post = Post.objects.get(id=id)
		if post != None:
			html = template.render(locals())
			postText = markdown.markdown(post.body, extensions=[
				'markdown.extensions.extra',
				'markdown.extensions.codehilite',
				'markdown.extensions.tables',
				'markdown.extensions.toc'
				])
			# return HttpResponse(html)
			return render_to_response('post.html', {'post': post, 'postText': postText})
	except:
		return redirect('/')