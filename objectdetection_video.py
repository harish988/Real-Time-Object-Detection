#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 12:01:40 2017

@author: www.github.com/GustavZ
"""
from rod.model import ObjectDetectionModel
from rod.config import Config


def main():
    model_type = 'od'
    input_type = 'video'
    config = Config(model_type)
    model = ObjectDetectionModel(config).prepare_model(input_type)
    model.run()

if __name__ == '__main__':
    main()
