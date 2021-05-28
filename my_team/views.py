from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'input.html')

def welcome(request):
    team=request.GET['team']
    member=request.GET['member']
    memberList=team_member.split(',')
    #입력받은 member를 ()기준을 가지고 나누어서 리스트형태로 만들고
    #입력받은 member가 중복이 되었는지 확인하고 
    
    member=[]
    #만약에 멤버리스트에서 가져온 멤버가 중복이 되지 않았다면 
    for mem in memberList:
        if mem not in member:
            member.append(mem)
    #멤버에 저장을 한다. 

    #확인한 멤버들의 수를 수치화 해야하고
    return render(request, 'welcome.html',{'team':team, 'count':len(member), 'fullmember':team_member, 'member':member}) 