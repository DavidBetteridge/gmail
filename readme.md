# gmail example

## Overview
Google provide a rest api for sending emails,  [here](https://developers.google.com/gmail/api/v1/reference/users/messages/send) is the documentation for the api.

Previously in order to authenticate with the API you supplied your username and password.  This however is no longer recommended as it is seen as a security risk.

The documentation doesn't make it totally clear (to me anyway!) as to what the best alternative is.

Originally I tried creating a service account.  This I believe will allow you to send emails on behalf of any users in your organisation.  In my case however I only wanted to send emails on behalf of a single user and so this looked like over kill.

I also researched if google supported personal access tokens (PAT) and they don't seem to.

This left me with the option of using OAuth2.  This is bit more complicated as you need to create a web application in order for the user to approve the access.  However,  as the user was me it meant I could take a couple of "short-cuts"






## Process



## Configuration


## References