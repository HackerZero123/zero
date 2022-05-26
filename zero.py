print('''
    ┏━━━┓
┗┓┏┓┃
╋┃┃┃┣━━┓┏┓╋┏┳━━┳┓┏┓
╋┃┃┃┃┏┓┃┃┃╋┃┃┏┓┃┃┃┃
┏┛┗┛┃┗┛┃┃┗━┛┃┗┛┃┗┛┃
┗━━━┻━━┛┗━┓┏┻━━┻━━┛
╋╋╋╋╋╋╋╋┏━┛┃
╋╋╋╋╋╋╋╋┗━━┛
┏┓╋╋╋╋╋╋╋╋╋╋╋╋╋┏┓╋┏┓╋╋╋╋╋┏┓
┃┃╋╋╋╋╋╋╋╋╋╋╋╋╋┃┃╋┃┃╋╋╋╋╋┃┃
┃┃┏┳━┓┏━━┳┓┏┓┏┓┃┗━┛┣━━┳━━┫┃┏┳━━┳━┓
┃┗┛┫┏┓┫┏┓┃┗┛┗┛┃┃┏━┓┃┏┓┃┏━┫┗┛┫┃━┫┏┛
┃┏┓┫┃┃┃┗┛┣┓┏┓┏┛┃┃╋┃┃┏┓┃┗━┫┏┓┫┃━┫┃
┗┛┗┻┛┗┻━━┛┗┛┗┛╋┗┛╋┗┻┛┗┻━━┻┛┗┻━━┻┛
╋╋╋╋╋╋╋╋╋╋╋╋╋┏━━━┓┏┓
╋╋╋╋╋╋╋╋╋╋╋╋╋┃┏━┓┃┃┃
┏━━━┳━━┳━┳━━┓┗┛┏┛┃┃┃
┣━━┃┃┏┓┃┏┫┃━┫╋╋┃┏┛┗┛
┃┃━━┫┗┛┃┃┃┃━┫╋╋┏┓╋┏┓
┗━━━┻━━┻┛┗━━┛╋╋┗┛╋┗┛

------------------------------------------------
v1.0
ThousandShadow
2022.5.23
    
Usage:zero.py -t target_host -p port
-l --listen                      - listen on [host]:[port] for
                                   incoming connections
-e --execute=file_to_run         - execute the given file upon
                                   receiving a connection
-c --command                     - initialize a command shell
-u --upload=destination          - upon receiving connection upload
                                   file and write to [destination]

Examples:
zero.py -t 192.168.1.1 -p 5555 -l -c
zero.py -t 192.168.1.1 -p 5555 -l -u=c:\\target.exe
zero.py -t 192.168.1.1 -p 5555 -l -e=cat /etc/passwd
''')
