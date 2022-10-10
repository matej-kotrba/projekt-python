import phycicsModule as phy

EARTH_GRAVITY = 9.807 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62 #? měsíční gravitace

print("Světlo urazí vzdálenost 300000 km za " + str(phy.time_by_light_speed(300000)) + "s")

print("Zvuk urazí vzdálenost 3000 km za " + str(round(phy.time_by_sound_speed(3000))) + "s")

print("Hydrostaticky tlak ponorky v hloubce 10m ve vodě hustoty 1000kg/m3 na zemi je " +
      str(phy.hydrostaticky_tlak(10, 1000, EARTH_GRAVITY)) + " Pa")

print("Hmotnost ze země 1000kg je na měsíci " +
      str(round(phy.hmotnost_v_jine_gravitaci(1000, EARTH_GRAVITY, MOON_GRAVITY))) + " kg")