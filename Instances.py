import numpy as np
from VehicleModel4Wh import Vehicle

# --- Helper Classes for Vehicle Inputs ---
class RenaultVehicle1:
    def __init__(self):
        self.slr = 230
        self.dlr = 245
        self.initial_camber = 0.5
        self.toe_in = 0.3
        self.tw = 1080
        self.wb = 1680
        self.wr_front = 1.1
        self.wr_rear = 2.8
        self.tire_stiffness_front = 200
        self.tire_stiffness_rear = 210
        self.pinion = 7
        self.tirep = 32
        self.dila = -40
        self.linkage_effort = 1.5
        self.linkage_kpm = 7.8

class SuzukiVehicle2:
    def __init__(self):
        self.slr = 240
        self.dlr = 255
        self.initial_camber = 0.2
        self.toe_in = 0.2
        self.tw = 1225
        self.wb = 2360
        self.wr_front = 1.3
        self.wr_rear = 2.5
        self.tire_stiffness_front = 250
        self.tire_stiffness_rear = 240
        self.pinion = 6
        self.tirep = 34
        self.dila = -42
        self.linkage_effort = 1.6
        self.linkage_kpm = 8.2

class Michelin12570R13:
    def __init__(self):
        self.tiredata = np.array([
            0.655, 0.11, 18.0,
            0.42, 0.26, 6.0,
            0.59, 0.32
        ])
        self.CF_Loads = np.array([0, 140, 190, 240, 480])
        self.CF_Stiffnessrad = np.array([
            0, 20000, 22800, 24500,
            24500 + 240*(24500-22800)/50
        ])
        self.pneumatictrail = np.array([
            0, 0.012, 0.018, 0.022,
            0.022 + 240*(0.022-0.018)/50
        ])

class Bridgestone14580R12:
    def __init__(self):
        self.tiredata = np.array([
            0.525, 0.115, 17.5,
            0.40, 0.255, 5.8,
            0.58, 0.31
        ])
        self.CF_Loads = np.array([0, 160, 210, 260, 500])
        self.CF_Stiffnessrad = np.array([
            0, 20500, 23200, 24800,
            24800 + 260*(24800-23200)/50
        ])
        self.pneumatictrail = np.array([
            0, 0.011, 0.017, 0.021,
            0.021 + 260*(0.021-0.017)/50
        ])

# --- Cache common objects so they are created only once ---
_common_objs = None

def get_common_objs():
    global _common_objs
    if _common_objs is None:
        _common_objs = {
            'objRenaultVehicle1': RenaultVehicle1(),
            'objSuzukiVehicle2': SuzukiVehicle2(),
            'objMichelin12570R13': Michelin12570R13(),
            'objBridgestone14580R12': Bridgestone14580R12()
        }
    return _common_objs

# --- Lazy Vehicle Instance Creation Functions ---
def get_Vehicle1_BaseModel():
    objs = get_common_objs()
    return Vehicle(
        np.array([1000, 400, 1200]),
        np.array([950, 380, 1250]),
        np.array([1100, 30, 1300]),
        np.array([980, 560, 940]),
        np.array([970, 490, 900]),
        r_La = np.array([1300, 500, 950]),
        r_Lb = np.array([1300, 250, 950]),
        r_Ua = np.array([1230, 390, 1270]),
        r_Ub = np.array([1230, 480, 1270]),
        GVW = 450,
        b = 750,
        CG_height = 320,
        slr = objs['objRenaultVehicle1'].slr,
        dlr = objs['objRenaultVehicle1'].dlr,
        initial_camber = objs['objRenaultVehicle1'].initial_camber,
        toe_in = objs['objRenaultVehicle1'].toe_in,
        tw = objs['objRenaultVehicle1'].tw,
        wb = objs['objRenaultVehicle1'].wb,
        wheel_rate_f = objs['objRenaultVehicle1'].wr_front,
        wheel_rate_r = objs['objRenaultVehicle1'].wr_rear,
        tire_stiffness_f = objs['objRenaultVehicle1'].tire_stiffness_front,
        tire_stiffness_r = objs['objRenaultVehicle1'].tire_stiffness_rear,
        pinion = objs['objRenaultVehicle1'].pinion,
        tirep = objs['objRenaultVehicle1'].tirep,
        dila = objs['objRenaultVehicle1'].dila,
        linkage_effort = objs['objRenaultVehicle1'].linkage_effort,
        linkage_kpm = objs['objRenaultVehicle1'].linkage_kpm,
        tiredata = objs['objMichelin12570R13'].tiredata,
        CF_Loads = objs['objMichelin12570R13'].CF_Loads,
        CF_Stiffnessrad = objs['objMichelin12570R13'].CF_Stiffnessrad,
        CF_pneumatictrail = objs['objMichelin12570R13'].pneumatictrail
    )

def get_Vehicle2_BaseModel():
    objs = get_common_objs()
    return Vehicle(
        np.array([1020, 410, 1250]),
        np.array([960, 390, 1280]),
        np.array([1150, 40, 1350]),
        np.array([990, 570, 950]),
        np.array([980, 500, 910]),
        r_La = np.array([1350, 510, 970]),
        r_Lb = np.array([1350, 270, 970]),
        r_Ua = np.array([1250, 400, 1300]),
        r_Ub = np.array([1250, 490, 1300]),
        GVW = 650,
        b = 800,
        CG_height = 340,
        slr = objs['objSuzukiVehicle2'].slr,
        dlr = objs['objSuzukiVehicle2'].dlr,
        initial_camber = objs['objSuzukiVehicle2'].initial_camber,
        toe_in = objs['objSuzukiVehicle2'].toe_in,
        tw = objs['objSuzukiVehicle2'].tw,
        wb = objs['objSuzukiVehicle2'].wb,
        wheel_rate_f = objs['objSuzukiVehicle2'].wr_front,
        wheel_rate_r = objs['objSuzukiVehicle2'].wr_rear,
        tire_stiffness_f = objs['objSuzukiVehicle2'].tire_stiffness_front,
        tire_stiffness_r = objs['objSuzukiVehicle2'].tire_stiffness_rear,
        pinion = objs['objSuzukiVehicle2'].pinion,
        tirep = objs['objSuzukiVehicle2'].tirep,
        dila = objs['objSuzukiVehicle2'].dila,
        linkage_effort = objs['objSuzukiVehicle2'].linkage_effort,
        linkage_kpm = objs['objSuzukiVehicle2'].linkage_kpm,
        tiredata = objs['objBridgestone14580R12'].tiredata,
        CF_Loads = objs['objBridgestone14580R12'].CF_Loads,
        CF_Stiffnessrad = objs['objBridgestone14580R12'].CF_Stiffnessrad,
        CF_pneumatictrail = objs['objBridgestone14580R12'].pneumatictrail
    )


# --- Lazy Loading via Module __getattr__ ---
_lazy_instances = {
    "Vehicle1": get_Vehicle1_BaseModel,
    "Vehicle2": get_Vehicle2_BaseModel,
}
def __getattr__(name):
    if name in _lazy_instances:
        value = _lazy_instances[name]()
        globals()[name] = value  # cache the computed value
        return value
    raise AttributeError(f"module {__name__} has no attribute {name}")
