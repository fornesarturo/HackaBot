var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var UserSchema = new Schema({
    name: {type: String, required: true},
    gender: {type: String, required: false},
    facebookID: {type: String, required: true}
});

module.exports = mongoose.model('User', UserSchema);
