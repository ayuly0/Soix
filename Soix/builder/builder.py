import os

if not os.path.exists('../venv/'):
	os.system('python -m venv ../venv')
	os.system(r'cmd /c "..\venv\Scripts\activate.bat && python -m pip install -r requirements.txt"')

cmd_build = r'cmd /k "..\venv\Scripts\activate.bat && pyinstaller --noconfirm --onefile --distpath=./dist/Soix-C2 --paths=../venv/Lib/site-packages --upx-dir=./upx --windowed  --icon=NONE --name "Soix" ../main.py"'

os.system(cmd_build)
