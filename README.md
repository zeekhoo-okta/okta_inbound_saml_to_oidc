Note. Runs on Python 2.7+

### Setup

* Clone repository
* Create virtual environment
```
virtualenv venv
```
* Activate virtualenv
```
source venv/bin/activate
```
* Install requirements
```
pip install -r requirements.txt
```
* Edit the .env file
```
OKTA_ORG=<the domain of your Okta org> eg: dev-61689.okta.com

CLIENT_ID=<client id of the OpenID Connect app you registered in Okta>

REDIRECT_URI=<where you want the id_token/access_token to be returned>
```
* Start the server
```
python manage.py runserver
```

###_Test it out:_
Point your browser to 
`http://localhost:8000`