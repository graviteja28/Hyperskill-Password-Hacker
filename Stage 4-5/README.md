## Objectives
Your algorithm is the following:

1. Try all logins with an empty password.
2. When you find the login, try out every possible password of length 1.
3. When an exception occurs, you know that you found the first letter of the password.
4. Use the found login and the found letter to find the second letter of the password.
5. Repeat until you receive the ‘success’ message.

Finally, your program should print the combination of login and password in JSON format. The examples show two ways of what the output can look like. See the hint to find out how to convert a dict object into a JSON string.
