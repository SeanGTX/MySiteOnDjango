@ECHO OFF
Echo  #**************************************#
Echo  *            VK Parser v0.1            *
Echo  *           Select the action          *
Echo  *--------------------------------------*
Echo  * Parse new public and start server - 1*
Echo  * Start server - 2                     *
Echo  * Delete public - 3                    *
Echo  #**************************************#
Echo.
Set /p choice="Your choice: "
if "%choice%"=="1" (
	python search.py
	start chrome "http://37.145.21.20"
	python manage.py runserver 0.0.0.0:8000
)
if "%choice%"=="2" (
	start chrome "http://37.145.21.20"
	python manage.py runserver 0.0.0.0:8000
)
if "%choice%"=="3" (python DeletePublic.py)
pause