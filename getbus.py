"""

"""
import urllib2, urllib
import json

def get_businfo(busno):
    parameters = {}
    parameters['strSrch'] = busno
    target = 'http://m.bus.go.kr/mBus/bus/getBusRouteList.bms'

    parameters = urllib.urlencode(parameters)

    while True:
        handler = urllib2.urlopen(target, parameters)
        if handler.code < 400:
            f = handler.read()
            j = json.loads(f.decode('cp949'))
            try:
                return j["resultList"][0]["busRouteId"]
            except:
                return None

def get_busroute(busno):
    routeid = get_businfo(busno)
    if not routeid:
        return
    parameters = {}
    parameters['busRouteId'] = routeid
    target = 'http://m.bus.go.kr/mBus/bus/getRouteAndPos.bms'

    parameters = urllib.urlencode(parameters)

    while True:
        handler = urllib2.urlopen(target, parameters)
        if handler.code < 400:
            f = handler.read()
            j = json.loads(f.decode('cp949'))
            routes = j["resultList"]
            for route in routes:
                busRouteNm = route['busRouteNm']
                busRouteId = route['busRouteId']
                stationNm = route['stationNm']
                stationNo = route['stationNo']
                x = route['gpsX']
                y = route['gpsY']
                l = '\t'.join([busRouteNm, busRouteId, stationNo, stationNm, x, y])
                # l = '\t'.join(list(route.values()))
                print(l.encode('utf-8'))
            break

def get_busroute_keys(busno):
    routeid = get_businfo(busno)
    parameters = {}
    parameters['busRouteId'] = routeid
    target = 'http://m.bus.go.kr/mBus/bus/getRouteAndPos.bms'

    parameters = urllib.urlencode(parameters)

    while True:
        handler = urllib2.urlopen(target, parameters)
        if handler.code < 400:
            f = handler.read()
            j = json.loads(f.decode('cp949'))
            route = j["resultList"][0]
            print(','.join(list(route.keys())))
            break

def main():
#     get_busroute_keys('0017')
    print('busno\tbusid\tstationid\tstationnm\tx\ty')
    busnos = ['0017', '0018', '1014', '1017', '1020', '1111', '1113', '1114', '1115', '1117', '1119', '1120', '1122', '1124', '1126', '1127', '1128', '1129', '1130', '1131', '1132', '1133', '1135', '1136', '1137', '1138', '1139', '1140',  '1141',  '1142', '1143', '1144', '1146', '1152', '1154', '1155', '1156', '1157', '1161', '1162', '1164', '1165', '1166', '1212', '1213', '1215', '1218', '1221', '1222', '1224', '1225', '1226', '1227', '1711', '2012', '2013', '2014', '2015', '2016', '2112', '2113', '2114', '2211', '2220', '2221', '2222', '2223', '2224', '2227', '2230', '2233', '2234', '2235', '2411', '2412', '2413', '2415', '3011', '3212', '3214', '3215', '3216', '3217', '3219', '3220', '3313', '3314', '3315', '3316', '3317', '3318', '3319', '3411', '3412', '3413', '3414', '3416', '3417', '3418', '3422', '3423', '4212', '4318', '4319', '4412', '4419', '4425', '4426', '4429', '4430', '4431', '4432', '4433', '4434', '5012', '5413', '5511', '5513', '5515', '5516', '5517', '5519', '5523', '5524', '5525', '5526', '5528', '5530', '5531', '5534', '5535', '5536', '5537', '5538', '5612', '5615', '5616', '5617', '5618', '5619', '5620', '5621', '5623', '5624', '5625', '5626', '5627', '5630', '5633', '5712', '5713', '5714', '6211', '6411', '6511', '6512', '6513', '6514', '6515', '6611', '6613', '6614', '6616', '6617', '6618', '6620', '6623', '6624', '6625', '6627', '6628', '6629', '6630', '6631', '6632', '6635', '6637', '6638', '6640', '6641', '6642', '6643', '6645', '6646', '6647', '6648', '6649', '6650', '6651', '6653', '6654', '6657', '6712', '6714', '6715', '6716', '7011', '7013A', '7013B', '7016', '7017', '7018', '7019', '7021', '7022', '7024', '7025', '7211', '7212', '7611', '7612', '7613', '7711', '7713', '7715', '7719', '7720', '7722', '7723', '7726', '7727', '7728', '7730', '7733', '7737', '7738']
    busnos += ['100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110A', '110B', '120', '121', '130', '140', '141', '142', '143', '144', '145', '146', '147', '148', '150', '151', '152', '153', '160', '162', '163', '171', '172', '201', '202', '240', '241', '260', '261', '262', '270', '271', '272', '273', '301', '302', '303', '320', '333', '340', '341', '350', '351', '352', '360', '370', '400', '401', '402', '405', '406', '407', '408', '420', '421', '440', '441', '461', '462', '463', '470', '471', '472', '500', '501', '502', '503', '504', '505', '506', '507', '540', '541', '542', '571', '600', '601', '602', '603', '604', '605', '606', '640', '641', '642', '643', '650', '651', '652', '653', '661', '662', '670', '672', '673', '700', '701', '702A', '702B', '703', '704', '705', '706', '707', '710', '720', '721', '740', '750A', '750B', '751', '752', '753', '760', '771']
    for busno in busnos:
        get_busroute(busno)

if __name__ == '__main__':
    main()
