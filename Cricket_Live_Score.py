#IPL --Cricket Live Score Using Python

import sports                #pip install sports.py
from pynotifier import Notification            #pip install py-notifier

Match_Info = sports.get_sport('CRICKET')

Notification(title = "LIVE SCORE", description = str(Match_Info), duration = 60).send()
