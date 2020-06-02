
from bids import BIDSLayout
from bids.tests import get_test_data_path


def read_layout_from_dataset(data_path):
    try : 
        layout = BIDSLayout(data_path)
    except ValueError as error : 
        return error 

    return layout

if __name__ == '__main__':
    data_path = '/home/maelle/Database'#/ds000224'
    result = read_layout_from_dataset(data_path)
    print(result)