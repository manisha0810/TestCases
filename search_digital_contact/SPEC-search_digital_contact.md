# Specification

## Overview

| | |
|------|-------|
| **Use Case Name** | Update Digital Contact |
| **Description** | Calling this endpoint changes 1-n field values in the existing customer record in the database, etc. | 
| **Prerequisites** | none | 
| **Base URL** | (standard HTTP) |
| **Endpoint** | /{customerId} |
| **Method** | PUT |
| **Body** | A customer data object (see [Body Details](#Body-Details) ) | 

## Body Details
```
email=[String]
Format Value: must include -> only one @  and  “.string”, for example .com, .org, .de  (Separate data validation task)

firstName=[String]

lastName=[String] 

street=[String]
streetNo=[String]

zip=[String]

city=[String]

phone=[String]
```

Missing optional fields indicate, that the particular property will be deleted on server.


## Responses

### Success Response : (only Json)
```
HTTP Code : 201
Content : The customer record successfully updated

Must contain the UID and all customer details for verification by the user.
```

### Error Response

see https://github.wdf.sap.corp/c4reuse/doc/blob/master/feature/error_codes
