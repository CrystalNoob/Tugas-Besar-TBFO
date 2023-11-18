# HTML Checker dengan Pushdown Automata (PDA)
> Tugas Besar TBFO Kelas 02 Kelompok 14
> 
> Oleh Kelompok Ejaan Yang diFormalkan (EYF):<br>
> 1. 13522061 Maximilian Sulistiyo<br>
> 2. 13522075 Marvel Pangondian<br>
> 3. 13522094 Andhika Tantyo Anugrah<br>
> 
> Sekolah Teknik Elektro dan Informatika<br>
> Institut Teknologi Bandung<br>
> Semester III Tahun 2023/2024

Kami diminta untuk membuat sebuah program pendeteksi error untuk HTML. Oleh sebab itu, implementasikan sebuah program yang dapat memeriksa kebenaran HTML dari segi nama tag yang digunakan serta attribute yang dimilikinya. Pada tugas pemrograman ini, gunakanlah konsep Pushdown Automata (PDA) dalam mencapai hal tersebut yang diimplementasikan dalam bahasa Python.

## Table of Contents
* [Getting started](#getting-started)
* [Developing](#developing)
* [Building](#building)
* [Features](#features)
* [Links](#links)

## Getting started

Needs Python (py) in order to run. Python can be found at [their website](https://www.python.org/downloads/). It also needs numpy library, bla bla, and bla bla that are listed in the requirements file. The requirements.txt file is located at the src folder. To automatically installed all of the modules required, simply copy and paste these lines into your terminal.

```shell
pip install -r requirements.txt
```

I know when using pip, it’s good practice to use a virtual environment, but I don't care right now. So, happy developing :D

## Developing

Here's a brief intro about what a developer must do in order to start developing
the project further:

```shell
git clone git@github.com:CrystalNoob/Tugas-Besar-TBFO.git
cd Tugas-Besar-TBFO/
```

Start developing in your favorite IDE.

### Building

Additional steps for the developer to build the project after some code changes.

```shell
cd ./src
py PDA.py PDA.txt htmlFile.html
```

Here, py runs the PDA.py file and parse the PDA to check the htmlFile.

## Features

What's all the bells and whistles this project can perform?
* HTML Syntax Evaluation

## Links

- [Tugas Pemrograman IF2124 Teori Bahasa Formal dan Otomata](https://docs.google.com/document/d/1W5QSSHVrXvArj3Aonw4FhbfctBK6J2YGefXpWsLW43Y/edit)
- [Repository](https://github.com/CrystalNoob/Tugas-Besar-TBFO)
- [Laporan Tugas Besar [email std]](https://docs.google.com/document/d/1BMXj_jpofB1vJbdooLsHa3aDacjD5mSNYYTZocM_rF0/edit)