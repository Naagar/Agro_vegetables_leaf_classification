import os
import random
from shutil import copyfile
import pandas as pd
import numpy as np
import csv


# file_name = 'shuffled_datafile.csv'
csv_file = open('dataset_all_images.csv','r')
csv_file.readline()

img_source_dir = './dataset/images'

train_size = 0.8 # split 80:20, train:validation

# def img_train_test_split(img_source_dir, df, train_size):
    
if not (isinstance(img_source_dir, str)):
    raise AttributeError('img_source_dir must be a string')
        
if not os.path.exists(img_source_dir):
    raise OSError('img_source_dir does not exist')
        
if not (isinstance(train_size, float)):
    raise AttributeError('train_size must be a float')
        
    # Set up empty folder structure if not exists
if not os.path.exists('dataset'):
        os.makedirs('dataset')
else:
    if not os.path.exists('dataset/train'):
        os.makedirs('dataset/train')
        # if not os.path.exists('data1/train/broken'):
        #     os.makedirs('data1/train/broken')
        # if not os.path.exists('data1/train/silkcut'):
        #     os.makedirs('data1/train/silkcut')
        # if not os.path.exists('data1/train/pure'):
        #     os.makedirs('data1/train/pure')
        # if not os.path.exists('data1/train/discolored'):
        #     os.makedirs('data1/train/discolored')

    if not os.path.exists('dataset/validation'):
        os.makedirs('dataset/validation')
        # if not os.path.exists('data1/validation/broken'):
        #     os.makedirs('data1/validation/broken')
        # if not os.path.exists('data1/validation/silkcut'):
        #     os.makedirs('data1/validation/silkcut')
        # if not os.path.exists('data1/validation/pure'):
        #     os.makedirs('data1/validation/pure')
        # if not os.path.exists('data1/validation/discolored'):
        #     os.makedirs('data1/validation/discolored')
            
    
train_subdir = os.path.join('dataset/train')
validation_subdir = os.path.join('dataset/validation')

        # Create subdirectories in train and validation folders
if not os.path.exists(train_subdir):
    os.makedirs(train_subdir)

if not os.path.exists(validation_subdir):
        os.makedirs(validation_subdir)

classes = ('Potato late blight', 'Tomato Curly Leaf', 'Tomato leaf miner')
train_counter = 0
validation_counter = 0
df_test= pd.DataFrame(columns=['name', 'class'])
df_train = pd.DataFrame(columns=['name', 'class'])
i_test = 0
i_train = 0
        # Randomly assign an image to train or validation folder
for filename, label in csv.reader(csv_file, delimiter=','):
    # print(filename)
    if filename.endswith(".jpg") or filename.endswith(".png"): 
        fileparts = filename.split('.')

        if random.uniform(0, 1) <= train_size:
            if label=='0':
                copyfile(os.path.join(img_source_dir, filename), os.path.join(train_subdir,'Potato late blight', filename ))
                train_counter += 1
                df_train.loc[i_train] = filename , label
                i_train += 1
            if label=='1':
                copyfile(os.path.join(img_source_dir, filename), os.path.join(train_subdir,'Tomato Curly Leaf', filename ))
                train_counter += 1
                df_train.loc[i_train] = filename , label
                i_train += 1
            if label=='2':
                copyfile(os.path.join(img_source_dir, filename), os.path.join(train_subdir,'Tomato leaf miner', filename ))
                train_counter += 1
                df_train.loc[i_train] = filename , label
                i_train += 1
        else:
            if label=='0':
                copyfile(os.path.join(img_source_dir, filename), os.path.join(validation_subdir,'Potato late blight', filename))
                validation_counter += 1
                df_test.loc[i_test] = filename , label
                i_test += 1
            if label=='1':
                copyfile(os.path.join(img_source_dir, filename), os.path.join(validation_subdir,'Tomato Curly Leaf', filename))
                validation_counter += 1
                df_test.loc[i_test] = filename , label
                i_test += 1
            if label=='2':
                copyfile(os.path.join(img_source_dir, filename), os.path.join(validation_subdir,'Tomato leaf miner', filename))
                validation_counter += 1
                df_test.loc[i_test] = filename , label
                i_test += 1
df_test.to_csv('test_data_file.csv') 
df_train.to_csv('train_data_file.csv')              
print('Copied ' + str(train_counter) + ' images to data/train/' )
print('Copied ' + str(validation_counter) + ' images to data/validation/')