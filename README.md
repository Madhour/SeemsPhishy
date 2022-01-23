<div align="center">
<h2>SeemsPhishy</h2>
<img src="src/SeemsPhishy/gui/app/static/assets/img/Logo_big.png" alt="Logo" width="180" align="center"/>
<br><br>
</div>

A penetration testing toolkit for collecting and extracting information about target organizations from publicly available text data. 


[![GitHub issues](https://img.shields.io/github/issues/Madhour/SeemsPhishy)](https://github.com/Madhour/SeemsPhishy/issues)
[![GitHub forks](https://img.shields.io/github/forks/Madhour/SeemsPhishy)](https://github.com/Madhour/SeemsPhishy/network)
[![GitHub stars](https://img.shields.io/github/stars/Madhour/SeemsPhishy)](https://github.com/Madhour/SeemsPhishy/stargazers)
[![GitHub license](https://img.shields.io/github/license/Madhour/SeemsPhishy)](https://github.com/Madhour/SeemsPhishy/blob/main/LICENSE)

<br>

![Postgres](https://img.shields.io/badge/DB-Postgres-lightgrey?style=flat&logo=postgresql)
![Docker](https://img.shields.io/badge/Container-Docker-lightgrey?style=flat&logo=docker)

![Flask](https://img.shields.io/badge/WebFramework-Flask-lightgrey?style=flat&logo=flask)
![Flask](https://img.shields.io/badge/Framework-Bootstrap-lightgrey?style=flat&logo=bootstrap)
![Flask](https://img.shields.io/badge/PyTorch-lightgrey?style=flat&logo=PyTorch)
![Flask](https://img.shields.io/badge/Scikit-learn-lightgrey?style=flat&logo=scikit-learn)

![Python](https://img.shields.io/badge/Language-Python-lightgrey?style=flat&logo=python)
![Flask](https://img.shields.io/badge/Language-HTML-lightgrey?style=flat&logo=html5)
![Flask](https://img.shields.io/badge/Language-CSS-lightgrey?style=flat&logo=css3)

## Execute (directly on system)

Start a Postgres database (with Docker)
```bash
docker container run -p 5433:5432 --name SeemsPhishyDB -e POSTGRES_PASSWORD=1234 postgres:12.2 
````
Execute the ``init.sql`` and ``mockup.sql`` script to populate the database (found under ``src/SeemsPhishy/db``).


Check if in line  23 in ``backend.py`` the right IP-address is used.

Install all python modules from ```requirements.txt``` (in the ```src``` folder).

Install the SeemsPhishy Module by executing the following:
```bash
python ./src/setup.py develop
```

Install the english NLP model from Spacy:
```bash
python -m spacy download en_core_web_lg
```

Starting the programming by executing the ``run.py`` script in ```./src/SeemsPhishy/gui```.

## Execute (with docker-compose)

Attention. This docker stack needs a lot of resources. 
At least 16 GB of RAM is needed and the build time is very high due to many big python modules and models.

```bash
docker compose up --build --force-recreate
```

or 

```bash
docker compose up
```

## Components

- Database
- Dataretrival
- GUI
- NLP
  - NER
  - Yake Keywords
  - TF-IDF
- Text Generation
  - E-Mail Newsletter


# Models

The developed and used text generation model can be found here: https://huggingface.co/Madhour/gpt2-eli5.