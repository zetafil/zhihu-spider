#!/bin/bash
ts=`date +%y%m%d%H%M%S`
nohup scrapy crawl people -o items_${ts}.json -s LOG_FILE=spider.log.$ts >> spider.log 2>&1 &
