"use strict"
let request = require('request');
let fs = require('fs')
let parseString = require('xml2js').parseString;
let House = require('../models/house')

let ZWSID = "X1-ZWz1fbxzh1icjv_a2eph"
// let zpid = 48749425
let zpidFile = '../data/soma-san-francisco-ca.txt'
let zpids = readZillowPropertyIds()

let zillowApiCalls = []
for(let i = 0; i < zpids.length - 1; i++) {
    zillowApiCalls.push(getZillowData(zpids[i]));
}

Promise.all(zillowApiCalls.slice(0, 1))
.then( (data) => {
    let allProperties = [];
    console.log(data)
    console.log(data.length)
    fs.writeFileSync('message.txt', data);
    // for(let i = 0; i < data.length; i++) {
    //     console.log(i)
    //     let xml = data[i].body
    //     // console.log(xml)
    //     parseString(xml, function (err, result) {
    //         let propertyInfo = result["UpdatedPropertyDetails:updatedPropertyDetails"].response[0];
    //         console.log(propertyInfo)
    //         allProperties.push(new House(propertyInfo));
    //     });
    // }
    // console.log(allProperties)
})


function readZillowPropertyIds(){
    let data = fs.readFileSync(zpidFile, 'utf8');
    let zpids = data.split("\n");
    return zpids;
}

function getZillowData(zpid) {
    let url = `http://www.zillow.com/webservice/GetUpdatedPropertyDetails.htm?zws-id=${ZWSID}&zpid=${zpid}`
    return promisifyGet(url);
}

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


module.exports = getZillowData
