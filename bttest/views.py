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

members2 = [
        {'id': '1', 'name': 'McGiney, Mark', 'email': 'mark@marksautomark.com', 'status' : 'Administrator'},
        {'id': '2', 'name': 'Alan, George', 'email': 'george@marksautomark.com', 'status' : 'Employee'},
        {'id': '3', 'name': 'Joned, Bob', 'email': 'bob@marksautomark.com', 'status' : 'Employee'},
        {'id': '4', 'name': 'O\'Brieb, Barbara', 'email': 'barbara@marksautomark.com', 'status' : 'Employee'},
    ]

def index(request):
    if request.method == 'POST':
        params = request.POST
        
        if "action" in params and params["action"] is not None and params["action"] != '':
            index = 0
            for member in members:
                if member['id'] == params["action"]:
                    del members[index]
                    break
                index = index + 1
            
            return render_to_response('index.html', {'form': MemberForm(), 'members': members}, context_instance=RequestContext(request))
        else:
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
    

def demo2(request):
    if request.method == 'POST':
        params = request.POST
        
        if "action" in params and params["action"] is not None and params["action"] != '':
            index = 0
            for member in members:
                if member['id'] == params["action"]:
                    del members[index]
                    break
                index = index + 1
            
            return render_to_response('index2.html', {'members': members}, context_instance=RequestContext(request))
        else:
            errormessage = None
            if params.get('first_name') == '' or params.get('first_name') is None:
                errormessage = "Please enter first name"
            elif params.get('last_name') == '' or params.get('last_name') is None:
                errormessage = "Please enter last name"
            elif params.get('email') == '' or params.get('email') is None:
                errormessage = "Please enter email"
            elif params.get('status') == '' or params.get('status') is None or params.get('status') == 'Select':
                errormessage = "Please select status"
            else:
                mem_id = len(members)
                name = params['last_name'] + ", " + params['first_name']
                members2.append({'id': mem_id,
                                    'name': name,
                                    'email': params['email'],
                                    'status': params['status']  
                                    })
                
            if errormessage is not None:
                return render_to_response('index2.html', {'members': members2, 'error': errormessage}, context_instance=RequestContext(request))
            else:
                return render_to_response('index2.html', {'members': members2}, context_instance=RequestContext(request))
    else:    
        return render_to_response('index2.html', {'members': members}, context_instance=RequestContext(request))
    
def delete(request, memberid=None):
    if memberid:
        index = 0
        for member in members:
            if member.id == memberid:
                break
            index = index + 1
            
        del members[index]
        return render_to_response('index.html', {'form': member_form, 'members': members}, context_instance=RequestContext(request))