import math


class Class_Status():

    def hpReturn(base, ivv, evv, lvl):
        return math.trunc((((2 * base[1] + ivv[1] + (evv[2] / 4)) * lvl) / 100) + lvl + 10)

    def attackReturn(base, ivv, evv, lvl, atk_nature):
        return math.trunc((((((2 * base[2] + ivv[2] + (evv[2] / 4)) * lvl) / 100) + 5) * atk_nature))

    def defenseReturn(base, ivv, evv, lvl, def_nature):
        return math.trunc((((((2 * base[3] + ivv[3] + (evv[3] / 4)) * lvl) / 100) + 5) * def_nature))

    def spattackReturn(base, ivv, evv, lvl, spec_atk_nature):
        return math.trunc((((((2 * base[4] + ivv[4] + (evv[4] / 4)) * lvl) / 100) + 5) * spec_atk_nature))

    def spdefenseReturn(base, ivv, evv, lvl, spec_def_nature):
        return math.trunc((((((2 * base[5] + ivv[5] + (evv[5] / 4)) * lvl) / 100) + 5) * spec_def_nature))

    def speedReturn(base, ivv, evv, lvl, speed_nature):
        return math.trunc((((((2 * base[6] + ivv[6] + (evv[6] / 4)) * lvl) / 100) + 5) * speed_nature))