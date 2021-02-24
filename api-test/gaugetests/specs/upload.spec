# Upload request

This test specification demonstrates how our current integration tests for the Graph API can be realized using Gauge.

The following are global steps that will always be executed before every single test case:

* Set API version to "b1"

## Create a request to upload a new image

When a POST request is made to a url with valid image file, a new image is uploaded successfully. 

* Create request to "/Stage/image"
* Send "POST" request with file from <file:images/POST.jpg>
* Assert that response status code is "201"
* Assert that response body is not empty


## Create a request with invalid url

When a POST request is made to a url with valid image file, a new image is uploaded successfully. 

* Create request to "/Stge/image"
* Send "POST" request with file from <file:images/POST.jpg>
* Assert that response status code is "400"
* Assert that response body is not empty
