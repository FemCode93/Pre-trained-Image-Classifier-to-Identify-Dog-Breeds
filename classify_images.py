#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
import os.path
from classifier import classifier 

def classify_images(images_dir, results_dic, model):

    # classifier function
    for key,value in results_dic.items():
        model_label = os.path.join(images_dir + '/' + key)
        model_label = classifier(images_dir+key, model)
        model_label = model_label.lower().strip()
              
       # defines truth as pet image label
        truth = results_dic[key][0]
        
        if truth in model_label:
            results_dic[[key][0]].extend([model_label, 1])
        else:
            results_dic[[key][0]].extend([model_label, 0])
