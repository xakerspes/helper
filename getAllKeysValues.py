def getAllKeysValues(response_json):
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
        return = [columns,values]
