while($true) {
    Clear-Host
    $ESC = [char]27
    $CYAN = "$ESC[96m"
    $WHITE = "$ESC[97m"
    $RESET = "$ESC[0m"

    # LOGO
    Write-Host "`n  $CYAN ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ "
    Write-Host "  █       █  █ █  █       █       █       █       █       █       █"
    Write-Host "  █   ▄   █  █▄█  █   ▄   █   ▄   █   ▄▄▄▄█   ▄   █   ▄   █       █"
    Write-Host "  █  █▄█  █       █  █ █  █  █ █  █  █▄▄▄▄█  █ █  █  █▄█  █     ▄▄█"
    Write-Host "  █       █       █  █▄█  █  █▄█  █  █▄▄▄▄█  █▄█  █       █    █   "
    Write-Host "  █   ▄   █   ▄   █       █       █       █       █   ▄   █    █▄▄▄"
    Write-Host "  █▄▄█ █▄▄█▄▄█ █▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄█ █▄▄█▄▄▄▄▄▄▄█$RESET"
    Write-Host "`n   [!] SYSTEM STATUS: ACTIVE | IDENTITY: DIRECTOR OF AI INNOVATION" -ForegroundColor Gray

    Write-Host "`n   $CYAN [1]$WHITE DEVELOPER AGENT $RESET (GitHub Guard)"
    Write-Host "   $CYAN [2]$WHITE STRATEGY AGENT  $RESET (Reporting Brain)"
    Write-Host "   $CYAN [3]$WHITE SYSTEM KERNEL   $RESET (Auto-Archive)"
    Write-Host "   $CYAN [4]$WHITE PROJECT SPAWNER $RESET (Template Engine)"
    Write-Host "   $CYAN [0]$WHITE EXIT            $RESET"

    Write-Host "`n  $CYAN ────────────────────────────────────────────────────────────$RESET"
    $choice = Read-Host "   $CYAN >>$WHITE SELECT MODE$RESET"

    switch ($choice) {
        "1" { Write-Host "`n [!] RUNNING DEV..." -ForegroundColor Cyan; python core.py dev; pause }
        "2" { Write-Host "`n [!] RUNNING STRATEGY..." -ForegroundColor Cyan; python core.py strategy; pause }
        "3" { Write-Host "`n [!] RUNNING KERNEL..." -ForegroundColor Cyan; python core.py kernel; pause }
        "4" { Write-Host "`n [!] RUNNING SPAWNER..." -ForegroundColor Cyan; python core.py spawn; pause }
        "0" { Write-Host "`n [!] Shutting down Workforce..."; exit }
        default { 
            Write-Host "`n [X] INVALID SELECTION." -ForegroundColor Red
            Start-Sleep -s 1 
        }
    }
}