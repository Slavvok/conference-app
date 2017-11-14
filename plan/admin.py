from django.contrib import admin
from .models import Post, Participant, Group, Faculty, Course, Presentation
# Register your models here.

class ParticipantInLine(admin.TabularInline):
    model = Participant
    extra = 3

class PostAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'title', 'created_date')
    fieldsets = [
        ('User', {'fields': ['author']}),
        ('Title', {'fields': ['title']}),
        ('Text', {'fields': ['text']}),
        ('Date', {'fields': ['conference_date'],
                    'classes': ['collapse']})
    ]
    inlines = [ParticipantInLine]

class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_id', 'name', 'course', 'faculty')

class FacultyAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'name')
    fieldsets = [
        ('Faculty', {'fields': ['name']})
    ]

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'name')
    fieldsets = [
        ('Course', {'fields': ['name']})
    ]

class PresentationAdmin(admin.ModelAdmin):
    list_display = ('pres_id', 'description')
    fieldsets = [
        ('Name', {'fields': ['description']}),
        ('Upload', {'fields': ['upload']})
    ]

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'group', 'course', 'faculty')

admin.site.register(Post, PostAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Presentation, PresentationAdmin)
