from django.shortcuts import render,redirect,get_object_or_404
from .forms import VoterRegistrationForm, ElectionOfficerRegistrationForm
from django.db.models import Count
from . models import ElectionOfficer,Voter, Election, Candidate, Vote,EligibleVoter
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.hashers import check_password


def index(request):
    return render(request,"index.html")

def officer_home(request):
    return render(request,"officer_home.html")

def voter_registration(request):
    if request.method == 'POST':
        form = VoterRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('voter_login')
    else:
        form = VoterRegistrationForm()
    return render(request, 'voter_reg.html', {'form': form})


def officer_registration(request):
    if request.method == 'POST':
        form = ElectionOfficerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('officer_login')
    else:
        form = ElectionOfficerRegistrationForm()
    return render(request, 'officer_reg.html', {'form': form})


def voter_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            voter = Voter.objects.get(username=username)
            if check_password(password, voter.password):
                return redirect('voter_home')
            else:
                return render(request, 'voter_login.html', {'error': 'Invalid credentials'})
        except Voter.DoesNotExist:
            return render(request, 'voter_login.html', {'error': 'Invalid credentials'})
    return render(request, 'voter_login.html')


def officer_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            officer = ElectionOfficer.objects.get(username=username)
            if check_password(password, officer.password):
                return redirect('officer_dashboard')
            else:
                return render(request, 'officer_login.html', {'error': 'Invalid credentials'})
        except ElectionOfficer.DoesNotExist:
            return render(request, 'officer_login.html', {'error': 'Invalid credentials'})
    return render(request, 'officer_login.html')

# def voter_reg(request):
#     return render(request,"voter_reg.html")

# def voter_login(request):
#     return render(request,"voter_login.html")

# def officer_reg(request):
#    if request.method =='POST':
#       regno = request.POST.get('regno')
#       name = request.POST.get('rname')
#       uname = request.POST.get('runame')
#       email = request.POST.get('remail')
#       phone = request.POST.get('rcontact')
#       passw = request.POST.get('rpass')
#       ElectionOfficer(register_no=regno,name=name,phone_number=phone,email=email,username=uname,password=passw).save()
#       return render(request,'officer_login.html')
#    else:
#       return render(request,"officer_reg.html")
    
# def voter_reg(request):
#    if request.method =='POST':
#       regno = request.POST.get('regno')
#       name = request.POST.get('rname')
#       uname = request.POST.get('runame')
#       email = request.POST.get('remail')
#       phone = request.POST.get('rcontact')
#       passw = request.POST.get('rpass')
#       Voterr(register_no=regno,name=name,phone_number=phone,email=email,username=uname,password=passw).save()
#       return render(request,'voter_login.html')
#    else:
#       return render(request,"voter_reg.html")
  
# def voter_home(request):
#     return render(request,'voter_home.html')
    

# def voter_login(request):
#     if request.method=='POST':
#         regno =  request.POST.get('regno')
#         uname = request.POST.get('runame')
#         passw = request.POST.get('rpass')
#         cr = Voterr.objects.filter(register_no=regno,username=uname,password=passw)
#         if cr:
#             details = Voterr.objects.get(username=uname, password = passw,register_no=regno)
#             username = details.username
#             request.session['cs']=username
#             regno = details.register_no
#             request.session['regno']=regno
            
#             return render(request,'voter_home.html')
#         else:
#             message="Invalid Username Or Password"
#             return render(request,'voter_login.html',{'me':message})
#     else: 
#         return render(request,'voter_login.html')

# def officer_login(request):
#     if request.method=='POST':
#         regno =  request.POST.get('regno')
#         uname = request.POST.get('runame')
#         passw = request.POST.get('rpass')
#         cr = ElectionOfficer.objects.filter(register_no=regno,username=uname,password=passw)
#         if cr:
#             details = ElectionOfficer.objects.get(username=uname, password = passw,register_no=regno)
#             username = details.username
#             request.session['cs']=username
#             regno = details.register_no
#             request.session['regno']=regno
            
#             return render(request,'officer_home.html')
#         else:
#             message="Invalid Username Or Password"
#             return render(request,'officer_login.html',{'me':message})
#     else: 
#         return render(request,'officer_login.html')

# def officer_profile(request):
#     c=request.session['cs']
#     cr=ElectionOfficer.objects.get(username=c)
#     pregno=cr.register_no
#     pname=cr.name
#     puname=cr.username
#     pemail=cr.email
#     pcontact=cr.phone_number
#     paddress=cr.address
#     pcreatedat=cr.created_at
#     return render(request,"officer_profile.html",{'regno':pregno,'name':pname,'uname':puname,'contact':pcontact,'email':pemail,'address':paddress,'created_at':pcreatedat})


# Add eligible voters
def add_voter(request):
    if request.method == "POST":
        mobile_number = request.POST['mobile_number']
        EligibleVoter.objects.create(mobile_number=mobile_number)
        return redirect('add_voter/')
    return render(request, 'add_voter.html')

# Create an election
def create_election(request):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        election = Election.objects.create(
            name=name,
            description=description,
            start_time=start_time,
            end_time=end_time
        )
        return redirect('create_election')
    return render(request, 'create_election.html')

