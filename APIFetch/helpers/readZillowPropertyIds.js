"use strict";
let fs = require('fs');

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

module.exports = readZillowPropertyIds;
