import soco
import pprint
from soco import SoCo

if __name__ == '__main__':
    coordinators = set([])
    for zone in soco.discover():
        track = zone.get_current_track_info()
        print zone.player_name
        coordinators.add(zone.group.coordinator)
        pprint.pprint(track)
        print '============'

    print coordinators
    for c in coordinators:
        c.play_uri(
            'http://assets.phishtracks.com/system/tracks/song_files/000/030/006/original/9da84ab9cfbd2ff0dcfe66df8d6d98e281d314fc.mp3')
        

# TODO: resume the song that was playing before
