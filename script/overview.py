
import os
import pandas
import plotly
import yaml
import datetime

def loadYAML(path):

    paper = open(path, 'r')
    content = yaml.load(paper, yaml.SafeLoader)
    paper.close()
    return(content)

def loadCSV(path):

    content = pandas.read_csv(path)
    return(content)

def writeContent(content=None, path=None):

    folder = os.path.dirname(path)
    os.makedirs(folder, exist_ok=True)
    with open(path, 'a') as paper: print(content, file=paper)
    return

content = loadYAML(path='overview.yaml')

writeContent(content=datetime.datetime.today(), path=content['log'])
for i in content['file']:

    t = loadCSV(os.path.join(content['folder'], i))
    writeContent(content=i, path=content['log'])
    writeContent(content=t.shape, path=content['log'])
    writeContent(content=t.keys(), path=content['log'])
    writeContent(content='\n', path=content['log'])
    continue

sheet = {}
pass

name = 'train_x_alert_date.csv'
sheet[name] = loadCSV(os.path.join(content['folder'], name))
len(sheet[name])
sheet[name]['alert_key'].nunique()
pass

name = 'public_x_alert_date.csv'
sheet[name] = loadCSV(os.path.join(content['folder'], name))
len(sheet[name])
sheet[name]['alert_key'].nunique()
pass

intersection = set.intersection(
    set(sheet['train_x_alert_date.csv']['alert_key']),
    set(sheet['public_x_alert_date.csv']['alert_key'])
)
intersection
pass

name = 'public_train_x_custinfo_full_hashed.csv'
sheet[name] = loadCSV(os.path.join(content['folder'], name))
len(sheet[name])
sheet[name]['alert_key'].nunique()
pass

name = 'train_y_answer.csv'
sheet[name] = loadCSV(os.path.join(content['folder'], name))
len(sheet[name])
sheet[name]['alert_key'].nunique()
pass

name = 'submission.csv'
sheet[name] = loadCSV(os.path.join(content['folder'], name))
len(sheet[name])
sheet[name]['alert_key'].nunique()
pass



