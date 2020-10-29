#!/bin/zsh

home=/Users/ryushi/PycharmProjects/card3/void/

base=https://atcoder.jp/contests/abc180/tasks/abc180_

var1=${base}a
var2=${base}b
var3=${base}c
var4=${base}d

rm -rf ${home}A/test
rm -rf ${home}B/test
rm -rf ${home}C/test
rm -rf ${home}D/test

cd ${home}A
oj d $var1
cd ${home}B
oj d $var2
cd ${home}C
oj d $var3
cd ${home}D
oj d $var4

cd ${home}
