# tpsCounter
# who should use it: Anyone who has log files like below and want to see how much transactions per sec are coming in the logs

#Log Format of the gz log file:
xxxxxxxx yyyyyyyyy zzzzzzzz tttttttt iiiiiiiiii

#What it does
From each log line it takes out the time ttttttt at a given index "timeIndex" and and strips the millisec part based on "timeSplitter"
It also takes out another string, say instanceName iiiiiiiiii, at instanceNameIndex in the log line.

Then using the unique key as "ttttttt|iiiiiiiiii" it counts the occurences which makes up the logEntries per timeString "ttttttt" for instanceName "iiiiiiiiii"
# Usage
$(which python) tpsCounter.py <gz file name>

#Sample output:
TPS of iiiiiiiiii :
Max      : iiiiiiiiii[ 78849 ] =  (u'17:53:25|iiiiiiiiii', 15)
98 %ile  : iiiiiiiiii[ 77271 ] =  (u'05:50:23|iiiiiiiiii', 7)
95 %ile  : iiiiiiiiii[ 74905 ] =  (u'20:59:54|iiiiiiiiii', 6)
90 %ile  : iiiiiiiiii[ 70963 ] =  (u'15:03:31|iiiiiiiiii', 5)

where 15 occurences of iiiiiiiiii happened at 17:53:25th sec , the max. There were total 78849+1 unique occurences of "ttttttt|iiiiiiiiii" and 98, 95 and 90th percentile happened at 05:50:23, 20:59:54 and 15:03:31th sec of the day

#Spped at which script runs is approx 30000 lines of log read/sec
