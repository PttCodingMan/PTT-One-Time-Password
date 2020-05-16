import subprocess
from os import walk

import config

def command(cmd, use_cmd=True):

    try:

        if isinstance(cmd, str):
            if use_cmd:
                cmd = 'cmd /c ' + cmd

            print(f'cmd [{cmd}]')

            cmd_buffer = None
            cmd_list = []
            mode = False
            cmd_temp = cmd.split(' ')
            for cmd_ in cmd_temp:
                mode_change = False
                if cmd_.startswith('\"') and not mode:
                    mode = True
                    mode_change = True
                    if cmd_buffer is None:
                        cmd_buffer = cmd_
                    else:
                        cmd_buffer = f'{cmd_buffer} {cmd_}'

                if cmd_.endswith('\"') and mode:
                    mode = False
                    mode_change = True
                    if cmd_buffer is None:
                        cmd_buffer = cmd_
                    else:
                        cmd_buffer = f'{cmd_buffer} {cmd_}'

                    cmd_list.append(cmd_buffer)
                    cmd_buffer = None

                if not mode_change:
                    cmd_list.append(cmd_)
        else:
            cmd_list = cmd

        print(cmd_list)
        r = subprocess.run(cmd_list, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        text = r.stdout.decode('cp950')
    except subprocess.CalledProcessError:
        return None
    except UnicodeDecodeError:
        return None
    return text


# command('RD /S /Q uPtt.build')
# command('RD /S /Q uPtt.dist')
#
print('開始編譯')
result = command(['cmd', '/c', 'pyinstaller', '--name=PttOneTimePassword', '--icon=../PTTOTP_small.png', '--windowed', '--onefile', './ptt_otp.py'])
print('編譯完成')
print(result)

# uptt_files = []
# for (dirpath, dirnames, filenames) in walk('uPtt.dist'):
#     uptt_files.extend(filenames)
#     break
#
# file_buffer = ''
# for file_name in uptt_files:
#     file_buffer += f'File \"uPtt.dist\\{file_name}\"\n'
# print(file_buffer)
#
# command(f'compile_nsis.bat uPtt.nsi', use_cmd=True)