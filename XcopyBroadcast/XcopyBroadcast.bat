@echo off 

ping -n 2 1.2.3.23 >> 'C:\applications\XcopyBroadcast_Ping.log' 
xcopy "C:\applications\SecureVNC" "\\1.2.3.23\c$\SecureVNC" /F /C /E
xcopy "\\1.2.3.23\c$\SecureVNC\Chaves" "\\1.2.3.23\c$\Program Files (x86)\uvnc bvba\UltraVNC" /F /C /E 

pause