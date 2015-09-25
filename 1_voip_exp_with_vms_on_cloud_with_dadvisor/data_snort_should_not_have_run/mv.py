#!/usr/bin/env python

import os
import sys

SERVERS = ['118', '131', '250']
FOLERS = ['client', 'server', 'snort']
FILES = ['cpu_stats.txt', 'rx_stats.txt', 'tx_stats.txt', 'usage.txt']

if len(sys.argv) == 2:
	for server,folder in zip(SERVERS,FOLERS):
		os.system('scp -i ~/.ssh/amanmangal.pem ubuntu@130.207.111.'+server+':*.txt '+folder)
	for folder in FOLERS:
		for f in FILES:
			os.system("mv "+folder+"/"+f+" "+folder+"/"+sys.argv[1]+"_"+f)

os.system('scp -i ~/.ssh/amanmangal.pem ubuntu@130.207.111.131:*.csv server/')
os.system('mv server/*.csv server/'+sys.argv[1]+"_uas.csv")

os.system('scp -i ~/.ssh/amanmangal.pem ubuntu@130.207.111.118:build_area/evpath/source/examples/dAdvisor/priv/*.csv client/')
os.system('mv client/*.csv client/'+sys.argv[1]+"_uac.csv")
