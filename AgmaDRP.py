import PySimpleGUI as sg
import os
import sys
from pypresence import Presence
import time
import sys


def main():
    sg.theme('DarkAmber')
    layout = [
        [sg.Combo(values=['EU | DodgeBall', 'EU | Infection (Beta)', 'EU | Battle Royale', 'EU | Solo Selffeed Royale', 'EU | Crazy', 'EU | PopSplit Paradise', 'EU | Instant', 'EU | Supersonic/Minions', 'EU | SlowSplit VirusFarm', 'EU | Gigantic', 'EU | Gig 2 [128x]', 'EU | Gig 3 [No Pows]', 'EU | Gig 4 [XP Farm Portal]', 'EU | MegaSplit', 'EU | Selffeed On Redbull', 'EU | Selffeed EU', 'NA | Dodgeball', 'NA | Infection (Beta)', 'NA | Battle Royale', 'NA | Solo Selffeed Royale', 'NA | SOLO Agf.io', 'NA | Crazy', 'NA | Splitrun Paradise', 'NA | X-Insta', 'NA | XY-Insta', 'NA | Supersonic/Minions', 'NA | FastSplit VirusFarm', 'NA | Giant', 'NA | Giant 2 [128x]', 'NA | Giant 3 [No Pows]', 'NA | Selffeed on Redbull', 'NA | Selffeed', 'AS | Battle Royale', 'AS | Crazy Asia', 'AS | Giga', 'AS | Giga 2 [No Pows]', 'AS | MegaSplit', 'AS | Selffeed', 'AS | Instant [New]'], key='select', size=(100, 100))],
        [sg.Button('Close')],
        [sg.Button('Apply and restart')],
    ]
    window = sg.Window('Agma.io DRP', layout, size=(200, 200), finalize=True, enable_close_attempted_event=True)
    window.load_from_disk('temp.pickle')

    event, values = window.read()

    Server = values['select']

    if ''.join(list(Server)[0:2]) == "EU":
            region = "Europe"
    elif ''.join(list(Server)[0:2]) == "NA":
            region = "North America"
    elif ''.join(list(Server)[0:2]) == "AS":
            region = "Asia"

    rpc = Presence("")

    rpc.connect()
    rpc.update(
            large_text = "Agma.io",
            large_image ="agm",
            details = f"Region - {region}",
            state=f"Server - {Server[3:]}",
            party_size=[1, 250],
            buttons=[{"label": "Play Now!", "url": "https://agma.io/"}],
            start=int(time.time()),
        )

    while True:
        
        event, values = window.read()
    
        if event in (sg.WINDOW_CLOSE_ATTEMPTED_EVENT, 'Close'):
            break
        if event in (sg.WINDOW_CLOSE_ATTEMPTED_EVENT, 'Apply and restart'):
            window.save_to_disk('temp.pickle')
            os.execl(sys.executable, sys.executable, *sys.argv)

        time.sleep(15)
        window.close()
    
    


if __name__ == '__main__':
    main()
