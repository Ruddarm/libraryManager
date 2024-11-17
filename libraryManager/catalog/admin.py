from django.contrib import admin
from .models import Book,BookInstance,Genre,Author,Language

# admin.site.register(Book)
# admin.site.register(BookInstance)
# admin.site.register(Author)
admin.site.register(Language)
admin.site.register(Genre)
# Register your models here.

class BookInsatanceInline (admin.TabularInline):
    model=BookInstance
class BookInline (admin.TabularInline):
    model=Book
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display= ('last_name','first_name','date_of_birth','date_of_death')
    fields=('last_name','first_name',('date_of_birth','date_of_death'))
    inlines=[BookInline]
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
        list_display = ('title', 'author', 'display_genre')
        inlines= [BookInsatanceInline]       
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display=('id','imprint','status','due_back')
    list_filter = ('status','due_back')
    fieldsets = (
        (None, {
            "fields": (
                'book','imprint','id'
            ),
        }),
        ('Avialbility',{
            'fields':(
                'status','due_back'
            )
        }),
    )
