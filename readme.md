# gmail example

## Overview
Google provide a rest api for sending emails,  [here](https://developers.google.com/gmail/api/v1/reference/users/messages/send) is the documentation for the api.

Previously in order to authenticate with the API you supplied your username and password.  This however is no longer recommended as it is seen as a security risk.

The documentation doesn't make it totally clear (to me anyway!) as to what the best alternative is.

Originally I tried creating a service account.  This I believe will allow you to send emails on behalf of any user in your organisation.  In my case however I only wanted to send emails on behalf of a single user and so this looked like over kill.

I also researched if google supported personal access tokens (PAT) and they don't seem to.

This left me with the option of using OAuth2.  This is bit more complicated as you need to create a web application in order for the user to approve the access.  However,  as the user was me it meant I could take a couple of "short-cuts"


## Configuration in the Google Cloud Console

1. Setup a new project in google

* Open the API Library in the [Google API Console](https://console.cloud.google.com/apis/library)
* If prompted, select a project, or create a new one.
* The API Library lists all available APIs.  Search for and enable the Gmail API.

2. Setup up the credentails

* Go to the Credentials page.
* Click Create credentials > OAuth client ID.
* Select the Web application application type.
* Fill in the form and click Create. For the Authorised Redirect URIs, enter `https://localhost:9000/oauth2callback`  (I had more success with https rather than http)
* Download the `client_secret.json` file and place it in the same directory as this file.  (DO NOT ADD THE FILE TO GIT!)

3. Add test users.  
As we aren't going to publish the application,  we need to explicitly specify the users who can access.  In our case it's the user we want to send the emails on behalf of.
* Go to the OAuth consent screen page.
* Click + ADD USERS and add your user.  e.g.  example@gmail.com


## Flask Application
* Open a shell prompt and navigate into the same folder as this file.  Then run the following
commands to create a virtual environment and install the required packages.

```shell
pip install virtualenv 

virtualenv venv

venv\Scripts\activate

venv\Scripts\python.exe -m pip install --upgrade pip

pip install -r requirements.txt
```

* Once the packages have been installed, run `setup.py`

* This will start the flask web server running which you can access on https://localhost:9000

* Open the site in a browser,  and ignore the certificate warning.  This is because we are running on a local machine with a self-signed certificate.  (DO NOT DO THIS IF YOU DEPLOY THIS SITE IN THE REAL WORLD!) 


## Getting user consent

* From the web page select the "Test the auth flow directly" option.

* This should take you to a page where you can select the user you want to send the email on behalf of.

* The following page will give a warning as the application hasn't been verified by google.  Again we can ignore this as we aren't going to deploy this application.  Click continue.

* Google will then warn you what permissions you are granting.  In our case the ability to send an email.  Click Continue.

* If successful this should have done two things.

1. Sent an test email from you to the email address specified on line 50.  (example@gmail.com)

2. Created a file in this folder called `persisted_credentials.json`  (DO NOT ADD THIS FILE TO GIT)


## Sending emails

If everything has been correctly configured then the file `send_email_test.py` can be used to send emails.  

* On line 33 onwards enter the details of your test message.

* Run the file.


## Persisted_credentials.json

Currently we are using the token for calling the API in a file.  This might be better written to the database.  When the token expires it will be automatically refreshed.  The database will then have to be updated with the new token.








## References

https://developers.google.com/identity/protocols/oauth2/web-server