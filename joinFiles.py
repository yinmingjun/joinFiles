#!/usr/bin/env python
#coding=utf-8

import sys, os, stat

def printHelp():
    print "help:"
    print "\t"+sys.argv[0]+" <dir_name> <output_name> <ext_filter>"
    print "\t e.g."+sys.argv[0]+" .\src\main ucc_test.out java"

def joinFolder(dirName, outName, extFilter):
    for item in os.listdir(dirName):
        subpath = os.path.join(dirName, item)
        mode = os.stat(subpath)[stat.ST_MODE]
        if stat.S_ISDIR(mode):
            print "enter: "+subpath
            joinFolder(subpath, outName, extFilter)
        else :
            if subpath.endswith("."+extFilter) :
                print "join:" +subpath
                #append this file to out file
                out = open(outName, "a")
                join = open(subpath)
                out.write(join.read())
                out.close()
                join.close()


def main(argv):
    
    if len(argv) != 4 :
        printHelp()
        exit(0)
        
    dirName = argv[1]
    outName = argv[2]
    extFilter = argv[3]
    
    print "dir:"+dirName
    print "out:"+outName
    print "filter:"+extFilter

    joinFolder(dirName, outName, extFilter)
    
main(sys.argv)
    

