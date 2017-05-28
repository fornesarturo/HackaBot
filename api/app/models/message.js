var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var MessageSchema = new Schema({
    timestamp: {type: Number, required: true},
    messageText: {type: String, required: true},
    user: {type: String, required: true}
});

module.exports = mongoose.model('Message', MessageSchema);
