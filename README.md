First user send request like signup or login. The request first goes to main.py which connect all the routes and send request to the correct file. If user is doing signup then auth_routes.py handle that request and user data is saved in database with help of models.py. The database connection is handled in database.py. Password is not saved in simple text, it is hashed for little security. The request and response format is defined in schemas.py.

When user login, the system check email and password. If they are correct then a JWT token is created. This token is used to access protected routes. When a protected route is called the system check the token first, if token is valid then request is allowed otherwise it return error.

There is also a route in llm_routes.py where user can send a prompt. The backend send this prompt to Google Gemini API and get response from it. Then that response is returned back to the user. So different files are doing different work and together they run the whole application.

