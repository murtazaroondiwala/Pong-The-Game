import cx_Freeze

executables = [cx_Freeze.Executable('pong.py')]

cx_Freeze.setup(
	name = "pong",
	options = {"biuld_exe":{"packages":["pygame"]}},
	#include_files contains all the file like images so we have to mention in it
	executables = executables

	)