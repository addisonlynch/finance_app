Finance app
=====
Django application for managing stocks and view portfolio vs time plot
![ScreenShot1](http://mishurov.5gbfree.com/github/finance/plot.png)
![ScreenShot1](http://mishurov.5gbfree.com/github/finance/portfolio.png)

## Installation and running
```bash
git clone git@github.com:mishurov/finance_app.git
cd finance_app
pip install -r requirements.txt
python manage.py syncdb
python manage.py runserver
```
## Stages
* Studying the related topic (finance, stock exchange terms).
* Setting up project, databases, styles etc.
* Create user registration & authentication functionality.
* Make historic data download ability using Yahoo! Finance API (YQL).
* Make portfolio page and get actual data using Yahoo! API for each item in portfolio.
* Integrate 3-rd party js-application for plot, retrieve through Yahoo! API and process data for plo and table.
* Final tweaks.
