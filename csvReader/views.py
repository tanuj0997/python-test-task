import csv,os,json,datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from collections import OrderedDict

@api_view()
def csvReader(request):
    try:
        requestData = dict(request.GET)
        ndays = None
        print(requestData['ndays'])
        if not requestData['ndays'] or requestData['ndays'][0] == '' or int(requestData['ndays'][0]) <= 0:
            ndays = datetime.datetime.today() - datetime.timedelta(days=7)
        else:
            ndays = datetime.datetime.today() - datetime.timedelta(days=int(requestData['ndays'][0]))

        csvFile = os.path.relpath('./data/data.csv')
        with open(csvFile,newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            csvData = []
            for row in reader:
                row = dict(OrderedDict(row))

                if ndays < datetime.datetime.strptime(row['date'],'%d-%m-%y'):
                    csvData.append(row)

        return Response({"data":csvData})
        
    except (Exception,TypeError,ValueError) as error:
        return Response({
            'error' : str(error),
        })
        