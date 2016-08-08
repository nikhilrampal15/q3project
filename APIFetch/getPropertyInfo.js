"use strict"
require('dotenv').load();
let request = require('request');
let fs = require('fs');

// Helper Functions in APIFetch/helpers
let promisifyRequest = require('./helpers/promisifyRequest');
let readZillowPropertyIds = require('./helpers/readZillowPropertyIds');
let xmlParsePropertyInfo = require('./helpers/xmlParsePropertyInfo');

/***************************************************************
 * Main - runs the program
 * 1. Change city
 * 2. Create new directory to save files: /data/propertyInfo/${city}`

 @ Note - check /data/propertyInfo/${city} file. If there is an error msg,
 such as "Error: this account has reached is maximum number of calls for today"
 the result file won't be correct.

 @ result: ${city}_propertyinfo.csv file in data/houseInfo directory
*****************************************************************/
let city = 'palo-alto-ca';
let zpidFile = `../data/zpid/${city}.txt`
let zpids = readZillowPropertyIds(zpidFile)
// zpids = zpids.slice(0, 2)
callGetUpdatedPropertyDetailsAPI(zpids);

let dir = `../data/propertyInfo/${city}`;
let files = [];
fs.readdirSync(dir).forEach(function(file) {
    files.push(`${dir}/${file}`);
})
xmlParsePropertyInfo(files, city);

/**
 * Call Zillow's GetUpdatedPropertyDetails API
 * @param {Number} zpid = Zillow Property ID
 * Data is written to a file in data/propertyInfo directory
 * @return N/A.
 */
function callGetUpdatedPropertyDetailsAPI(zpid) {
    let zillowApiCalls = []
    for(let i = 0; i < zpids.length - 1; i++) {
        let zpid = zpids[i];
        let url = `http://www.zillow.com/webservice/GetUpdatedPropertyDetails.htm?zws-id=${process.env.ZWSID}&zpid=${zpid}`;

        zillowApiCalls.push(promisifyRequest(url));
    }

    Promise.all(zillowApiCalls)
    .then( (data) => {
        let allProperties = [];
        for(let i = 0; i < data.length; i++) {
            let xml = data[i].body;
            fs.writeFile(`../data/propertyInfo/${city}/${city}_${i}`, xml, function(err) {
                if(err) console.log(err)
            });
        }
    });

    return;
}
