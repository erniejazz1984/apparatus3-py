#!/lab/software/epd-7.0-1-rh5-x86/bin/python

import os
import glob
import time

def waitforit( path, expr ):
    current = glob.glob(path + expr) 
    #print "waiting..."
    #for i in range(20):
    while ( True ) :
      time.sleep(2)
      new = glob.glob( path + expr ) 
      diff = []
      for f in new: 
         if not f in current:
           diff.append(f)
      if len(diff) > 0:
         return diff


if __name__ == "__main__":
  diff = waitforit( '/lab/data/app3/2012/1206/120621/', '????atoms.fits' )
  print diff
    


  


