from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from datetime import datetime

def upload_file(request):
    df = []
    if request.method == 'POST':
        file = request.FILES['file']
        directory = '/usr/local/src/gitrepos/python-web/security/socweb/output/'
        df.append(pd.read_excel(file, usecols=['IP Address']))
        df_data = pd.concat(df, axis=0)
        # df_data.to_excel('trickbot.xlsx', index=False, header=False)
        # df_data.to_csv('trickbot.txt', index=False, header=False)
        # df_data.to_html('trickbot.html', index=False, header=False)
       
        df_txtoutput = df_data.to_string(index=False, header=False).strip()
        #current_date = datetime.now().strftime("%Y-%m-%d")
        #file_name = f"output_{current_date}.txt"
        file_name = "output.txt"
        file_path = directory + file_name
        with open(file_path, 'a') as f:
            f.write(df_txtoutput + '\n')
        
        with open(file_path, 'r') as showdata:
            contents = showdata.read()
        # df = pd.read_excel(file)
        # columns = df.columns
        return render(request, 'file_upload/result.html', {'display': contents})
    return render(request, 'file_upload/upload.html')

def output_data(request):
      directory = '/usr/local/src/gitrepos/python-web/security/socweb/output/'
      file_name = "output.txt"
      file_path = directory + file_name
      
      with open(file_path, 'r') as showdata:
         content = showdata.read()      
        
      return HttpResponse(content, content_type='text/plain')
