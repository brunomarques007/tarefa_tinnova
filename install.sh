#!/bin/bash

function instalar_dependencias() {
  sudo apt-get update -y > /dev/null
  for cmd in python3 pip; do
    command -v $cmd >/dev/null || sudo apt-get install -y $cmd
  done
  command -v pipx >/dev/null || pip install pipx
  command -v poetry >/dev/null || pipx install poetry && pipx inject poetry poetry-plugin-shell
  command -v ignr >/dev/null || pipx install ignr
}


function instalar_poetry() {
  if [ ! -f "poetry.lock" ]; then
    poetry install
  else
    poetry update
  fi
}


function finalizar_script() {
  echo -e "\n\033[1;30;103m\u2705 Projeto instalado com sucesso para a TINNOVA! \u2705 \033[m"
  echo -e "\033[1;93mPara iniciar o projeto, execute: \033[m"
  echo -e "poetry run python main.py"
}

### Execução do Script ###
instalar_dependencias
instalar_poetry

popd > /dev/null
exit 0