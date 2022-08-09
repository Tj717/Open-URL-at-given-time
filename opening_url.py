import webbrowser
import datetime as DT
import time


url = "https://lolesports.com"


browser1_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe";

while True:
    now = DT.datetime.now()
    # Today + timedelta days
    target = DT.datetime.combine(DT.date.today() + DT.timedelta(days=1),
    # target = DT.datetime.combine(DT.date.today(),
    DT.time(hour=1, minute=0, second=0))

    print(now)
    print(target)
    if target < now:
        target += DT.timedelta(days=1)
    time.sleep((target-now).total_seconds())

    webbrowser.register('chrome',
        None,
        webbrowser.BackgroundBrowser(browser1_location))
    webbrowser.get('chrome').open(url
    
    break
