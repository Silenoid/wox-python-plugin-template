# This scripts print the tail of Wox logs. Change it as you need.

$dateForFile=Get-Date -Format "yyyy-MM-dd"

# WARNING: change the root directory to your own
$dateForFile="C:\Users\user\AppData\Roaming\Wox\Logs\1.4.1196\"+$dateForFile+".txt"

# Tail log file on console
Get-Content $dateForFile -Wait -Tail 30

# Clean
Remove-Variable $dateForFile