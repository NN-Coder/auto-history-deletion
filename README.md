Automate It to Run Daily

Windows (Task Scheduler)
	1.	Open Task Scheduler (Win + R → type taskschd.msc).
	2.	Click Create Basic Task → Name it “Clear Chrome History”.
	3.	Set Trigger → “Daily” at a specific time.
	4.	Set Action → “Start a Program”.
	5.	Browse for win.py and add the script’s full path as an argument.
	6.	Click Finish.

Mac/Linux (Cron Job)
	1.	Open Terminal.
	2.	Type crontab -e and add this line:
 "0 0 * * * /usr/bin/python3 /path/to/macOS.py"

 One-Time Use

 Windows
 python "C:\path\to\script.py"
 
 Mac/Linux
 python3 /path/to/script.py

(Replace path with actual)
 
 

 
