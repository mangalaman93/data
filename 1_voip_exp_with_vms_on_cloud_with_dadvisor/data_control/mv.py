#!/usr/bin/env python

import os
import sys

SERVERS = ['109', '117', '131', '250', '118']
FOLDERS = ['client1', 'client2', 'server', 'snort1', 'snort2']
FILES = ['cpu_stats.txt', 'rx_stats.txt', 'tx_stats.txt']

if len(sys.argv) == 2:
	for server,folder in zip(SERVERS,FOLDERS):
		os.system('scp -i ~/.ssh/amanmangal.pem ubuntu@130.207.111.'+server+':*.txt '+folder)
		for f in FILES:
			os.system("mv "+folder+"/"+f+" "+folder+"/"+sys.argv[1]+"_"+f)
		os.system('scp -i ~/.ssh/amanmangal.pem ubuntu@130.207.111.'+server+\
			':/home/ubuntu/build_area/evpath/source/dadvisor/priv/*.csv .')
		os.system('mv *_rtt.csv '+folder+"/"+sys.argv[1]+'_sipp_rtt.csv')
		os.system('mv *.csv '+folder+"/"+sys.argv[1]+'_sipp.csv')
