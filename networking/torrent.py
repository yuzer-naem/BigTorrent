from networking.tracker import Tracker


class Torrent:
    def __init__(self, tracker):
        self.tracker: Tracker = tracker
