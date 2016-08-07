function House(config) {
  if(!config) {
    config = {};
  }

  this.zpid = config.zpid[0] || null;
  this.address = config.address ? config.address[0] : null;
  this.zestimate = config.zestimate ? config.zestimate[0] : null;
  this.bedrooms = config.editedFacts ? config.editedFacts.bedrooms: null;
  this.bathrooms = config.editedFacts ? config.editedFacts.bathrooms: null;
  this.sqFt = config.editedFacts ? config.editedFacts.finishedSqFt: null;
  this.yearBuilt = config.editedFacts ? config.editedFacts.yearBuilt: null;
  this.parkingType = config.editedFacts ? config.editedFacts.parkingType: null;
}

module.exports = House;
