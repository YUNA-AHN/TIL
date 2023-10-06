from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt

# 그래프 그리기 위한 사전 준비
from io import  BytesIO
import base64
plt.switch_backend('Agg')

# Create your views here.
def index(request):
    return render(request, 'base.html')

# 파일 경로 설정
csv_path = 'weathers/data/austin_weather.csv'
def problem1(request):
    df = pd.read_csv(csv_path)
    context  = {
        'df': df
    }
    return render(request, 'weathers/problem1.html', context)

def problem2(request):
    df = pd.read_csv(csv_path)
    df['Date'] = pd.to_datetime(df['Date'])
    
    plt.clf()
    
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature (Fahrenheit)')
    plt.plot(df['Date'], df['TempHighF'], label = 'High Temperature')
    plt.plot(df['Date'], df['TempAvgF'], label = 'Average Temperature')
    plt.plot(df['Date'], df['TempLowF'], label = 'Low Temperature')
    plt.grid()
    plt.legend(loc = 'lower center')
    
    buffer = BytesIO()
    plt.savefig(buffer, format = 'png')
    image_base64 =  base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()
    
    context  = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'weathers/problem2.html', context)

def problem3(request):
    df = pd.read_csv(csv_path)
    df['month'] = df['Date'].apply(lambda x: x[:-3])
    
    plt.clf()
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature (Fahrenheit)')

    plt.plot(df.groupby('month')[['TempHighF','TempAvgF','TempLowF']].mean())
    plt.xticks(['2014-01','2014-07','2015-01','2015-07','2016-01', '2016-07','2017-01','2017-06'])
    plt.grid()
    plt.legend(('High Temperature','Average Temperature','Low Temperature'), loc = 'lower right')
    
    buffer = BytesIO()
    plt.savefig(buffer, format = 'png')
    image_base64 =  base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()
    
    context  = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'weathers/problem3.html', context)

def problem4(request):
    df = pd.read_csv(csv_path)
    
    weather = dict()
    for weathers in df['Events']:
        events = weathers.replace(' ', '').split(',')
        if events == ['']:
            weather.setdefault('No Events', 0)
            weather['No Events'] += 1
        else:
            for event in events:
                weather.setdefault(event, 0)
                weather[event] += 1
                
    w_list = sorted(weather.items(), key = lambda x:x[1], reverse=True)
    key_list=[]
    v_list=[]
    for key, value in w_list:
        key_list.append(key)
        v_list.append((value))
        
    plt.clf()
    plt.bar(key_list, v_list)
    plt.grid()
    plt.title('Event Counts')
    plt.xlabel('Events')
    plt.ylabel('Count')
    
    buffer = BytesIO()
    plt.savefig(buffer, format = 'png')
    image_base64 =  base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()
    
    context  = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'weathers/problem4.html', context)