
# to run just type:
# . scripts\local_enable.ps1

try {
    . $HOME\.venvs\demo\Scripts\activate.ps1
}
catch {
    . ..\..\.venvs\demo\Scripts\activate.ps1
}

cd src
