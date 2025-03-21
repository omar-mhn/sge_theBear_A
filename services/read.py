from schema import read_sch

def registre():
    users = {
        "user1":{
            "id":1,
            "name":"Roger",
            "surname":"Sobrino",
            "age":49
        },
        "user2":{
            "id":2,
            "name":"Josep Oriol",
            "surname":"Roca",
            "age":23
        },
        "user3":{
            "id":3,
            "name":"Juan Manuel",
            "surname":"sanchez",
            "age":40
        },
        "user4":{
            "id":4,
            "name":"Juan Carlos",
            "surname":"Garcia",
            "age":30
        },
        "user5":{
            "id":5,
            "name":"Ken Ryuga",
            "surname":"Kamau",
            "age":22
        },
        "user6":{
            "id":6,
            "name":"Kyle",
            "surname":"Kim",
            "age":23
        }
    }
    return read_sch.schemas(users)