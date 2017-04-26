#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
qm9.py:

Usage:

"""

import torch.utils.data as data
import numpy as np
import argparse

import os, sys

reader_folder = os.path.realpath( os.path.abspath( '../GraphReader' ))
if reader_folder not in sys.path:
    sys.path.insert( 0, reader_folder)

from GraphReader.graph_reader import xyz_graph_reader


class Qm9(data.Dataset):

    # Constructor
    def __init__(self, root_path, ids, transform=None, target_transform=None):
        self.root = root_path
        self.ids = ids

    def __getitem__(self, index):
        g, target = xyz_graph_reader(os.path.join(self.root,self.ids[index]))
        return g, target

    def __len__( self ):
        return len(self.ids)

if __name__ == '__main__':

    # Parse optios for downloading
    parser = argparse.ArgumentParser(description='QM9 Object.')
    # Optional argument
    parser.add_argument('--root', nargs=1, help='Specify the data directory.', default=['../data/qm9/dsgdb9nsd/'])

    args = parser.parse_args()
    root = args.root[0]

    files = [f for f in os.listdir(root) if os.path.isfile(os.path.join(root, f))]

    idx = np.random.permutation(len(files))
    idx = idx.tolist()

    valid_ids = [files[i] for i in idx[0:10000]]
    test_ids  = [files[i] for i in idx[10000:20000]]
    train_ids = [files[i] for i in idx[20000:]]

    data_train = Qm9(root, train_ids)
    data_valid = Qm9(root, valid_ids)
    data_test = Qm9(root, test_ids)