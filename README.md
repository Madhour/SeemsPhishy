<div align="center">
<h2>SeemsPhishy</h2>

<img src="doc/logo.png" alt="Logo" width="210" align="center"/>
<br>
<img src="https://img.shields.io/badge/postgresql-grey?style=flat-square&logo=postgresql"/>
<img src="https://img.shields.io/badge/docker-grey?style=flat-square&logo=docker"/>
<img src="https://img.shields.io/badge/flask-grey?style=flat-square&logo=flask"/>
<img src="https://img.shields.io/badge/python-grey?style=flat-square&logo=python"/>
<img src="https://img.shields.io/badge/PyTorch-grey?style=flat-square&logo=PyTorch"/>
<img src="https://img.shields.io/badge/scikit-learn-grey?style=flat-square&logo=scikit-learn"/>
<img src="https://img.shields.io/badge/bootstrap-grey?style=flat-square&logo=bootstrap"/>
<img src="https://img.shields.io/badge/html5-grey?style=flat-square&logo=html5"/>
<img src="https://img.shields.io/badge/css3-grey?style=flat-square&logo=css3"/>
</p>

---

[![GitHub issues](https://img.shields.io/github/issues/Madhour/SeemsPhishy?style=flat-square)](https://github.com/Madhour/SeemsPhishy/issues)
[![GitHub forks](https://img.shields.io/github/forks/Madhour/SeemsPhishy?style=flat-square)](https://github.com/Madhour/SeemsPhishy/network)
[![GitHub stars](https://img.shields.io/github/stars/Madhour/SeemsPhishy?style=flat-square)](https://github.com/Madhour/SeemsPhishy/stargazers)
[![GitHub license](https://img.shields.io/github/license/Madhour/SeemsPhishy?style=flat-square)](https://github.com/Madhour/SeemsPhishy/blob/main/LICENSE)

</div>


SeemsPhishy is a penetration testing toolkit for collecting data, extracting information and generating phishing emails, tailored to the target organization. 




<br>

## Execute (manually)

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

# Components

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

The developed and used text generation model can be found here: https://huggingface.co/Madhour/gpt2-eli5. For further information or reproduction, check out the used [notebook](doc/gpt2_finetuning.ipynb).