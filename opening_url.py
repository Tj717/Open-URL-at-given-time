import webbrowser
import datetime as DT
import time

# REMEMBER TO ADJUST BROWSER WINDOWS SIZES BEFORE EXECUTING

lck_url = "https://lolesports.com/live/lck/lck"
lpl_url = "https://lolesports.com/live/lpl/lpl"
lec_url = "https://lolesports.com/live/lec/LEC"
tcl_url = "https://lolesports.com/live/turkiye-sampiyonluk-ligi/riotgamesturkish"
cblol_url = "https://lolesports.com/live/cblol-brazil/cblol"
lcs_url = "https://lolesports.com/live/lcs/lcs"
ljl_url = "https://lolesports.com/live/ljl-japan/riotgamesjp"
lco_url = "https://lolesports.com/live/lco/lco"


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
        webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
    webbrowser.get('chrome').open(lck_url)


    time.sleep(1800)
    webbrowser.register('chrome',
        None,
        webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
    webbrowser.get('chrome').open(lpl_url)


    now = DT.datetime.now()
    target = DT.datetime.combine(DT.date.today(), DT.time(hour=2, minute=0, second=0))
    time.sleep((target-now).total_seconds())
    webbrowser.register('chrome',
        None,
        webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
    webbrowser.get('chrome').open(ljl_url)


    target = DT.datetime.combine(DT.date.today(), DT.time(hour=4, minute=0, second=0))
    time.sleep((target-now).total_seconds())
    webbrowser.register('chrome',
        None,
        webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
    webbrowser.get('chrome').open(tcl_url)


    # now = DT.datetime.now()
    # target = DT.datetime.combine(DT.date.today(), DT.time(hour=8, minute=0, second=0))
    # time.sleep((target-now).total_seconds())
    # webbrowser.register('chrome',
    #     None,
    #     webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
    # webbrowser.get('chrome').open(lec_url)


    now = DT.datetime.now()
    target = DT.datetime.combine(DT.date.today(), DT.time(hour=9, minute=0, second=0))
    time.sleep((target-now).total_seconds())
    webbrowser.register('chrome',
        None,
        webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
    webbrowser.get('chrome').open(cblol_url)


    now = DT.datetime.now()
    target = DT.datetime.combine(DT.date.today(), DT.time(hour=12, minute=30, second=0))
    time.sleep((target-now).total_seconds())
    webbrowser.register('chrome',
        None,
        webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
    webbrowser.get('chrome').open(lcs_url)

    break


# "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

# url = 'https://pythonexamples.org'
# webbrowser.register('chrome',
# 	None,
# 	webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
# webbrowser.get('chrome').open(url)

# time.sleep(2)

# webbrowser.register('chrome',
#     None,
#     webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
# webbrowser.get('chrome').open(lpl_url)
