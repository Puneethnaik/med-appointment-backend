# Med Appointment Backend
This repository maintains the source of the backend system of Med Application. The frontend can be found in this [repository](https://github.com/rajedeepak/medAppointment)

# API Endpoints
1. User authorization: <br>
    url : /api/v1/api-auth-token/ <br>
    Method : POST <br>
    Request body examples: <br>
    { <br>
        "Username": Mobile UUID, <br>
        "Password": password of account in whose name the client is to be registered. <br>
    } <br>
    You have to first direct the user to register either as a doctor or as a patient… As such the POST endpoint so and so can be used. <br>
    Then after hitting the corresponding POST request, take the username and password and hit this endpoint to get access to PUT, DELETE endpoints. <br>
    Check against the response status code. If it is 200 OK then the api has succeeded, otherwise, the api has failed. The fail parsing logic is TBD. <br>
2. Where does a doctor work? <br>
    url: /api/v1/worksfor/worksfor/ <br>
    Method: GET <br>
    TODO add json response 
    Method: POST <br>
    { <br>
		"doctorId":  valid doctor Id , <br>
		"hospitalId":  valid hospital Id , <br>
	} <br>
    <br>
    url: /api/v1/worksfor/worksfor/1/ <br>
    Method: GET, PUT, DELETE <br>
    Request body examples: <br>
    {<br>
		“doctorId”: valid doctor Id, <br>
		“hospitalId”: valid hospital Id, <br>
	}<br>
    Example endpoints: /api/v1/worksfor/worksfor/1/(Don't forget the end slash after the pk, it is important to give otherwise there will be 500 ISE)<br>
4. Where is my appointment? <br>
    description: Get All Appointments <br>
    url: /api/v1/appointment/appointment/ <br>
    Method: GET, POST <br>
    Request Body Examples: <br>
    { <br>
        “doctorId”: valid doctor Id, <br>
		“hospitalId”: valid hospital Id, <br>
        “start”: time in following format: 11-04-2020 18:03:54, or 25-03-2014 03:02:00, etc <br>
        “end”: time in following format: 11-04-2020 18:03:54, or 25-03-2014 03:02:00, etc <br>
    } <br>
    <br>
    description: Get, Update, Delete appointment by appointment id <br>
    url: appointment/appointment/1/ <br>
    Method: GET, PUT, DELETE <br>
    Request Body Examples: <br>
    { <br>
        “doctorId”: valid doctor Id, <br>
		“hospitalId”: valid hospital Id, <br>
        “start”: time in following format: 11-04-2020 18:03:54, or 25-03-2014 03:02:00, etc <br>
        “end”: time in following format: 11-04-2020 18:03:54, or 25-03-2014 03:02:00, etc <br>
    } <br>,
    <br>
    description: Get Appointments of a doctor,<br>
    url: appointment/doctor/1/<br>
    Method: GET<br>
    <br>
    description: Get Appointments in a Hospital <br>
    url: appointment/hospital/1/ <br>
    Method: GET <br>


The backend system can be accessible [here](https://backend14557.herokuapp.com/)




