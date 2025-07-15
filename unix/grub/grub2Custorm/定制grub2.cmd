@echo off
title Grub2定制

:: 设置当前目录为脚本所在目录
pushd %~dp0

echo.
echo  Grub2启动文件定制
echo ================================================
echo  1.自选模块grubx64.efi   4.预设模块grubx64.efi
echo.
echo  2.自选模块grubia32.efi  5.预设模块grubia32.efi
echo.
echo  3.自选模块g2ldr         6.预设模块g2ldr
echo ================================================
set n=1
set /p n=请输入定制选项并回车确认(1-6,默认%n%)：
cls
goto do%n%

:do1
set str1=%~p0
for /f %%i in ('echo %str1%^|find /i "windows"') do set str=%%i
set format=x86_64-efi
set prefix=/efi/boot
if %str%a==a set prefix=/efi/grub
set output=bootx64.efi
set modules=part_msdos part_gpt fat ntfs normal chain search halt reboot
if %str%a==a set /p modules= < x64.txt
goto do

:do2
set format=i386-efi
set prefix=/efi/grub
set output=grubia32.efi
set /p modules= < x32.txt
goto do

:do3
set format=i386-pc
set prefix=/boot/grub
set output=core.img
set /p modules= < xpc.txt
call :do
goto pc

:do4
set format=x86_64-efi
set prefix=/efi/grub
set output=grubx64.efi
set /p modules= < arch\x64\builtin.txt
goto do

:do5
set format=i386-efi
set prefix=/efi/grub
set output=grubia32.efi
set /p modules= < arch\ia32\builtin.txt
goto do

:do6
set format=i386-pc
set prefix=/boot/grub
set output=core.img
set /p modules= < arch\legacy\builtin.txt
call :do
goto pc

:pc
Copy /B i386-pc\boot.img+core.img g2ldr
del core.img
exit /b

:do
grub-mkimage -O %format% -p %prefix% -o %output% %modules%