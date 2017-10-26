# -*- coding: utf-8 -*-
#!/usr/bin/env python 
import msql, time
msql.connect('database.msql')
msql.execute('CREATE TABLE test (ID:id, category:Text, TEST:Int)')
t0 = time.time()
for test in range(1, 1000):
    msql.execute('INSERT INTO test ROW (category, TEST) NOT (TEST)', 'beta', test)
msql.update()
t1 = time.time()
print '{} saniyede {} data kaydedildi.'.format(t1-t0, 999)

#msql.UPDATE_(1, 'test', 'category', 'beta')
#msql.DELETE_(1, 'test')
#msql.gettables()
#msql.getrows('test') #-> test:table
#msql.gettype('test')
#msql.gets('test', 1)
#msql.count('test')
#msql.tableinfo_()
