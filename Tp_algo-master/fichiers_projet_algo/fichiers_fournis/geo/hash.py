"""module de hashage_segments"""

from geo.segment import load_segments

def hashage_segments(filename, t):
    """Hash les segments : les clefs sont les numéros des carres exempl :
    point(1, 2) avec t = 0.5 sera mis dans le carré (2, 4)"""
    segments = load_segments(filename)
    table_hashage = {}
    for segment in segments:
        points = segment.endpoints
        for i in range(2):
            point = points[i]
            coordonnees_hash = point.coordinates[0] // t, point.coordinates[1] // t
            if (coordonnees_hash) in table_hashage:
                table_hashage[coordonnees_hash].append(point)
            else:
                print("nouvelle clef")
                print(point)
                print(coordonnees_hash)
                table_hashage[coordonnees_hash] = [point]
    return table_hashage


def ordered_segments():
  pass
