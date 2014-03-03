# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
from forms import MemberForm
 
#Passing member data from view, these data should be retrieved from database
members = [
        {'id': '1', 'name': 'McGiney, Mark', 'email': 'mark@marksautomark.com', 'status' : 'Administrator'},
        {'id': '2', 'name': 'Alan, George', 'email': 'george@marksautomark.com', 'status' : 'Employee'},
        {'id': '3', 'name': 'Joned, Bob', 'email': 'bob@marksautomark.com', 'status' : 'Employee'},
        {'id': '4', 'name': 'O\'Brieb, Barbara', 'email': 'barbara@marksautomark.com', 'status' : 'Employee'},
    ]

def index(request):
    if request.method == 'POST':
        params = request.POST
        member_form = MemberForm(request.POST)
        
        if member_form.is_valid():
            mem_id = len(members)
            name = member_form.cleaned_data['last_name'] + ", " + member_form.cleaned_data['first_name']
            members.append({'id': mem_id,
                            'name': name,
                            'email': member_form.cleaned_data['email'],
                            'status': member_form.cleaned_data['status']  
                            })
            
        return render_to_response('index.html', {'form': member_form, 'members': members}, context_instance=RequestContext(request))
    else:    
        return render_to_response('index.html', {'form': MemberForm(), 'members': members}, context_instance=RequestContext(request))
    
def delete(request, id):
    if id:
        index = 0
        for member in members:
            if member.id == id:
                break
            index = index + 1
            
        
        del members[index]
        return render_to_response('index.html', {'form': member_form, 'members': members}, context_instance=RequestContext(request))