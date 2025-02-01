from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class Voter(models.Model):
    id_number = models.CharField(max_length=20, unique=True)
    profile_picture = models.ImageField(upload_to='voters/', blank=True, null=True)
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class ElectionOfficer(models.Model):
    id_number = models.CharField(max_length=20, unique=True)
    profile_picture = models.ImageField(upload_to='officers/', blank=True, null=True)
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    address = models.TextField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

# class Voterr(models.Model):
#     register_no = models.IntegerField()
#     name = models.CharField(max_length=100)
#     username = models.CharField(max_length=100)
#     email = models.EmailField(max_length=255)
#     phone_number = models.CharField(max_length=15)
#     address = models.TextField()
#     password = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.name
    
# class ElectionOfficer(models.Model):
#     register_no = models.IntegerField()
#     name = models.CharField(max_length=100)
#     username = models.CharField(max_length=100)
#     email = models.EmailField(max_length=255)
#     phone_number = models.CharField(max_length=15)
#     address = models.TextField()
#     password = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.name

# Model for eligible voters
class EligibleVoter(models.Model):
    mobile_number = models.CharField(max_length=15, unique=True)
    is_eligible = models.BooleanField(default=True)
    
    def __str__(self):
        return self.mobile_number

# Model for election
class Election(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_active = models.BooleanField(default=False)
    
    def is_ongoing(self):
        now = timezone.now()
        return self.start_time <= now <= self.end_time

    def __str__(self):
        return self.name

# Model for candidates
class Candidate(models.Model):
    election = models.ForeignKey(Election, related_name="candidates", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    party = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='candidates/', blank=True, null=True)
    
    def __str__(self):
        return self.name

# Model for votes
class Vote(models.Model):
    election = models.ForeignKey(Election, related_name="votes", on_delete=models.CASCADE)
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.voter} voted for {self.candidate} in {self.election.name}"

