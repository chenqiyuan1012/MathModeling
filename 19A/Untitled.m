close all;clear all;clc;
A=xlsread('附件3-弹性模量与压力.xlsx',1);
x=A(:,1);
y=A(:,2);
scatter(x,y);