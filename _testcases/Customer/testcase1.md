# Test

Wrong URL endpoint.

# Precondition

Check the Reuse db and delete the record with the email "hello.example@domain.com" if it exists.

# Input Specification

Request:

URL: `/v1/custors`  
Body:
```
{
firstName":"Hello", 
"lastName":"Example", 
"email": "hello.example@domain.com", 
"street": "One-Way-Street", 
"streetNo": "1A" ,
"zip": "1234T"
} 
```

# Expected Outcomes

1) Response :

HTTP code : `404 Bad Request`
Body :
```
{
 "type": "ResourceNotFound",
 "code": 41001,
 "message": "Please check the resource URL , endpoints."
}
```


2) Additional check. 

# Pass/Fail Criteria

**Pass:** The request has been denied by the server.\
**Fail:** The record has been created.
