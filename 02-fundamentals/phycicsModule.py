def time_by_light_speed(length ,light_speed):
    '''
        return whole length divided by speed of light
        this will return you how fast would it take for light to travel this distance
    '''
    return str(length / light_speed) + "s"

def weight_at_moon(weight_at_earth, moon_gravitation):
    return weight_at_earth / 10 * moon_gravitation

def weight_at_earth_by_moon_weight(weight_at_earth, earth_gravitation):
    return weight_at_earth / 1.62 * earth_gravitation