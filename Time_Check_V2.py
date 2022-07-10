#!/usr/bin/env python
import PySimpleGUI as sg
import csv

import os.path
# Show CSV data in Table
sg.theme('Dark Red')

file = 'time_table.csv'
time_file_exists = os.path.isfile(file)


with open(file, 'a+') as time_file:
    writer = csv.writer(time_file)
    if not time_file_exists:
        writer.writerow(['In','Out','Hours'])
    # with open(file,newline='' ) as in_file:
    #     with open(file, 'w',newline='') as out_file:
    #         for row in csv.reader(in_file):
    #             if row:
    #                 writer.writerow(row)

data = []
header_list = []


with open(file, "r") as time_file:
    reader = csv.reader(time_file)

    header_list = next(reader)
    

    try:
        data = list(reader)  # read everything else into a list of rows
        # if button == 'No':
        #     header_list = ['column' + str(x) for x in range(len(data[0]))]
    except:
        sg.popup_error('Error reading file')
            
sg.set_options(element_padding=(0, 0))

table_layout = [[sg.Table(values=data,
                        headings=header_list,
                        max_col_width=25,
                        auto_size_columns=True,
                        justification='right',
                        # alternating_row_color='lightblue',
                        num_rows=min(len(data), 20))]]


window = sg.Window('Table', table_layout, grab_anywhere=False)
event, values = window.read()
print(type(data))

window.close()

