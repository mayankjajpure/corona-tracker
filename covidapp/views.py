from django.shortcuts import render,HttpResponse
import json
# Create your views here.
import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "20aa3c85c0mshfbf5b454f19812ep1cac51jsn7675f3102361",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }


response = requests.request("GET", url, headers=headers).json()

# print(response.text)

def helloworld(request):
    noofresullt=int(response['results'])
    mylist=[]
    for x in range(0,noofresullt):
        # print(response['response'][x]['country'])
        mylist.append(response['response'][x]['country'])
        context={'mylist':mylist}    
    if request.method=='POST':
        print('post method')
        selectedcountry=request.POST['selectedcountry']
        print(selectedcountry)

        for x in range(0,noofresullt):
            if selectedcountry==response['response'][x]['country']:
                print('found')
                print(response['response'][x]['cases'])
                new=response['response'][x]['cases']['new']
                active=response['response'][x]['cases']['active']
                critical=response['response'][x]['cases']['critical']
                recovered=response['response'][x]['cases']['recovered']
                total=response['response'][x]['cases']['total']
                if not total:
                    total=0
                    active=0
                    recovered=0
                
                elif not recovered:
                    recovered=0
                
                elif not active:
                    active=0
            
                deaths=int(total)-int(recovered)-int(active)

                context={'mylist':mylist,'selectedcountry':selectedcountry,'new':new,'active':active,'critical':critical,'recovered':recovered,'total':total,'deaths':deaths}    

                return render(request,'hello.html',context)

    # context={'mylist':mylist,'response':response}
    return render(request,'hello.html',context)