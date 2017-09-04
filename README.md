# codecollab

A web based interface which let's a user[0] upload code[1] and enables another assigned collaborators[2] to review your code. after a user logs-in he get's a button which let him upload his code file,  and as soon as the code get's uploaded, site admin[3] can assign any collaborator(s). once the collaborators receives a request to review code, he can make multiple comments[4] by pointing out the lines(?) and after he is done, he can click finish.

# Definition

0. user - a user is someone who is seeking review to his code, he can upload multiple code.
1. code - code is the fundamental object in this app, which can only be created by a user. it have a heading, a file which contains code, and a small description.
2. collaborator - a user can be a collaborator but not all users are collaborators.
 a collaborator can do all the function that a user does, but can have a read-only access to any code, where he can add comments, and do reviewing process.
3. admin - a admin have a power to.
      a. assign or revoke code review to any user who is not author of the code.
      b. delete the code, or user.
      c. have access to view all the users and their code.
4. comment - a comment can be added on any code by a user who is an author of the code or someone who had been assigned to.

# Basic Flow

1. user upload the code.
2. admin assigns the reviewer for the code
3. reviewer reviews the code.
4. fin.

# Database design

![ERM](http://i.imgur.com/XDZHSMD.png)
