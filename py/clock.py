import sys, datetime, time
print "END: Ctrl + C"
while 1:
  now = datetime.datetime.today()
  sys.stdout.write("\r%s" % now)
  sys.stdout.flush()
  time.sleep(0.1)
