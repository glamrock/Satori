#!/bin/bash
# -*- Mode: sh; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-

clear
sleep 1

#----- FUNCTIONS -----#

#run initial function

# CLEAN ENVIRONMENT FIRST
function grabem {

# Empty various cache files
    echo 'Grabbing files...'

    wget --user-agent=Chrome -O webstore.zip https://clients2.google.com/service/update2/crx?response=redirect&x=id%3Doncomejlklhkbffpdhpmhldlfambmjlf%26uc%26lang%3Den-US&prod=chrome
    wget -O github.zip https://github.com/glamrock/Satori/archive/master.zip

    echo 'Extracting folders'
    unzip github.zip -d github2
    unzip webstore.zip -d chrome
    mv github2/Satori-master/chrome ../../github
    rm -rf github2

    sleep 1

compare
}

#----- RUN UPDATES -----#

function compare {
    echo 'Comparing files...'
    diff -rq github/ chrome/ -x "chrome/manifest.json" -x "github/manifest.json"

 exit
}

grabem
