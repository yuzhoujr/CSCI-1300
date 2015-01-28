#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Problem 2
# Yu Zhou
# TA: Srinjita Bhaduri


Pass_completions = input ("Pass completions: ")
Pass_attempts = input ("Pass attempts: ")
Total_passing_yards = input ("Total passing yards: ")
Touchdowns = input ("Touchdowns!? : ")
Interceptions = input ("Interceptions: ")


C = ((Pass_completions / Pass_attempts) - 0.30) * 5
Y = (Total_passing_yards /Pass_attempts - 3) * 0.25
T = (Touchdowns / Pass_attempts) * 20
I = 2.375 - ((Interceptions / Pass_attempts) * 25)
PasserRating = (C+Y+T+I)/6*100

Rating = PasserRating

if Rating <= 85 :
	print "Rating: " , Rating, ", This is poor"

elif Rating > 85 and Rating <= 90 :
	print "Rating: " , Rating, ", This is mediocre"

elif Rating > 90 and Rating <= 95 :
	print "Rating: " , Rating, ", This is good"

elif Rating > 95 :
	print "Rating: " , Rating, ", This is great"




#Comment:
# utf-8 from the top comment solves the issue of Non-ASCII character calculation
# 5 arguments were grab from user
# C Y T I calculate for necessary entry
# Then PasserRating calculate the rate
# Adding if/esleif for conditioning