@echo off
title codealpha_automation - Auto Git Sync Service
echo Starting Auto Git Sync for Task 3...
cd /d "%~dp0"
python auto_sync.py
pause
