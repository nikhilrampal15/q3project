"use strict";
let fs = require('fs');
let xml2js = require('xml2js');
let House = require('../models/house');

/**
 * Parse xml file to JS object using xml2js module
 * @param {Array} files, each element is xml document in string format
 * @return N/A
 */
function xmlParseZestimate(files, city) {
    let header = "ZPID"+"," +"Zestimate"+","+ "Street"+","+ "City"+","+ "State"+"," +"Zipcode"+ "\n";
    fs.writeFile(`../data/houseInfo/${city}_zestimate.csv`, header, function(err) {
        if(err) console.log(`Error during writing to ${city}.csv`);
    });
    files.forEach(function(file) {
        let parser = new xml2js.Parser();
        fs.readFile(file, function(err, data) {
            console.log("Processing: " + file);
            parser.parseString(data, function (err, result) {
                // let message = result["Zestimate:zestimate"].message[0];
                // console.log(message)
                if(!result["Zestimate:zestimate"].response) return;
                let response = result["Zestimate:zestimate"].response[0];
                // console.log(response);
                let house = new House(response);
                // console.log(house);
                let zpid = response.zpid[0];

                let info = house.zpid+"," +house.zestimate.amount[0]["_"]+","+ house.address.street[0]+","+ house.address.city[0]+","+ house.address.state[0]+"," +house.address.zipcode[0]+ "\n";
                fs.writeFile(`../data/houseInfo/${city}_zestimate.csv`, info, {'flag':'a'});
            });
        });
        parser.reset();
    });
    return;
}

module.exports = xmlParseZestimate;
