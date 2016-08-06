"use strict";
let fs = require('fs');
let xml2js = require('xml2js');
let House = require('./models/house');

/**
 * Main - runs the program
 */
let dir = '../data/propertyInfo';
let files = [];
fs.readdirSync(dir).forEach(function(file) {
    files.push(`${dir}/${file}`);
})
xmlParse(files);

/**
 * Parse xml file to JS object using xml2js module
 * @param {Array} files, each element is xml document in string format
 * @return N/A
 */
function xmlParse(files) {
    let allHouses = [];
    files.forEach(function(file) {
        let parser = new xml2js.Parser();
        fs.readFile(file, function(err, data) {
            parser.parseString(data, function (err, result) {
                let request = result["UpdatedPropertyDetails:updatedPropertyDetails"].request[0];
                console.log(request)
                let message = result["UpdatedPropertyDetails:updatedPropertyDetails"].message[0];
                console.log(message)
                // let response = result["UpdatedPropertyDetails:updatedPropertyDetails"].response[0];
                // console.log(response);
                // allHouses.push(new House(response));
            });
        });
        parser.reset();
    });
    return;
}
