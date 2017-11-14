from django.db import models
from django.utils import timezone
from django import forms

# Post is a single conference info model
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=50)
    text = models.TextField()
    conference_date = models.DateTimeField(
            blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
#Student's faculty
class Faculty(models.Model):
    faculty_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)
#Student's course
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)
#Student's group
class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)
#Presentation class
class Presentation(models.Model):
    pres_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    upload = models.FileField(upload_to='presentation', null=True)
    def __str__(self):
        return self.description
#Information about participants
class Participant(models.Model):
    STUDENT = 'ST'
    TEACHER = 'TE'
    PROFESSOR = 'PR'
    POSITION_CHOICES = (
        (STUDENT, 'Студент'),
        (TEACHER, 'Преподаватель'),
        (PROFESSOR, 'Профессор'),
    )
    name = models.CharField(max_length=50, default="")
    surname = models.CharField(max_length=50, default="")
    patronymic = models.CharField(max_length=50, default="")
    position = models.CharField(max_length = 9, choices = POSITION_CHOICES,
                                default = STUDENT)
    conference = models.ForeignKey(Post, related_name = 'members', on_delete=models.CASCADE, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True, blank=True)
    presentation = models.ForeignKey(Presentation, related_name = 'pres', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
