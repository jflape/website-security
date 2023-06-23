from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from datetime import datetime
import os

def upload_file(request):
    df = []
    if request.method == 'POST':
        file = request.FILES['file']
        directory = '../output/'

        df.append(pd.read_excel(file, usecols=['IP Address']))
        df_data = pd.concat(df, axis=0)
       
        df_txtoutput = df_data.to_string(index=False, header=False).strip()
        #current_date = datetime.now().strftime("%Y-%m-%d")
        #file_name = f"output_{current_date}.txt"
        file_name = "output.txt"
        #file_path = directory + file_name
        
        file_path = os.path.join(directory, file_name)
        if not os.path.exists(directory):
            os.makedirs(directory)
            
        with open(file_path, 'a') as f:
            f.write(df_txtoutput + '\n')
        
        with open(file_path, 'r') as showdata:
            contents = showdata.read()

        return render(request, 'file_upload/result.html', {'display': contents})
    return render(request, 'file_upload/upload.html')

def output_data(request):
        directory = '../output/'
        file_name = "output.txt"
    #   file_path = directory + file_name
        file_path = os.path.join(directory, file_name)
        if not os.path.exists(directory):
            os.makedirs(directory)   
      
        with open(file_path, 'r') as showdata:
            content = showdata.read()      
        
        return HttpResponse(content, content_type='text/plain')
