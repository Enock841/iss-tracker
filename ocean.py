def ocean_name(lat,lon):
    if lat > 66:
        return "Arctic Ocean"
    
    elif lat < -60:
        return "Southern Ocean"
    
    elif (20 > lon >= -70):
        return "Atlantic Ocean"
    
    elif (20 <= lon < 100):
        return "Indian Ocean"
    
    else:
        return "Pacific Ocean"
    
if __name__ == "__main__":
    print(ocean_name(10, 140))