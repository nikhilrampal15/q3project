function House(config) {
  if(!config) {
    config = {};
  }

  this.zpid = config.zpid;
  this.address = config.address;
  this.bedrooms = config.editedFacts.bedrooms;
  this.bedrooms = config.editedFacts.bedrooms;
  this.bathrooms = config.editedFacts.bathrooms;
  this.finishedSqFt = config.editedFacts.finishedSqFt;
  this.yearBuilt = config.editedFacts.yearBuilt;
  this.parkingType = config.editedFacts.parkingType;
};

module.exports = House
