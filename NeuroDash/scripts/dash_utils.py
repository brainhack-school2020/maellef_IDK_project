import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

def input_text(app, output_function, my_id='my-id', my_div='my-div', default_text='type your entry'):
    app.layout = html.Div([
        dcc.Input(id=my_id, value=default_text, type='text'),
        html.Div(id=my_div)
    ])

    @app.callback(
        Output(component_id=my_div, component_property='children'),
        [Input(component_id=my_id, component_property='value')]
    )
    def update_output_div(input_value):
        return output_function(input_value)

#dcc.Dropdown, dcc.RadioItems, dcc.Checklist
def multiple_choices(labels, values, choice_type = dcc.Dropdown, default_value=None, multi=False) :
    ''' create a dropdown element, with the given labels and values, that can be add in a layout.
    A default value can be given so the dropdown element will show by default this value.
    if multi is True, then multiple choices can be selected in one input.
    --------------------------
    input : 2 lists, labels and values, where each row in labels correponds 
        to the same row in values (labels must contain only immutable items).
    output : 1 dropdown element
    '''
    datalist = [ {'label': label, 'value': value} for label, value in zip(labels, values) ]
    return choice_type(
        options=datalist,
        value=default_value,
        #multi=multi
    ),

def text_input(default=None):
    return dcc.Input(value=default, type='text'),

def slider_input(min_input, max_input, legends_input = None, default=None)
    ''' create a slider element.'''
    if legends_input is not None : 
        
    else : 
        legends = {i:str(i) for i in range(min_input, max_input+1)}

    return dcc.Slider(
        min=min_input,
        max=max_input,
        marks=legends,
        value=default,
    ),