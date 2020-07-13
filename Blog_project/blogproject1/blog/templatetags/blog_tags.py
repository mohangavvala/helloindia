from blog.models import Post
from django import template
register=template.Library()

@register.simple_tag(name='my_tag')
def total_posts():
    return Post.objects.count() # it return total number of posts published upto now


@register.inclusion_tag('blog/latest_posts.html')#the context passed to the latest_posts.html
#def show_latest_posts():
#    latest_posts=Post.objects.order_by('-publish')[:3]#latest three post_list
#    return{'latest_posts':latest_posts}#passing a context
def show_latest_posts(count=3):# here count=3 default we pass argument for count from bsae.htm file  {%show_latest_posts   4%}  4 is argment for count
    latest_posts=Post.objects.order_by('-publish')[:count]#latest three post_list we pass any count value from base.html
    return{'latest_posts':latest_posts}#passing a context



from django.db.models import Count
@register.assignment_tag
def  get_most_commented_posts(count=5):

    return  Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
    #it means count the total comments related to that post and assign that value to temporary variable total_comments.based on number of
    # total_comments display the posts
