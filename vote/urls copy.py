"""
URL configuration for votesphere project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('officer_home/',views.officer_home,name='officer_home'),
    path('voter_home/',views.voter_home,name='voter_home'),
    
    
    
    
    #voter
    path('voter_login/',views.voter_login,name='voter_login'),
    path('voter_reg/',views.voter_reg,name='voter_reg'),
    
    #officer
    path('officer_login/',views.officer_login,name='officer_login'),
    path('officer_reg/',views.officer_reg,name='officer_reg'),
    path('officer_home/',views.officer_home,name='officer_home'),
    path('officer_profile/',views.officer_profile,name='officer_profile'),
    
    
    path('add_voter/', views.add_voter, name='add_voter'),
    path('create_election/', views.create_election, name='create_election'),
    path('manage_candidates/<int:election_id>/', views.manage_candidates, name='manage_candidates'),
    path('monitor_voting/<int:election_id>/', views.monitor_voting, name='monitor_voting'),
    path('election_results/<int:election_id>/', views.election_results, name='election_results'),
    path('election_list/', views.election_list, name='election_list'),  # URL for the election list page
    
    path('view_elections/', views.view_elections, name='view_elections'),
    path('cast_vote/<int:election_id>/', views.cast_vote, name='cast_vote'),
    path('check_eligibility/', views.check_eligibility, name='check_eligibility'),
    path('election_countdown/<int:election_id>/', views.election_countdown, name='election_countdown'),
    # Add other necessary URLs...
    
    path('live_results/<int:election_id>/', views.live_results, name='live_results'),
    path('live_results/<int:election_id>/data/', views.live_results_data, name='live_results_data'),
    
]
