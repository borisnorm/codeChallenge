#Implement a function that makes 10 http requests in parallel,
#returning the responses in the order in which the url
# are defined f([url1, url2, url3]) should return [body1, body2, body3]

#JavaScript based questions

#Array are urls, fuctions are the http requests

var asych_parallel = function(request_function, array) {
    var arg_count = array.length
    finished = 0
    returned_request =
    #request function takes in a callback, and a url
    #custom callback
    var callBack = function(value, index) {
        if finished >= arg_count:
            return returned_request
        returned_request[index] = value
   }

    for (var i = 0; i < array.length; i++) {
        request_function(array[i], callBack(i)
     }

}

