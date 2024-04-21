@echo off
setlocal

:: Pedir uma mensagem de commit
set /p commit_message=Digite a mensagem do commit (ou pressione Enter para mensagem padrao): 

:: Se o usuário pressionar Enter sem digitar nada, usar uma mensagem padrão
if "%commit_message%"=="" (
    set commit_message=Mudancas padroes realizadas
)

:: Adicionar todos os arquivos modificados
git add .

:: Fazer o commit com a mensagem fornecida ou padrão
git commit -m "%commit_message%"

:: Enviar para o repositório remoto
git push origin main

echo Alteracoes enviadas com sucesso para o GitHub com a mensagem: "%commit_message%"
