# import os

# while True:
# 	_cmd = input('cmd> ')
# 	cmd = _cmd.split(' ')[0]
# 	args = _cmd.split(' ')[1] if len(_cmd.split(' ')) > 2 else None
# 	if cmd == 'cd':
# 		os.chdir(args)
# 	if cmd == 'dir':
# 		os.

import subprocess
while True:
	cmd = input('> ')
	subprocess.call(cmd, shell=True)