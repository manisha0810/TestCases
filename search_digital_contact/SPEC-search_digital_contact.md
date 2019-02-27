# Specification

## Overview

| | |
|------|-------|
| **Use Case Name** | Search Digital Contact |
| **Description** | Calling this endpoint list all records on the basis of search parameters (e.g. BP id, email Id, phone number, address etc. ) stored in the database.  |
| **Prerequisites** | none | 
| **Base URL** | http://35.195.178.198/v1/customers |
| **Endpoint** | /{customer?} |
| **Method** | GET |
| **Body** | none | 

## Responses

### Success Response : (only Json)
```
HTTP Code : 200
Content : The customer record is successfully exposed.

Must contain the UID and all customer details for verification by the user.
```

### Error Response

see https://github.wdf.sap.corp/c4reuse/doc/tree/master/feature/error_codes 
