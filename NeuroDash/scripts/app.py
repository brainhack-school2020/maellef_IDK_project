import dash
import dash_html_components as html
import os

import bids_reader as br
import dash_utils as du

def show_bids_layout(input_value):
    if not os.path.lexists(input_value):
        return 'this path isn\'t correct. Please enter a real path.'
    
    return '{}'.format(br.read_layout_from_dataset(input_value))

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)#, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(children=[
    html.H1(children='BidsDash'),

    html.Div(children='''
        help visualise the content of a BIDS dataset
    ''')])

du.input_text(app, show_bids_layout, 
            my_id='my-id', my_div='my-div', 
            default_text='enter a absolute path')

if __name__ == '__main__':
    app.run_server(debug=True)