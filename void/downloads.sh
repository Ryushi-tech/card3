#!/bin/zsh

contest=ABC
num=184

home=/Users/ryushi/PycharmProjects/card3/void/
base=https://atcoder.jp/contests/${contest}${num}/tasks/${contest}${num}_

var1=${base}a
var2=${base}b
var3=${base}c
var4=${base}d
var5=${base}e

rm -rf ${home}A/test ${home}B/test ${home}C/test ${home}D/test ${home}E/test

cd ${home}A || exit
oj d $var1
cd ${home}B || exit
oj d $var2
cd ${home}C || exit
oj d $var3
cd ${home}D || exit
oj d $var4
cd ${home}E || exit
oj d $var5

cd ${home} || exit
