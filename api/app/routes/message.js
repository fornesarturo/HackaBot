var Message = require('../models/message');
var User = require('../models/user');
var express = require('express');
var router = express.Router();

//var packet;

router.route('/message')
    .post(function(req, res) {
        var packet = req.body;
        function callback(data) {
            if (data) {
                delete packet['name'];
                delete packet['gender'];
                delete packet['facebookID'];
                packet['user'] = data;
                var newMessage = new Message(packet);
                newMessage.save(function(err) {
                    if (err) {
                        console.log("ERROR: " + err);
                    }
                    console.log("POST IN MESSAGE");
                });
            }
            res.send({'code': 1, 'data': packet});
        }

        User.findOne({'facebookID': packet['facebookID']}, function(err, user) {
            if (err) {
                console.log("ERROR: " + err);
                res.send(err);
                return;
            }
            if (user) { // If user exists in collection, don't add it again
                var userID = user['_id'].toString();
                callback(userID);
            }
            else {
                var userJSON = {
                    'name': packet['name'],
                    'gender': packet['gender'],
                    'facebookID': packet['facebookID']
                }
                var newUser = new User(userJSON);
                newUser.save(function(err) {
                    if (err) {
                        console.log("ERROR: " + err);
                        return;
                    }
                    var userID = newUser['_id'].toString();
                    callback(userID);
                });
            }
        })
    })

router.route('/message/:facebookID')
    .get(function(req, res) {
        function callback(data) {
            console.log("GET IN MESSAGE");
            res.send({'code': 1, 'message': data});
        }

        User.findOne({'facebookID': req.params.facebookID}, function(err, user) {
            if (err) {
                console.log("ERROR: " + err);
                return;
            }
            Message.find({'user': user['_id'].toString()}).sort('-timestamp').exec(function(err, messages) {
                callback(messages[0]);
            });
        })
    })
    
module.exports = router;
