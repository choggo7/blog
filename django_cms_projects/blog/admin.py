from django.contrib import admin
from .models import post,category
# Register your models here.

admin.site.register(category)

class categoryAdmin(admin.ModelAdmin):
	list_display = ('name','slug')
	prpopulated_fields = {'slug' : ('name',)}


admin.site.register(post)

class postAdmin(admin.ModelAdmin):
	list_display = ('title','published','category','created','status')
	list_filter = ('created','published','category','status')
	search_fields = ('title')
	prpopulated_fields = {'slug' : ('title',)}

