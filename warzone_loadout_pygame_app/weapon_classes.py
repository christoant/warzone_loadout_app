
list_ars = []
list_smgs = []
list_shotguns = []
list_lmgs = []
list_marksman_rifles = []
list_sniper_rifles = []
list_handguns = []
list_melee = []
attachments_list = []


class Weapon:
    def __init__(
        self, game, name, guntype, muzzle, barrel, optic, stock, underbarrel, reargrip,
    ):  
        self.game = game
        self.name = name
        self.guntype = guntype
        self.muzzle = muzzle
        self.barrel = barrel
        self.optic = optic
        self.stock = stock
        self.underbarrel = underbarrel
        self.reargrip = reargrip
        
        curr_attachments_list = vars(self)
        curr_attachments_list.update({'full_name': str(self.game + " " + self.name)})
        attachments_list.append(curr_attachments_list)
        print(attachments_list[len(attachments_list) - 1]['full_name'])
        

        if self.guntype == "ar":
            list_ars.append(self.game + " " + self.name)
        elif self.guntype == "smg":
            list_smgs.append(self.game + " " + self.name)
        elif self.guntype == "shotgun":
            list_shotguns.append(self.game + " " + self.name)
        elif self.guntype == "lmg":
            list_lmgs.append(self.game + " " + self.name)
        elif self.guntype == "marksman_rifle" or "marksman rifle":
            list_marksman_rifles.append(self.game + " " + self.name)
        elif self.guntype == "sniper_rifle" or "sniper rifle":
            list_sniper_rifles.append(self.game + " " + self.name)
        elif self.guntype == "handgun":
            list_handguns.append(self.game + " " + self.name)
        elif self.guntype == "melee":
            list_melee.append(self.game + " " + self.name)
        else:
            print(self.name + "'s guntype is not valid...")


class MW(Weapon):
    MAX_MW_ATTACHMENTS = 5

    def __init__(
        self,
        game,
        name,
        guntype,
        muzzle,
        barrel,
        optic,
        stock,
        underbarrel,
        reargrip,
        laser,
        ammo,
        perk,
    ):
        super().__init__(
            game, name, guntype, muzzle, barrel, optic, stock, underbarrel, reargrip, 
        )
        self.laser = laser
        self.ammo = ammo
        self.perk = perk


class CW(Weapon):
    MAX_CW_ATTACHMENTS = 5

    def __init__(
        self,
        game,
        name,
        guntype,
        muzzle,
        barrel,
        optic,
        stock,
        underbarrel,
        reargrip,
        laser,
        ammo,
    ):
        super().__init__(
            game, name, guntype, muzzle, barrel, optic, stock, underbarrel, reargrip
        )
        self.laser = laser
        self.ammo = ammo


class VG(Weapon):
    MAX_VG_ATTACHMENTS = 5

    def __init__(
        self,
        game,
        name,
        guntype,
        muzzle,
        barrel,
        optic,
        stock,
        underbarrel,
        reargrip,
        ammo,
        magazine,
        perk,
        perk2,
    ):
        super().__init__(
            game, name, guntype, muzzle, barrel, optic, stock, underbarrel, reargrip
        )
        self.ammo = ammo
        self.magazine = magazine
        self.perk = perk
        self.perk2 = perk2


mw_mp5 = MW(
    "mw",
    "mp5",
    "smg",
    "",
    "thic integral suppressor",
    "",
    "ftac collapsible",
    "merc foregrip",
    "",
    "5mW laser",
    "45 round mag",
    "",
)
# print(mw_mp5)

cw_mp5 = CW(
    "cw",
    "mp5",
    "smg",
    "agency suppressor",
    "",
    "",
    "raider stock",
    "",
    "bruiser grip",
    "tiger team spotlight",
    "stanag 50 rnd drum",
)
# print(cw_mp5)

vg_mp40 = VG(
    "vg",
    "mp40",
    "smg",
    "mercury suppressor",
    "krausnick 317mm 04b",
    "krausnick 1s01m",
    "no stock",
    "m301 hand stop",
    "polymer grip",
    "incendiary",
    "45 rnd",
    "brace",
    "quick",
)



