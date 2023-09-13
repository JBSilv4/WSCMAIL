# WSCMAIL - SMTP/IMAP
## Ferramentas e Linguagens Utilizadas:
<img src="https://img.shields.io/badge/Linux-black?style=for-the-badge&logo=linux" /> <img src="https://img.shields.io/badge/Ansible-black?style=for-the-badge&logo=Ansible" /> <img src="https://img.shields.io/badge/Flask-black?style=for-the-badge&logo=flask" /> <img src="https://img.shields.io/badge/Shell_Script-black?style=for-the-badge&logo=gnu-bash" /> <img src="https://img.shields.io/badge/Python-black?style=for-the-badge&logo=python" />

### Sobre o Projeto:
Ele foi feito para rodar no linux, sendo mais especifico no **Debian**, Fiz esse projeto para testar meus conhecimentos em algumas tecnologias

* **Instalação:**
  ```bash
  ./install
  ```
* **Fazer Algumas Alterações:**<br>
  Você precisa fazer algumas alterações, para que funcione com o seu Servidor DNS.
  Tenha em mente que você já precisa ter configurado o MX e o PTR no seu DNS.

  Entre no diretorio /etc/wscmail/src/mail/hosts e mude par seu ip e dominio
  ```bash
  [wscmail]
  (ip-da-maquina) domain=(seu-dominio)
  ```
* **Apos Instalar use o comando:**
  ```bash
  systemctl start wscmail
  
  systemctl enable wscmail #para subir com a inicialização
  ```
