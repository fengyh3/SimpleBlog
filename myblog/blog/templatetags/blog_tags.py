from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

from ..models import Post

@register.simple_tag
def total_posts():
	return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
	latest_posts = Post.published.order_by('-publish')[:count]
	return {'latest_posts': latest_posts}

@register.inclusion_tag('blog/post/most_commented_posts.html')
def get_most_commented_posts(count=5):
	most_commented_posts = Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
	return {'most_commented_posts': most_commented_posts}

@register.filter(name='markdown')
def markdown_format(text):
	return mark_safe(markdown.markdown(text))