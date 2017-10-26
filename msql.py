# -*- coding: utf-8 -*-
#!/usr/bin/env python
#Kararlı (STABLE) (Son güncelleme:20-Ekim-2017:16:11)
global table
def UPDATE_(id, table, row, string):
    global database
    table = str(table)
    row = str(row)
    string = str(string)
    id = str(id)
    search = '[' + table + ':' + row + ':' + id + ']'
    start = database.find(search) + 1
    end = database.find(search, start)
    old = database[start-1:end+len(search)]
    new = '{}{}{}'.format(search, string, search)
    database = database.replace(old, new)
    #update() 
def DELETE_(id, table):
    global database
    id = str(id)
    table = str(table)
    for beta in getrows(table):
        string = '[' + table + ':' + beta + ':' + id + ']' + str(gets(table, id)[getrows(table).index(beta)])
        delete = '[' + table + ':' + beta + ':' + id + ']' + '' ##iyilestirme <- (Null)
        database = database.replace(string, delete)
    update()
def research(source, string):
    return source.find(string)
def trim(string):
    index = []
    for trim in range(0, len(string), +1):
        if string[trim:trim+1] != ' ': 
            index.append(trim)
            break   
    for trim in range(len(string)-1,-1, -1):
        if string[trim:trim+1] != ' ': 
            index.append(trim+1)
            break
    return string[index[0]:index[1]]
def tableinfo_():
    global tableinfo
    tableinfo = {} 
    for tablelist in gettables():
        table = tablelist
        row = getrows(table)
        type = gettype(table)
        tableinfo[table] = row, type
    return tableinfo
def connect(beta):
    import os
    global database, n; database = ''
    n = beta
    try:
        if os.path.lexists(beta) == True:
            with open(beta,"r") as source: 
                database = source.read() + "\n"
            tableinfo_()
            return database
        else: return 'database file not find error!'
    except:
        return ''
def gettables():
    try:
        beta = database.find("table:info")
        for index in range(beta+len('table:info'), len(database), +1):
            if database[index:index+1] == "\n":
                f = index; break
        return database[beta+len('table:info')+1:index].split('|')
    except:
        return ''
def getrows(table):
    beta = database.find(table+":row")+len(table+":row")+1
    for index in range(beta, len(database), +1):
        if database[index:index+1] == "\n":
            f = index; break
    return database[beta:f].split('|')
def gettype(table):
    beta = database.find(table+":type")+len(table+":type")+1
    for index in range(beta, len(database), +1):
        if database[index:index+1] == "\n":
            f = index; break
    return database[beta:f].split('|')
def gets(table, id):
    id = str(id)
    item, index, gets = [], [], []
    item.append(id)
    try:
        for row in getrows(table)[1:]: ##iyilestirme <- (0:)
            '''if row == getrows(table)[0]: ##id
                continue'''
            string = "[" + table + ":" + row + ":" + id + "]"
            ls = len(string)
            index.append(database.find(string) + ls)
            for beta in range(index[len(index)-1], len(database)):
                if database[beta:beta+ls] == string:
                    index.insert(len(index), beta)
                    break #iyilestirme <- (continue)
        for beta in range(0, len(index), +2):
            test = database[index[beta]:index[beta+1]]
            item.append(test)
        for type, string in zip(gettype(table), item):
            if (type == 'Int'): gets.append(int(string))
            elif (type == 'Bool'): 
                if (string == '0'): 
                    gets.append(False)
                else:
                    gets.append(True)
            elif (type == 'Float'): 
                gets.append(float(string))
            elif (type == 'id'): 
                gets.append(int(string))           
            else: 
                gets.append(str(string))
        return gets    
    except:
        return 'connect error!'
        pass
def count(table):
    global database
    try:
        string = table+':'+'count'+'|'
        count = database.find(string) + len(string)
        for ln_ in range(count, count + 16, +1):
            if database[ln_:ln_+1] == '\n':
                break
        return int(database[count:ln_])
    except:
        return 'connect error!'
        pass
def update():
    global database, n
    with open(n, "w") as msql: msql.write(database[0:len(database)-1]) 
