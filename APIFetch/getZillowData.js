"use strict"
let request = require('request');
let fs = require('fs');

/**
 * Main - runs the program
 * @ change city for different cities
 */
let city = 'palo-alto-ca';
let zpidFile = `../data/zpid/${city}.txt`
let zpids = readZillowPropertyIds(zpidFile)
let ZWSID = "X1-ZWz1fbxzh1icjv_a2eph"

let zillowApiCalls = []
for(let i = 0; i < zpids.length - 1; i++) {
    zillowApiCalls.push(getZillowData(zpids[i]));
}

Promise.all(zillowApiCalls.slice(0, 2))
// Promise.all(zillowApiCalls)
.then( (data) => {
    let allProperties = [];
    for(let i = 0; i < data.length; i++) {
        let xml = data[i].body;
        fs.writeFile(`../data/propertyInfo/${city}_${i}`, xml, function(err) {
            if(err) console.log(err)
        });
    }
})

/**
 * Read file and return zpids
 * @param {String} fname - input filename
 * @return {Array} zpids - array of Zillow Property IDs
 */
function readZillowPropertyIds(fname){
    let data = fs.readFileSync(fname, 'utf8');
    let zpids = data.split("\n");
    return zpids;
}

/**
 * Create promise of request
 * @param {Number} zpid = Zillow Property ID
 * @return {Promise} promise
 */
function getZillowData(zpid) {
    let url = `http://www.zillow.com/webservice/GetUpdatedPropertyDetails.htm?zws-id=${ZWSID}&zpid=${zpid}`
    // let url = `http://www.zillow.com/webservice/GetUpdatedPropertyDetails.htm?zws-id=X1-ZWz1fbxzh1icjv_a2eph&zpid=48749425`
    return promisifyGet(url);
}

/**
 * Promisify request's get request
 * @param {String} url = url for get request
 * @return {Promise} promise
 */
function promisifyGet(url) {
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
