# elevator-system
RESTful API for an elevator system

Components

The project has two components or files - the first is the Elevator.py which is a class representing the elevator. The second is run.py which contains the logic and API endpoints.

Endpoints

GET /elevator - Gets information of all the elevators

Response

{
  "Data": [
    {
      "currentFloor": 2,
      "direction": 1,
      "finalFloor": 5,
      "floorRequests": [
        2,
        3,
        5
      ],
      "id": 0
    },
    {
      "currentFloor": 0,
      "direction": 1,
      "finalFloor": 5,
      "floorRequests": [
        0,
        5
      ],
      "id": 3
    }
  ]
}

GET /elevator/{elevatorId}/status - Gets the information for a particular elevator

Response - 

{
  "Data": {
    "currentFloor": 5,
    "direction": -1,
    "finalFloor": 1,
    "floorRequests": [
      -5,
      -1
    ],
    "id": 3
  }
}

PUT /elevator/{elevatorId}/stop - Endpoint to stop a particular elevator

Response -

{
  "Message" : "elevator stopped"
}

PUT /elevator/{elevatorId}/goto - This endpoint is called when a user presses a button inside an elevator to go to a particular floor

Request - 

{"currentFloor":0,
"finalFloor":5}

Response - 

{
  "Data": {
    "currentFloor": 0,
    "direction": 1,
    "finalFloor": 5,
    "floorRequests": [
      0,
      5
    ],
    "id": 3
  }
}

PUT /elevator/{elevatorId}/state - This endpoint is used to set the status of an elevator

Request - 

{"currentFloor":1,"finalFloor":10,"direction":1,"floorRequests":[1,2,3,10]}

Response - 

{
  "Data": {
    "currentFloor": 1,
    "direction": 1,
    "finalFloor": 10,
    "floorRequests": [
      1,
      2,
      3,
      10
    ],
    "id": 2
  }
}

POST /building - This endpoint is called when a user calls an elevator at any floor. Returns id of the elevator as response

Request - 

"{"currentFloor":1,"direction":1}"

Response - 

{
  "id": 0
}
