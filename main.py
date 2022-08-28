import os
import sys

file = open('test.txt','w',encoding='utf-8')
file.write('test')
file.close()
os.system('cd /d F:\/OneDrive\/Documents\/blog\/ && npm install hexo-deployer-git --save && hexo clean && hexo g && hexo d')