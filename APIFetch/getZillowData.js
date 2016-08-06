"use strict"
require('dotenv').load();
let request = require('request');
let fs = require('fs');

/**
 * Main - runs the program
 * @ change city for different cities
 */
let city = 'san-francisco-ca';
let zpidFile = `../data/zpid/${city}.txt`
let zpids = readZillowPropertyIds(zpidFile)

// zpids = zpids.slice(0, 3);
getZestimateAPI(zpids);
// getUpdatedPropertyDetailsAPI(zpids);

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
 * Call Zillow's GetUpdatedPropertyDetails API
 * @param {Number} zpid = Zillow Property ID
 * Data is written to a file in data/propertyInfo directory
 * @return N/A.
 */
function getUpdatedPropertyDetailsAPI(zpid) {
    let zillowApiCalls = []
    for(let i = 0; i < zpids.length - 1; i++) {
        let zpid = zpids[i];
        let url = `http://www.zillow.com/webservice/GetUpdatedPropertyDetails.htm?zws-id=${process.env.ZWSID}&zpid=${zpid}`;

        zillowApiCalls.push(promisifyGet(url));
    }

    Promise.all(zillowApiCalls)
    .then( (data) => {
        let allProperties = [];
        for(let i = 0; i < data.length; i++) {
            let xml = data[i].body;
            fs.writeFile(`../data/propertyInfo/${city}_${i}`, xml, function(err) {
                if(err) console.log(err)
            });
        }
    });

    return;
}

/**
 * Call Zillow's GetZestimate API
 * @param {Array} zpids = array of Zillow Property IDs
  * Data is written to a file in data/zestimate directory
 * @return N/A
 */
function getZestimateAPI(zpids) {
    let zillowApiCalls = []
    for(let i = 0; i < zpids.length - 1; i++) {
        let zpid = zpids[i];
        let url = `http://www.zillow.com/webservice/GetZestimate.htm?zws-id=${process.env.ZWSID}&zpid=${zpid}`;

        zillowApiCalls.push(promisifyGet(url));
    }

    Promise.all(zillowApiCalls)
    .then( (data) => {
        let allProperties = [];
        for(let i = 0; i < data.length; i++) {
            let xml = data[i].body;
            fs.writeFile(`../data/zestimate/${city}_${i}`, xml, function(err) {
                if(err) console.log(err)
            });
        }
    });

    return;
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
