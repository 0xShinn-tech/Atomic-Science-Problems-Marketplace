from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    expertise = models.CharField(max_length=200, blank=True)
    reputation = models.IntegerField(default=0)
    profile_picture = models.URLField(blank=True)
    
class Problem(models.Model):

    STATUS_CHOICES = [
        ("open", "Open"),
        ("in_progress", "In Progress"),
        ("solved", "Solved"),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100, default='Geral')
    difficulty = models.CharField(max_length=20, default='Fácil')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="open"
    )
    best_solution = models.ForeignKey(
        "Solution",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="best_for"
    )
    created_at = models.DateTimeField(auto_now_add=True)

class Solution(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    version = models.IntegerField(default=1)
    parent_solution = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    is_validated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, null=True, blank=True)
    solution = models.ForeignKey(Solution, on_delete=models.CASCADE, null=True, blank=True)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    

class ReputationEvent(models.Model):

    ACTIONS = [
        ("create_problem", "+ Problem"),
        ("create_solution", "+ Solution"),
        ("solution_accepted", "Accepted Solution"),
        ("comment_helpful", "Helpful Comment"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=50, choices=ACTIONS)
    points = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)    