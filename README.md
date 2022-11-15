# Django Template
## Setup
After creating your project, some additional configuration is required to allow the project to run in Gitpod.

1. Install the [`django-cors-headers`](https://pypi.org/project/django-cors-headers/) package and follow the Setup instructions in the README.

1. Add the following to the project's `settings.py`:
    ```
    CSRF_TRUSTED_ORIGINS = ['https://*.gitpod.io']
    CORS_ALLOWED_ORIGIN_REGEXES = [
        r"^https://.*\.gitpod\.io$",
    ]
    ```

----    
# Django Jams
----
This is a project with the goal of creating the back-end of a music-streaming app by using REST api 
while adding Create, Read, Update, and Delete functionality to the app the goal of it being a functional 
app in the back end.

![image](https://user-images.githubusercontent.com/111811657/202031854-bdf6b819-fc29-439b-95a6-febb34fcabe8.png)
