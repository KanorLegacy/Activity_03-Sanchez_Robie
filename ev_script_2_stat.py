import math
class Class_EV():

    def desired(base,evv,ivv,opt,lvl,EV_Desired_Choice,mod):
        Total_EV_Desired = ((2*base[opt+1]+ivv[opt+1]+(evv[opt+1]/4))*lvl/100)
        return math.trunc((((EV_Desired_Choice/mod)-(Total_EV_Desired))*400/lvl)/4)*4