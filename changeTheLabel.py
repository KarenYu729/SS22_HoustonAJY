import pandas as pd
import os

data_dir = 'C:/Users/karen/Downloads/annotation_1017/'

dirs = [os.listdir(data_dir)]
target_file = []
filename = []
for d in dirs[0]:
    file_dirs = os.path.join(data_dir, d)
    filename.append(d[:-4])
    target_file.append(file_dirs)

for i in range(len(target_file)):
    df = pd.read_csv(target_file[i])
    df['Species Desc'] = df['Species Desc'].apply(lambda x: 'fly' if ('Flying' in x)or('Wings Spread' in x)or('Flight' in x) else x)
    df.drop(index=(df.loc[(df['Species Desc']=='Great Blue Heron Egg')].index))
    df.drop(index=(df.loc[(df['Species Desc'] == 'Great Blue Heron Nest')].index))
    df.drop(index=(df.loc[(df['Species Desc']=='White Ibis Nest')].index))
