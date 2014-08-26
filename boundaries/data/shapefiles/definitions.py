from datetime import date

SHAPEFILES = {
    'Cities': {
        'file': 'cities/cities_id_added.shp',
        'name': 'cities',
        'authority': 'U.S. Census Bureau',
        'last_updated': date(2012, 3, 26),
        'slug': 'cities',
        'source_url': 'http://www.census.gov/cgi-bin/geo/shapefiles2010/main',
        'layer_mapping': {
            'name': 'NAME10',
            'identifier': 'GEOID10',
            'shape': 'MULTIPOLYGON',
            'collection': {
                'slug': 'COLLECTION'
            }
        }
    },

    'Counties': {
        'file': 'counties/counties_id_added.shp',
        'name': 'counties',
        'authority': 'U.S. Census Bureau',
        'last_updated': date(2012, 3, 26),
        'slug': 'counties',
        'source_url': 'http://www.census.gov/cgi-bin/geo/shapefiles2010/main',
        'layer_mapping': {
            'name': 'NAME10',
            'identifier': 'GEOID10',
            'shape': 'MULTIPOLYGON',
            'collection': {
                'slug': 'COLLECTION'
            }
        }
    },

    'School Districts': {
        'file': 'school_districts/school_districts_id_added.shp',
        'name': 'school_districts',
        'authority': 'Texas Education Agency',
        'last_updated': date(2013, 7, 1),
        'slug': 'school-districts',
        'source_url': 'http://www.tea.state.tx.us/'
                      'School_District_Locator/Data_Download/',
        'layer_mapping': {
            'name': 'NAME',
            'identifier': 'DISTRICT_C',
            'shape': 'MULTIPOLYGON',
            'collection': {
                'slug': 'COLLECTION'
            }
        }
    },
}
