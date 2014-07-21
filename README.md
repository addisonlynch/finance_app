Finance app
=====
Django application for managing stocks and view portfolio vs time plot
![ScreenShot1](https://dl.dropboxusercontent.com/u/20988720/CG/finance/plot.png)
![ScreenShot1](https://dl.dropboxusercontent.com/u/20988720/CG/finance/portfolio.png)

## Installation and running
```bash
git clone git@github.com:mishurov/finance_app.git
cd finance_app/source
pip install -r requirements.txt
python manage.py syncdb
python manage.py runserver
```
## Time spent
* Studying the related topic (finance, stock exchange terms). **1.5h.**
* Setting up project, databases, styles etc. **0.5h.**
* Create user registration & authentication functionality. **1.5h.**
* Make historic data download ability using Yahoo! Finance API (YQL). **1.5h.**
* Make portfolio page and get actual data using Yahoo! API for each item in portfolio. **1h.**
* Integrate 3-rd party js-application for plot, retrieve through Yahoo! API and process data for plo and table. **2.5h.**
* Final tweaks. **0.5h.**
