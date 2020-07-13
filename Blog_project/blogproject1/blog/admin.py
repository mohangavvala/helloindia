from django.contrib import admin
from blog.models import Post,comments,ContactPost

# Register your models here.
class Postadmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','id','data','code',]
    prepopulated_fields={'slug':('title',)}#populate some fields based  on some other fields.#here consider title as slug.('title',) is single value tuple
    list_filter=('status','author','created','publish')#('status',) is single value tuple . hree filtering by status
    search_fields=('title','body',)#search given word in title and body fields
    raw_id_fields=('author',)#it provides id for each author
    date_hierarchy='publish'#it provides date nav bar in the database
    ordering=['status','publish']#display order of posts based on status
admin.site.register(Post,Postadmin)
class CommentsAdmin(admin.ModelAdmin):
    list_display=('name','email','post','body','created','updated','active')#list_display tuple or list
    list_filter=('active','created','updated')#list_filter tuple or list
    search_fields=('name','email','body')
admin.site.register(comments,CommentsAdmin)

class Cont_Post_Admin(admin.ModelAdmin):
    list_display=['name','mail','subj','msg']
admin.site.register(ContactPost,Cont_Post_Admin)