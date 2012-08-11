from django.http import HttpResponse

import matplotlib
matplotlib.use('Agg')
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter

import  matplotlib.pyplot as plt
import networkx as nx
from networkx.readwrite import json_graph

import json
import random
import datetime

def graph(request):
    #Create a figure and add subplot
    fig = Figure()
    ax = fig.add_subplot(111)
    x = []
    y = []
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now+=delta
        y.append(random.randint(0,1000))
    ax.plot_date(x,y,'-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas=FigureCanvas(fig)
    #Create a png file and return it
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response

def draw_network(request):
    G = nx.cycle_graph(24)
    pos = nx.spring_layout(G, iterations=200)
    nx.draw(G, pos, node_color=range(24), node_size=800, cmap=plt.cm.Blues)
    response =  HttpResponse(mimetype='image/png')
    plt.savefig(response, format='png')
    return response

def force(request):
    G = nx.barbell_graph(6, 3)
    # write json formatted data
    d = json_graph.node_link_data(G)  #node-link format to serialize
    # write json to client
#    json.dump(d, open('data/force.json', 'w'))
    return HttpResponse(json.dumps(d), mimetype='application/json')