# Manage candidates
def manage_candidates(request, election_id):
    election = Election.objects.get(id=election_id)
    if request.method == "POST":
        name = request.POST['name']
        party = request.POST['party']
        Candidate.objects.create(election=election, name=name, party=party)
        return redirect('manage_candidates', election_id=election.id)
    candidates = election.candidates.all()
    return render(request, 'manage_candidates.html', {'election': election, 'candidates': candidates})

# Monitor voting (View live data)
def monitor_voting(request, election_id):
    # Fetch the election object
    election = Election.objects.get(id=election_id)
    
    # Fetch candidates and their votes for the election
    candidates = Candidate.objects.filter(election=election).annotate(
        votes=Count('vote')
    )
    
    # Calculate the total votes
    total_votes = sum(candidate.votes for candidate in candidates)
    
    # Pass the context to the template
    context = {
        'election': election,
        'candidates': candidates,
        'total_votes': total_votes
    }
    return render(request, 'monitor_voting.html', context)

# Publish results

def election_results(request, election_id):
    # Fetch election and related data
    election = Election.objects.get(id=election_id)
    candidates = Candidate.objects.filter(election=election).annotate(
        votes=Count('vote')
    )
    
    # Determine the winner (candidate with the most votes)
    winner = max(candidates, key=lambda c: c.votes, default=None)
    for candidate in candidates:
        candidate.is_winner = candidate == winner

    # Pass data to the template
    return render(request, 'election_results.html', {
        'election': election,
        'candidates': candidates,
        'winner': winner if not election.is_ongoing else None,
    })

def election_list(request):
    elections = Election.objects.all()  # Retrieve all elections
    return render(request, 'election_list.html', {'elections': elections})

# View Elections: List of active elections the voter can participate in
def view_elections(request):
    if request.method == "POST":
        mobile_number = request.POST.get('mobile_number')
        try:
            voter = Voter.objects.get(mobile_number=mobile_number)
            # Get the elections the voter is eligible for
            eligible_elections = Election.objects.filter(is_active=True)
            return render(request, 'view_elections.html', {'voter': voter, 'eligible_elections': eligible_elections})
        except Voter.DoesNotExist:
            return render(request, 'view_elections.html', {'error': 'Voter not found or not eligible.'})
    return render(request, 'view_elections.html')

# Vote Casting: Voters cast their vote for a candidate in a specific election
def cast_vote(request, election_id):
    election = get_object_or_404(Election, id=election_id)
    
    if request.method == "POST":
        mobile_number = request.POST.get('mobile_number')
        candidate_id = request.POST.get('candidate')
        
        try:
            voter = Voter.objects.get(mobile_number=mobile_number)

            # Check if the voter has already voted in this election
            existing_vote = Vote.objects.filter(election=election, voter=voter).first()
            if existing_vote:
                return render(request, 'cast_vote.html', {
                    'election': election,
                    'candidates': election.candidates.all(),
                    'error': 'You have already voted using this mobile number.',
                })

            candidate = Candidate.objects.get(id=candidate_id)

            # Save the vote
            Vote.objects.create(election=election, voter=voter, candidate=candidate)
            return render(request, 'thank_you.html', {'message': 'Your vote has been cast successfully!'})

        except Voter.DoesNotExist:
            return render(request, 'cast_vote.html', {
                'election': election,
                'candidates': election.candidates.all(),
                'error': 'This mobile number is not registered.',
            })

        except Candidate.DoesNotExist:
            return render(request, 'cast_vote.html', {
                'election': election,
                'candidates': election.candidates.all(),
                'error': 'Invalid candidate selection.',
            })

    # Render the voting page with election details and candidates
    return render(request, 'cast_vote.html', {
        'election': election,
        'candidates': election.candidates.all(),
    })
# Eligibility Check: Voter checks if they are eligible to vote
def check_eligibility(request):
    if request.method == "POST":
        mobile_number = request.POST.get('mobile_number')
        try:
            eligiblevoter = EligibleVoter.objects.get(mobile_number=mobile_number)
            return render(request, 'check_eligibility.html', {'voter': eligiblevoter, 'eligible': eligiblevoter.is_eligible})
        except Voter.DoesNotExist:
            return render(request, 'check_eligibility.html', {'error': 'Voter not found.'})
    return render(request, 'check_eligibility.html')

# Election Countdown: Show the countdown timer until the election ends
def election_countdown(request, election_id):
    election = Election.objects.get(id=election_id)
    time_remaining = election.end_time - timezone.now()
    return render(request, 'election_countdown.html', {'election': election, 'time_remaining': time_remaining})

def live_results(request, election_id):
    election = Election.objects.get(id=election_id)
    return render(request, 'live_results.html', {'election': election})

def live_results_data(request, election_id):
    election = Election.objects.get(id=election_id)
    candidates = Candidate.objects.filter(election=election).annotate(
        votes=Count('vote')
    )
    time_remaining = max(election.end_time - timezone.now(), timezone.timedelta(0))

    # Create JSON response
    data = {
        'candidates': [
            {'name': candidate.name, 'party': candidate.party, 'votes': candidate.votes}
            for candidate in candidates
        ],
        'time_remaining': str(time_remaining)
    }
    return JsonResponse(data)


