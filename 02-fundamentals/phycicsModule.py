SPEED_OF_LIGHT = 300000  #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu

def time_by_light_speed(length):
    '''
        accepts length in km
        return whole length divided by speed of light
        this will return you how fast would it take for light to travel this distance
    '''
    return length / SPEED_OF_LIGHT


def time_by_sound_speed(length):
    '''
        accepts length in km
        return whole length divided by speed of sound
        this will return you how fast would it take for sound to travel this distance
    '''
    return (length * 1000) / SPEED_OF_SOUND


def hydrostaticky_tlak(hloubka, hustota_kapaliny, gravitacni_konstanta):
    '''
        Vypocte hydrostaticky tlak
    '''
    return hloubka * hustota_kapaliny * gravitacni_konstanta


def hmotnost_v_jine_gravitaci(hmotnost, grav_konstanta_puvod, grav_konstanta_cil):
    '''
        Hmotnost = hmotnost s puvodni gravitacni konstantou
        grav_konstanta_puvod = puvodni gravitacni konstanta
        grav_konstanta_cil = nova gravitacni konstanta
        Vrati hmotnost pro novou gravitacni konstantu odvozenou ze stare
    '''
    return hmotnost * (grav_konstanta_cil / grav_konstanta_puvod)