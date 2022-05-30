<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/DPtxWEl.png" alt="Project logo"></a>
</p>

<h3 align="center">DCA Bot</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Dollar Cost Averaging Bot
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Tech](#tech)
- [Installation](#installation)
- [Built Using](#built_using)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

DCA Bot (Dollar Cost Averaging Bot) is a bot that executes periodic purchases of a target asset (in this case, crypto) in an effort to reduce the impact of volatility on the overall purchase. The purchases occur regardless of the asset's price and at regular intervals.



## 💻 Tech <a name = "tech"></a>
DCA Bot is written in [Python 3](https://www.python.org/)


## ⚙️ Installation  <a name = "installation"></a>


### Fedora 34(Workstation)

Fedora contains many popular packages for Python. Usually, they are named with a python3- prefix, such as python3-requests.

These are useful for scripting and exploring Python and for Fedora-specific applications. For software development or reproducible data analysis, it is better to use virtual environments.

Please install these packages and set up your environment in the order listed below. Run an upgrade or update if you find that the package is already installed:

- Python 3. Run the 'python3 -V' command to see the version you have installed.

- Ensure you have python version >= 3.8+ installed.


- Using VS Code as our text editor:  right click on the folder explorer and open a terminal


Using virtual environments
When you work on a project, it is good to keep it inside a virtual environment. It will keep the dependencies you need in one place and you do not have to worry about different projects which need different versions of the same module. It also makes it easy to collaborate with people who don’t use Fedora yet.

- create a virtual environment 
```sh
<your_preferred_envname>
``` 
which will contain Python and pip. You can use pip to install a project’s dependencies.
```sh
python -m venv <your_preferred_envname>
```
If you want to work in the virtual environment, you have to activate it.
```sh
source <your_preferred_envname>/bin/activate
```
When the virtual environment is activated (you can see its name in brackets at the beginning of your prompt), you can install modules via pip install.
```sh
<your_preferred_envname> python -m pip install requests
```

That is all, you have successfully created your own virtual environment. Now you can run Python (see above) and start working on your project.

When you finish your work, you can deactivate the virtual environment.
```sh
 <your_preferred_envname>  deactivate
```

- Install requirements in the virtual environment created:

```sh
pip install -r requirements.txt
```

- Install [PostgreSQL](https://www.postgresql.org/).

- Create a database with PostgresQL, the installation instructions for Fedora can be found [here](https://www.postgresql.org/download/linux/redhat/). Make sure to note Database name, Database Username and Password and also ensure that the server is running




### Windows 10 Users

Please install and set up the following packages first. Upgrade if you find the package is already installed:

- Download [Python 3](https://www.python.org/downloads/). It is advisable to install the python package as an administrator. Click on the 'Add path' checkbox before moving on to the next step of the installation process. Run this command in your terminal to see the version you have installed.

  ```sh
  python3 -V
  ```

- Ensure you have python version >= 3.8+ installed.

- Download [pip](https://pip.pypa.io/en/latest/installing/) and follow the instructions in the link as an installation guide.

- [PostgreSQL](https://www.postgresql.org/download/windows/) (Ensure the server is running).

- It is advisable to install packages in a virtual environment. The README uses [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html#basic-installation) to create this environment. You could use any virtualenv package of your choice but for Windows, install this wrapper with:

  ```sh
  pip install virtualenvwrapper-win
  ```

- Create a new virtual environment:

  ```sh
  mkvirtualenv <envname>
  ```

- Activate the virtual environment with:

  ```sh
  <envname>\Scripts\activate
  ```
  or use this command
  ```sh 
  & C:/Users/<username>/Envs/<envname>/Scripts/Activate.ps1
  ```

- Install requirements in the virtual environment created:

  ```sh
  pip install -r requirements.txt
  ```

* Deactivate the virtual environment with:

  ```sh
  deactivate
  ```

- Create a database with PostgreSQL, if you installed it earlier. If not, installation instructions can be found [here](https://www.postgresql.org/download/windows/). Make sure to note database name, database username and password.


### Python installation instructions for Windows, macOS and other Linux distributions


## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://[python.org]/) - Programming Language
- [PostgreSQL](https://www.postgresql.org/) - Database
- [Quidax API](https://docs.quidax.com/docs) - Crypto Service API
- [PeeWee](https://docs.peewee-orm.com/en/latest/index.html) - Object Relational Mapper
- [Doppler](https://www.doppler.com/) - Environment Secrets Manager
- [Mailgun](https://www.mailgun.com/) - Email Service
- [GitHub Actions](https://docs.github.com/en/actions) - Continuous Integration

## ✍️ Authors <a name = "authors"></a>

- [@seun-beta](https://github.com/seun-beta) - Idea & Initial work

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- Inspiration
- References
