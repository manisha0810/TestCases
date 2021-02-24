# Upload Request

When a POST request is made to a url along with a valid image file, a new record is uploaded successfully. 

* Send "POST" request to "/Stage/image" with body from <file:fixtures/checks/createCheck.json>
* Assert that response status code is "201" 
* Assert that response body contains <file:fixtures/checks/createCheck.json> with "number,payeeAddress" included


## Display number of items
* Add task "first task"
* Must display "1 item left"
* Add task "second task"
* Must display "2 items left"

## Must list only active tasks
* Add tasks 

   |description|
   |-----------|
   |first task |
   |second task|
   |third task |
   |fourth task|
   |fifth task |

* Complete tasks 

   |description|
   |-----------|
   |second task|
   |fifth task |
* View "Active" tasks
* Must have 

   |description|
   |-----------|
   |first task |
   |third task |
   |fourth task|
* Must not have 

   |description|
   |-----------|
   |second task|
   |fifth task |

A tear down step for every scenario
___
* Clear all tasks
