#!/bin/bash
xrandr --output DP-5 --off
sleep 2
xrandr --output DP-5 --auto --right-of DP-3 --rotate left

