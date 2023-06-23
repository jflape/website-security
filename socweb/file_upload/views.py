from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from datetime import datetime
import os

def upload_file(request):
    df = []
    if request.method == 'POST':
        file = request.FILES['file']
        directory = './output/'

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
        
        with open(file_path, 'r') as rm_dup:
            dup_outs = rm_dup.readlines()
            
        unique_lines = []
        num_duplicate_lines = 0
        
        for dup_out in dup_outs:
            dup_out = dup_out.strip()
            
            if dup_out not in unique_lines:
                unique_lines.append(dup_out)
            else:
                num_duplicate_lines += 1
        
        num_lines_inserted = len(unique_lines) - len(dup_outs)
                
        with open(file_path,'w') as no_dups:
            no_dups.write('\n'.join(unique_lines) + '\n')
        
        with open(file_path, 'r') as showdata:
            alldata = showdata.read()
        
        contents = {
            'alldata' : alldata,
            'num_lines_inserted' : num_lines_inserted,
            'num_duplicate_lines' : num_duplicate_lines
        }    

        # return render(request, 'file_upload/result.html', {'display': contents})
        return render(request, 'file_upload/result.html', contents)
    
    return render(request, 'file_upload/upload.html')

def output_data(request):
        directory = './output/'
        file_name = "output.txt"
    #   file_path = directory + file_name
        file_path = os.path.join(directory, file_name)
        if not os.path.exists(directory):
            os.makedirs(directory)   
      
        with open(file_path, 'r') as showdata:
            content = showdata.read()      
        
        return HttpResponse(content, content_type='text/plain')
