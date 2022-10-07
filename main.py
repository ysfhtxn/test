import os
import sys

god = '---\n'
god = god + 'title: 今日更新番剧\n'
god = god + 'date: 2022-9-29 12:00:00\n'
god = god + 'tags: anime\n'
god = god + '---\n'

god = god + '1'
god = god + '2'
god = god + '3'
god = god + '4'

with open("anime.md", 'w', encoding="utf-8") as f:
        f.write(god)

#print(god)
