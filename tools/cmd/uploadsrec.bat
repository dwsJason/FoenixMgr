@echo off
REM Upload an SREC file to the Foenix

python %FOENIXHOME%\FoenixMgr\fnxmgr.py --upload-srec %1
