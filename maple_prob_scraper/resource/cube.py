from enum import Enum


class CubeId(Enum):
    suspicious_cube = 2711000
    '''수상한 큐브'''
    craftmans_cube = 2711003
    '''장인의 큐브'''
    meisters_cube = 2711004
    '''명장의 큐브'''
    red_cube = 5062009
    '''레드 큐브'''
    black_cube = 5062010
    '''블랙 큐브'''
    additional_cube = 5062500
    '''에디셔널 큐브'''


class Grade(Enum):
    rare = 1
    '''레어'''
    epic = 2
    '''에픽'''
    unique = 3
    '''유니크'''
    legendary = 4
    '''레전드리'''


class PartType(Enum):
    weapon = 1
    '''무기'''
    emblem = 2
    '''엠블렘'''
    subweapon_except_forceshield_soulring = 3
    '''보조무기(포스실드, 소울링 제외)'''
    forceshield_soulring = 4
    '''포스실드, 소울링'''
    shield = 5
    '''방패'''
    cap = 6
    '''모자'''
    coat = 7
    '''상의'''
    longcoat = 8
    '''한벌옷'''
    pants = 9
    '''하의'''
    shoes = 10
    '''신발'''
    gloves = 11
    '''장갑'''
    cape = 12
    '''망토'''
    belt = 13
    '''벨트'''
    shoulder = 14
    '''어깨장식'''
    faceAccessory = 15
    '''얼굴장식'''
    eyeAccessory = 16
    '''눈장식'''
    earrings = 17
    '''귀고리'''
    ring = 18
    '''반지'''
    pendant = 19
    '''펜던트'''
    machineHeart = 20
    '''기계심장'''




















