@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo === 更新工作台到云端 ===
echo.

git add -A
if errorlevel 1 (
  echo [错误] git add 失败
  pause
  exit /b 1
)

git commit -m "auto-update %date% %time%"
if errorlevel 1 (
  echo [提示] 没有新修改，无需更新
  pause
  exit /b 0
)

echo 正在推送到 GitHub...
git push origin main
if errorlevel 1 (
  echo.
  echo [错误] push 失败，请检查网络后重试
  echo 提示：如果 GitHub 连接不稳定，可以稍后再执行本脚本
  pause
  exit /b 1
)

echo.
echo [完成] 代码已推送，Cloudflare Pages 将在 1-2 分钟内自动更新。
echo 线上地址：https://customer-workbench-c59.pages.dev/
pause
