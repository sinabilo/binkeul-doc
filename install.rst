필수 
================
* python 3.7.8 설치 

* pip3 install sphinx

* pip3 install docxbuilder


확장(편집용)
==========================

* pip3 install pyside2

* ffmpeg 설치 

* graphviz 설치 ::

    # powershell 을 관리자모드로 실행
    
    > Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
    
    또는 
    
    > Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

    # 명령행에서 ``choco -v`` 실행
    # powershell 에서 다음 명령으로 설치 
    
    > choco install graphviz
    
    
* pandoc 설치 