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



## References

https://developers.google.com/identity/protocols/oauth2/web-server