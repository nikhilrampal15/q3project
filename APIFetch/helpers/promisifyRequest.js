"use strict"
let request = require('request');

/**
 * Promisify request's get request
 * @param {String} url = url for get request
 * @return {Promise} promise
 */
function promisifyRequest(url) {
    return new Promise(function(resolve, reject) {
        request.get(url, function(error, response, body){
            if(error) {
                reject(error);
            }
            else {
                resolve(response);
            }
        });
    });
}

module.exports = promisifyRequest;
