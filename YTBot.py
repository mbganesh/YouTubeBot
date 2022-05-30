import webbrowser, time


url = input("Enter url: ")
views = input("Enter amount of views: ")
duration = input("Enter duration before opening another video (in seconds): ")

for i in range(int(views)):
    webbrowser.open_new(url)
    time.sleep(int(duration))