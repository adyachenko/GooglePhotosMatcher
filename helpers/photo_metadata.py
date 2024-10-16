import piexif
from fractions import Fraction
from datetime import datetime
import logging

def to_deg(value, loc):
    if value < 0:
        loc_value = loc[0]
    elif value > 0:
        loc_value = loc[1]
    else:
        loc_value = ""
    abs_value = abs(value)
    deg = int(abs_value)
    t1 = (abs_value - deg) * 60
    min = int(t1)
    sec = round((t1 - min) * 60, 5)
    return deg, min, sec, loc_value

def change_to_rational(number):
    f = Fraction(str(number))
    return f.numerator, f.denominator

def set_exif(filepath: str, lat, lng, altitude, timestamp):
    try:
        exif_dict = piexif.load(filepath)

        # Update date and time information
        date_time = datetime.fromtimestamp(timestamp).strftime("%Y:%m:%d %H:%M:%S")
        exif_dict['0th'][piexif.ImageIFD.DateTime] = date_time
        exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = date_time
        exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = date_time

        # GPS information
        lat_deg = to_deg(lat, ["S", "N"])
        lng_deg = to_deg(lng, ["W", "E"])

        exiv_lat = (change_to_rational(lat_deg[0]), change_to_rational(lat_deg[1]), change_to_rational(lat_deg[2]))
        exiv_lng = (change_to_rational(lng_deg[0]), change_to_rational(lng_deg[1]), change_to_rational(lng_deg[2]))

        gps_ifd = {
            piexif.GPSIFD.GPSVersionID: (2, 0, 0, 0),
            piexif.GPSIFD.GPSLatitudeRef: lat_deg[3],
            piexif.GPSIFD.GPSLatitude: exiv_lat,
            piexif.GPSIFD.GPSLongitudeRef: lng_deg[3],
            piexif.GPSIFD.GPSLongitude: exiv_lng,
            piexif.GPSIFD.GPSAltitudeRef: 1,
            piexif.GPSIFD.GPSAltitude: change_to_rational(round(altitude, 2))
        }

        exif_dict['GPS'] = gps_ifd

        exif_bytes = piexif.dump(exif_dict)
        piexif.insert(exif_bytes, filepath)
        logging.debug(f"Set EXIF data for {filepath}")
    except Exception as e:
        logging.error(f"Error setting EXIF data for {filepath}: {e}")
