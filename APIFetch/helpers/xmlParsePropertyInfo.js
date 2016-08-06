"use strict";
let fs = require('fs');
let xml2js = require('xml2js');
let House = require('../models/house');

/**
 * Parse xml file to JS object using xml2js module
 * @param {Array} files, each element is xml document in string format
 * @return N/A
 */
function xmlParsePropertyInfo(files, city) {
    let header = "ZPID"+"," +"Bedroom"+","+ "Bathroom"+","+ "SqFt"+","+ "YearBuilt"+"," +"Parking"+ "\n";
    fs.writeFile(`../data/houseInfo/${city}_propertyinfo.csv`, header, function(err) {
        if(err) console.log(`Error during writing to ${city}.csv`);
    });
    files.forEach(function(file) {
        let parser = new xml2js.Parser();
        fs.readFile(file, function(err, data) {
            console.log("Processing: " + file);
            parser.parseString(data, function (err, result) {
                if(!result["UpdatedPropertyDetails:updatedPropertyDetails"].response) return;
                let request = result["UpdatedPropertyDetails:updatedPropertyDetails"].request[0];
                // console.log(request)
                let message = result["UpdatedPropertyDetails:updatedPropertyDetails"].message[0];
                // console.log(message)
                let response = result["UpdatedPropertyDetails:updatedPropertyDetails"].response[0];
                // console.log(response);
                let house = new House(response);
                // console.log(house);
                let zpid = response.zpid[0];

                let info = house.zpid+"," +house.bedrooms+","+ house.bathrooms+","+ house.sqFt+","+ house.yearBuilt+"," +house.parkingType+ "\n";
                fs.writeFile(`../data/houseInfo/${city}_propertyinfo.csv`, info, {'flag':'a'});
            });
        });
        parser.reset();
    });
    return;
}

module.exports = xmlParsePropertyInfo;
