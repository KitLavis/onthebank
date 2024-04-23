from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import Venue

# Auto-generated `LayerMapping` dictionary for WatercourseLink model
venue_mapping = {
    'name1': 'name1',
    'identifier': 'identifier',
    'startnode': 'startNode',
    'endnode': 'endNode',
    'form': 'form',
    'flow': 'flow',
    'fictitious': 'fictitious',
    'length': 'length',
    'name2': 'name2',
    'county': 'County',
    'angclub': 'angClub',
    'bank': 'bank',
    'clubsite': 'clubSite',
    'geom': 'MULTILINESTRING25D',
}

venue_shp = Path(__file__).resolve().parent / 'qgis-data' / 'somerset' / 'ClevedonFWAC.shp'

def run(verbose=True):
    lm = LayerMapping(Venue, venue_shp, venue_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
