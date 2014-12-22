#!/usr/bin/env python

import os, glob, datetime, time
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "uSystem.settings")

def main():
        from uQuery.models import AllUser
        
        fileall = glob.glob('fwq\*.txt')
        for filename in fileall:
                f = open('%s' % filename)
                db = filename.split('\\')[1].split('.')[0]
                llist = list()
                for l in f:
                        llist.append(l)
                        if len(llist) == 200000:
                                userList = list()
                                userList = [AllUser(time=line.split('\t')[0], \
                                         fwqName=line.split('\t')[1], \
                                         fwqID=line.split('\t')[2], \
                                         usrID=line.split('\t')[3], \
                                         usrName=line.split('\t')[4], \
                                         account=line.split('\t')[5], \
                                         app=line.split('\t')[6], \
                                         device=line.split('\t')[7], \
                                         udid=line.split('\t')[8], \
                                         usrTel="0")
                                    for line in llist]
                                
                                if db == '10004':
                                        User10004.objects.bulk_create(userList)
                                
                                llist = list()
                
                userList = [AllUser(time=line.split('\t')[0], \
                         fwqName=line.split('\t')[1], \
                         fwqID=line.split('\t')[2], \
                         usrID=line.split('\t')[3], \
                         usrName=line.split('\t')[4], \
                         account=line.split('\t')[5], \
                         app=line.split('\t')[6], \
                         device=line.split('\t')[7], \
                         udid=line.split('\t')[8], \
                         usrTel="0")
                    for line in llist]
                
                if db == '10004':
                        User10004.objects.bulk_create(userList)

if __name__ == "__main__":
        while 1:
                try:
                        main()
                        print('Import Done!')
                        print datetime.datetime.now()
                        time.sleep(600)
                except:
                        print "restart"
