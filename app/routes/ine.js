var Ine = require('../models/ine');
var User = require('../models/user');
var express = require('express');
var router = express.Router();

//var packet;

router.route('/ine')
    .post(function(req, res) {
        var packet = req.body;

        function callback2() {
            console.log("POST IN INE");
            res.send({'code': 1, 'data': packet});
        }

        function callback(data) {
            delete packet['facebookID'];
            packet['user'] = data;

            var newIne = new Ine(packet);
            newIne.save(function(err) {
                if (err) {
                    console.log("ERROR: " + err);
                    return;
                }
                callback2()
            });
        }

        User.findOne({'facebookID': req.body['facebookID']}, function(err, user) {
            if (err) {
                console.log("ERROR: " + err);
            }
            var newIne

        });
    })

module.exports = router;
