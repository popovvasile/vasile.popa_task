###Dependencies

You will need docker and docker-compose.
###Getting Started

First, clone the project.

Then install dependencies and check that it works

```bash
$ make server.install      # Install the pip dependencies on the docker container
$ make server.start        # Run the container containing your local python server
```

If everything works, you should see the available routes [here](http://127.0.0.1:3000/application/spec)..

### Challenge: User service
The objective is to implement a rest-service which is able to:

* create new user with contact data
* return user by id
* return user by name
* add additional mail/phone data
* update existing mail/phone data
* delete user

The data objects are defined as followed:
```
User:
    id: <int>
    lastName: <string>
    firstName: <string>
    emails: List<Email>
    phoneNumbers: List<PhoneNumber>

Email:
    id: <int>
    mail: <string>
    
PhoneNumber:
    id: <int>
    number: <string>
```

#### Constraints
* you provide a straight forward documentation how to build and run the service
* submitted data is stored in database (free choice which one)
* free choice of following programming languages: Scala, Java, Python


#### Bonus
* you let your service run within a container based environment (Docker, Kubernetes)
* you provide a documentation of your services API endpoints
* your service is covered with tests