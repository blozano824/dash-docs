import dash_core_components as dcc
import dash_html_components as html

from tutorial import styles


def ComponentBlock(example_string, **kwargs):
    scope = {}
    converted_string = example_string.replace(
        'dcc.', 'component = dcc.').replace(
            'daq.', 'component = daq.')
    try:
        exec(converted_string, scope)
    except Exception as e:
        print('\nError running\n{}\n{}'.format(
            converted_string,
            ('======================================' +
             '======================================')
        ))

        raise e
    return html.Div([
        dcc.SyntaxHighlighter(
            example_string,
            language='python',
            customStyle=styles.code_container
        ),
        html.Div(
            scope['component'],
            className='example-container',
            style=(({'overflow-x': 'initial'}) if (
                'DatePicker' in example_string or
                'Dropdown' in example_string
            ) else ({
                'overflow-x': 'initial',
                'padding-bottom': '25px'
            }) if 'Slider' in example_string else ({
                'float': 'center'
            }) if 'ColorPicker' in example_string else ({
                'padding-left': '30px'
            }) if 'Tank' in example_string else ({
                'height': '240px'
            }) if 'Thermometer' in example_string else {})
        )
    ])

