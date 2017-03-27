import time
import webbrowser

totalBreaks = 3
print("The program started at " + time.ctime())
for i in range(totalBreaks):
  time.sleep(2 * 60 * 60)
  webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
