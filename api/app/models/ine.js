var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var IneSchema = new Schema({
    fName: {type: String, required: true},
    mName: {type: String, required: true},
    lName: {type: String, required: false},
    address: {type: String, required: false},
    ineID: {type: String, required: true},
    curp: {type: String, required: true},
    user: {type: String, required: true}
});

module.exports = mongoose.model('Ine', IneSchema);
