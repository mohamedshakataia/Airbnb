from django.contrib import admin
from . import models
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class RoomImagesTabular(admin.TabularInline):
    model = models.RoomImage


class RoomAdmin(SummernoteModelAdmin,admin.ModelAdmin):
    list_display= ['name','price','location']
    inlines=[RoomImagesTabular,]
    summernote_fields = ('description',)
    prepopulated_fields = {'slug':("name",)}




admin.site.register(models.Room,RoomAdmin)
# admin.site.register(models.RoomImage)
admin.site.register(models.category)
admin.site.register(models.RoomReview)
admin.site.register(models.RoomBook)


