import random,requests,json,logging,sys,time,pymysql
headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'Origin': '',
    'User-Agent': '',
    'Content-Type': 'application/json',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': '',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
}
# logging.basicConfig(filename='list.log', level=logging.INFO, format='%(message)s')

def parse_to_sql(response_json):
    keys = []
    values = []

    for i in response_json:
        if i=='namedParams':
            for j in response_json[i]:
                keys.append(j['key'])
                values.append(j['value'])
        else:
            keys.append(i)
            values.append(response_json[i])
    columns= "`, `".join([str(x) for x in keys])
    columns= "`" + columns + "`"
    values= "', '".join([str(x) for x in values])
    values= "'" + values + "'"
    return [columns, values]
def main(argv):
# argv = [0,1019039,1019040]
    base = []

    data = '{"serviceId":3,"account":"23423432","regionCode":"","subRegionCode":""}'
    con = pymysql.connect(host='localhost', port=3306, user='', passwd='', db='atad_ym')

    for i in range(int(argv[1]),int(argv[2])):
        data = json.loads(data)
        data['account'] = '{0:07d}'.format(i)
        data = json.dumps(data)  
        print(type(data))
        try:
            response = requests.post('https://', headers=headers, data=data)
            if response.json()['status']!='STPIMS-ERR-010':
                response_json = response.json()
                columns, values = parse_to_sql(response_json)[0], parse_to_sql(response_json)[1]
                with con:
                    cur = con.cursor()
                    print(values)
#                     sql = "truncate table table_name"  # clear table
                    sql = f"insert into table_name (`accountID`, {columns}) VALUES('{i}',{values})"
                    cur.execute(sql)
                    con.commit()
                    cur.close()
                info = str(i) + str(response.json()) + ';'
                print(i,'----', response.json()['fullName'],'--',response.json()['namedParams'][0]['value'])
    #                 logging.info(f'{info}') 
            if (i % 10 == 0):
                print(i, '----')
        except Exception as e:
            print(e,'XXXXXXXXXXXXXXXXXXXXXXXXXXXX')
            time.sleep(5)
            i -+ 1
        else:
            pass
        finally:
            pass
if __name__ == '__main__':
    main([0,1019035,1019040])
    #region":"10","_Region":"207"
