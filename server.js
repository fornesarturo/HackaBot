// =============================================================================
// BASIC CONFIGURATION
var express = require('express');
var server = express();
var bodyParser = require('body-parser');

server.use(bodyParser.urlencoded({extended: true}));
server.use(bodyParser.json());

//var port = process.env.PORT || 8080;
var port = 8080;
var router = express.Router();
// =============================================================================

// =============================================================================
// DATABASE
var mongoose = require('mongoose');

mongoose.Promise = global.Promise;
mongoose.connect('mongodb://localhost:27017/hackabot');
// =============================================================================

// =============================================================================
// HEADERS
server.use(function(req, res, next) {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
  res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
  next();
});
// =============================================================================

// =============================================================================
// API ROUTES
var routes = [
    require('./app/routes/ine'),
    require('./app/routes/message')
];
// =============================================================================

// =============================================================================
// SERVER
server.use('/api', routes);
server.listen(port);
console.log('Magic happens on port ' + port);
// =============================================================================