def execute(command, *values):
    global database, stringother, stringid; stringid, stringother = '', ''
    row  = []
    ifnot = []
    sort = []
    select = []
    LIST = []
    global table
    global commandchar; commandchar = ''
    global str_beforetable; str_beforetable = ''
    global str_beforetype; str_beforetype = ''
    global str_beforerow; str_beforerow = ''
    global str_beforecout; str_beforecout = ''
    global str_newtype; str_newtype = ''
    global str_newrow; str_newrow = '' 
    global str_oldtable; str_oldtable = ''
    global str_newtable; str_newtable = ''
    global str_newcount; str_newcount = ''
    global newtable; newtable = ''
    info_newtable = []
    command_list = []
    for add in command:
        if add != ' ': commandchar = commandchar + add 
    for replcommand in ['INSERT', 'INTO','ROW', '(', ',', ')', 'SELECT', '*', 'FROM','SORT','CREATE', 'TABLE', 'LIST']:
        if replcommand is ',': 
            commandchar = commandchar.replace(replcommand, ' ') 
        commandchar = commandchar.replace(replcommand, ' ' + replcommand + ' ')
    commandchar = commandchar.replace('  ', ' ')
    commandchar = trim(commandchar)
    for command in commandchar.split(' '):
        command_list.append(command)
    for table in command_list:
        if table == 'INTO' or table == 'FROM' or table == 'TABLE':
            table = command_list[command_list.index(table)+1]
            break
    for row_ in command_list:
        if row_ == 'ROW':
            row.append('ROW')
            for add_ in command_list[command_list.index(row_)+2:]:
                if add_ == ')':
                    break
                row.append(add_)
    for not_ in command_list:
        if not_ == 'NOT':
            ifnot.append('NOT')
            for add_ in command_list[command_list.index(not_)+2:]:
                if add_ == ')':
                    break
                ifnot.append(add_)
    for sort_ in command_list:
        if sort_ == 'SORT':
            for add_ in command_list[command_list.index(sort_)+2:]:
                if add_ == ')':
                    break
                sort.append(add_)
    for list_ in command_list:
        if list_ == 'LIST':
            for add_ in command_list[command_list.index(list_)+2:]:
                if add_ == ')':
                    break
                LIST.append(add_)
    for newtable_ in command_list:
        if newtable_ == 'TABLE':
            for add_ in command_list[command_list.index(newtable_)+3:]:
                if add_ == ')':
                    break
                info_newtable.append(add_)  
    if command_list[0:2] == ['CREATE', 'TABLE']:
        if table not in gettables():
            for beforetable in gettables()[0:]:
                str_beforetable = str_beforetable +'|'+ beforetable
            str_oldtable = str_oldtable + 'table:info' + str_beforetable + '\n'
            for beforetable in gettables()[0:]:
                str_beforetype = ''
                str_beforerow = ''
                str_beforecout = ''
                for beforetype in gettype(beforetable):
                    str_beforetype = str_beforetype +'|'+beforetype
                str_oldtable = str_oldtable + beforetable + ':type' + str_beforetype + '\n'
                for beforerow in getrows(beforetable):
                    str_beforerow = str_beforerow +'|'+beforerow
                str_oldtable = str_oldtable + beforetable + ':row' + str_beforerow + '\n'
                str_beforecout = str_beforecout + beforetable + ':' + 'count' +'|'+ str(count(beforetable))
                str_oldtable = str_oldtable + str_beforecout + '\n' #
            for before in  gettables()[0:]:
                str_newtable = str_newtable + '|' + before 
            str_newtable = 'table:info' + str_newtable +'|'+ table + '\n'
            for newtype in info_newtable[0:]:
                str_newtype = str_newtype +'|'+ newtype.split(':')[1]
            str_newtable = table +':type' + str_newtype + '\n'
            for newrow in info_newtable[0:]:
                str_newrow = str_newrow +'|'+ newrow.split(':')[0]
            str_newtable = str_newtable +table+':row'+ str_newrow + '\n'
            str_newcount = table + ':' + 'count' +'|0'+'\n'
            str_newtable = str_newtable + str_newcount
            newtable = str_oldtable + str_newtable
            newtable = newtable.replace('table:info'+str_beforetable, 'table:info'+str_beforetable + '|' + table)
            database = newtable
            update()
    if command_list[0:2] == ['INSERT','INTO']:
        if  len(row[1:]) is len(values):
            stringid = '{}{}{}ID{}{}{}'.format('[',table,':',':',count(table)+1,']\n')
            for other in row[1:]:
                beta = '['+table+':'+other+':'+str(count(table)+1)+']'
                stringother = stringother + beta+str(values[row.index(other)-1])+beta+'\n'
            if len(ifnot) > 0:
                string = ']'+str(values[row.index(ifnot[1:][0])-1])+'['+table+':'+ifnot[1:][0]+':'
                if research(database, string) is  -1:
                    beta = table+':'+'count'+'|'
                    database = database.replace(beta+str(count(table)),beta+str(count(table)+1))
                    database = database + stringid + stringother
                    return -1 #kayit yok
                else:
                    return 1 #kayit var
            else:
                beta = table+':'+'count'+'|'
                database = database.replace(beta+str(count(table)),beta+str(count(table)+1))
                database = database + stringid + stringother
        else:
            return 'hata', row[1:], values
    if command_list[0:3] == ['SELECT', '*', 'FROM']:
        if len(sort) is 0:
            if len(LIST) is 0:
                for id in range(1, count(table)+1):
                    select.append(gets(table, id))
            else:
                for id in range(int(LIST[0].split(':')[0]), int(LIST[0].split(':')[1])+1):
                    select.append(gets(table, id))
        else:
            if sort[0] == 'ZA':
                if len(LIST) is 0:
                    for id in range(count(table), 0, -1):
                        select.append(gets(table, id))
                if len(LIST) > 0:
                    for id in range(int(LIST[0].split(':')[1]), int(LIST[0].split(':')[0])-1, -1):
                        select.append(gets(table, id))
            if sort[0] == 'AZ':
                if len(LIST) is 0:
                    for id in range(1, count(table)+1):
                        select.append(gets(table, id))
                if len(LIST) > 0:
                    for id in range(int(LIST[0].split(':')[0]), int(LIST[0].split(':')[1])+1):
                        select.append(gets(table, id))
        return select
