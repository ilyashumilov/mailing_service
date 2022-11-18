<h1 align="center">Mailing system</h1>

[Click “Watch” in this repository](https://help.github.com/en/github/receiving-notifications-about-activity-on-github/watching-and-unwatching-repositories) to keep track of the latest changes in the project.

Please read through our [Contribution Guidelines](CONTRIBUTING.md), [Architecture Overview](ARCHITECTURE.md) and [Installation Instructions](INSTALL.md).

The repository is a part of the [fabrique](https://fabrique.studio). This project and everyone participating in it is governed by the [Code of Conduct](CODE_OF_CONDUCT.md).


## Overview

The system consists pf three microservices:
- `api` microservice, responsible for api calls handling
- `sender` microservice, responsible for sending messages of each mailing
- `mail_sender` microservice, responsible for sending reports periodically to the mail


## API calls


### Create new Mailing instance `mailing/`

Method: `POST`

```
curl -XPOST
-H "Content-Type: application/json"
-d     "{
        "id": 17,
        "start": "2022-11-17T18:30:59Z",
        "text": "text",
        "client_property": {
            "operator_code": "0"
        },
        "end": "2022-11-17T19:55:59Z",
        "current_status": "Processed"
    }"
"<hostname>/api/v1/mailing"

```

Response:

```
{
    "message": "The new Mailing instance has been created"
}
```

### Retrieve all Area's instances `mailing/`

Метод: `GET`

```
curl -XGET
-H "Content-Type: application/json"
"<hostname>/api/v1/mailing"

```

Response:

```
[
    {
        "id": 14,
        "start": "2022-11-17T18:30:59Z",
        "text": "text",
        "client_property": {
            "operator_code": "0"
        },
        "end": "2022-11-17T19:50:59Z",
        "current_status": "Processed"
    },
    {
        "id": 17,
        "start": "2022-11-17T18:30:59Z",
        "text": "text",
        "client_property": {
            "operator_code": "0"
        },
        "end": "2022-11-17T19:55:59Z",
        "current_status": "Processed"
    }
]
```

### Delete Mailing instance `mailing/?id=instance's id`

Method: `DELETE`

```
curl -XDELETE
-H "Content-Type: application/json"
"<hostname>/api/v1/mailing/?id=instance's id"

```

Response:

```
{
    "message": "The Mailing instance with id 4 has been deleted"
}
```


### Create new Client instance `client/`

Method: `POST`

```
curl -XPOST
-H "Content-Type: application/json"
-d "{"name":"curator's name", "area_id":"Curator's area's id"}"
"<hostname>/api/v1/client"

```

Response:

```
{
    "message": "The new Client instance has been created"
}
```

### Retrieve all Client's instances `client/`

Метод: `GET`

```
curl -XGET
-H "Content-Type: application/json"
"<hostname>/api/v1/client"

```

Response:

```
[
    {
        "id": 1,
        "phone_number": "test",
        "operator_code": "0",
        "tag": "tag",
        "timezone": "UTC"
    },
    {
        "id": 3,
        "phone_number": "test",
        "operator_code": "0",
        "tag": "1",
        "timezone": "UTC"
    }
]
```
### Delete Client instance `client/?id=instance's id`

Method: `DELETE`

```
curl -XDELETE
-H "Content-Type: application/json"
"<hostname>/api/v1/client/?id=instance's id"

```

Response:

```
{
    "message": "The Client instance with id 4 has been deleted"
}
```





### Retrieve general statistics about each mailing with amounts of messages sent and not sent `general_stat/`

Method: `GET`

```
curl -XGET
-H "Content-Type: application/json"
"<hostname>/api/v1/general_stat/"
```

Response:

```
[
    {
        "id": 3,
        "start": "2022-12-18T14:30:59Z",
        "text": "new",
        "client_property": {
            "tag": "15"
        },
        "end": "2022-11-19T14:30:59Z",
        "messages_sent": "1",
        "messages_not_sent": "0"
    },
[
```

### Retrieve statistics about particular mailing with that's messages `exact_stat/`

Method: `GET`

```
curl -XGET
-H "Content-Type: application/json"
"<hostname>/api/v1/exact_stat/"
```

Response:

```
{
    "mailing": {
        "id": 3,
        "start": "2022-12-18T14:30:59Z",
        "text": "new",
        "client_property": {
            "tag": "15"
        },
        "end": "2022-11-19T14:30:59Z"
    },
    "messages": [
        {
            "sent": "2022-11-17T14:17:10Z",
            "status": "Sent"
        }
    ]
}
```
