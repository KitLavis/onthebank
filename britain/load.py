from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import WatercourseLink

# Auto-generated `LayerMapping` dictionary for WatercourseLink model
watercourselink_mapping = {
    'name1': 'name1',
    'identifier': 'identifier',
    'startnode': 'startNode',
    'endnode': 'endNode',
    'form': 'form',
    'flow': 'flow',
    'fictitious': 'fictitious',
    'length': 'length',
    'name2': 'name2',
    'geom': 'MULTILINESTRING25D',
}

watercourselink_shp = Path(__file__).resolve().parent / 'osrivers' / 'data' / 'WatercourseLink.shp'

def run(verbose=True):
    lm = LayerMapping(WatercourseLink, watercourselink_shp, watercourselink_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
