#!/usr/bin/python
import sys
import os

if (len(sys.argv) == 2):
    line = str(sys.argv[1])
    command = line[line.rfind('|')+3:]
    if command.startswith('exec'):
        command = 'sleep 0.05 && ' + command + ' &' #? Sleep so we can launch another instance of rofi and other applications seem to work too like xkill and blurlock.
    else:
        command = 'i3-msg ' + command
    os.system(command)
    os.system('pkill rofi') #? when executing some applications with this script rofi freezes so let's kill it. Not sure why it freezes though.
else:
    filename =  os.path.expanduser('~') + '/.i3/config' #? Change this if you have your config file located somewhere else.
    with open(filename) as file:
        description = ''
        for line in file:
            if line.startswith('# '):
                description = line[2:-1]
            elif line.startswith('bindsym '):
                line = line.replace(' --release', '').replace(' --no-startup-id', '')
                command_pos = line.find(' ', 8)
                if command_pos != -1:
                    command = line[command_pos:-1]
                    bindsym = line[8:command_pos]
                    if description == '' or description.startswith('bindsym '):
                        #? Remove continue if you want to show bindsyms without a description
                        continue
                        print (bindsym + ' | ' + command)
                    else:
                        print(description + ' | ' + bindsym + ' | ' + command)
            else:
                description = ''
