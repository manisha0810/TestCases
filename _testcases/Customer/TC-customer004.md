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
