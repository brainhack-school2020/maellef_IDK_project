
from bids import BIDSLayout
from bids.tests import get_test_data_path
import os


data_path = '/media/maelle/Backup Plus/dataset/cneuromod'
layout = BIDSLayout(data_path)
print(layout)