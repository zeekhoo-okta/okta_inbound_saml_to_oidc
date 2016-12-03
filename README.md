Note. Runs on Python 2.7+

### Setup

1. Clone repository
2. Create virtual environment
>>`virtualenv venv`
3. Activate virtualenv
>>`source venv/bin/activate`
4. Install requirements
>>`pip install -r requirements.txt`
5. Edit the .env file
>>`OKTA_ORG=<the domain of your Okta org> eg: dev-61689.okta.com`
>>`CLIENT_ID=<client id of the OpenID Connect app you registered in Okta>`
>>`REDIRECT_URI=<where you want the id_token/access_token to be returned>`
6. Start the server
>>`python manage.py runserver`

###_Test it out:_
Point your browser to 
`http://localhost:8000`