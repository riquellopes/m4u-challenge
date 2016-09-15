// User views
var router = require('express').Router();
var jwt = require('jwt-simple');
var moment = require('moment');

// Get token secret
var TOKEN_SECRET = process.env.TOKEN_SECRET;

// Model
var User = require("../models/user");

router.post("/", function(request, response){
    console.log("POST USER - ", request.body);

    var user = new User({
        email: request.body.email,
        password: request.body.password
    });

    user.save(function(error){
        if( error ){
            response.send(error);
        }

        response.json({msg: "User created", user: user});
    });
});

router.post("/auth", function(request, response){
    var email = request.body.email;
    var password = request.body.password;

    if( !email || !password ){
        response.send(401);
    }

    User.findOne({email: email}, function(error, user){

        if(error){
            response.send(401);
        }

        user.validation(password, function(isMatch){
            if(!isMatch){
                return response.send(401);
            }

            // define expiration time.
            var expiration = moment().add(7,'days').valueOf();
            var token = jwt.encode({
                iss: user.id,
                exp: expiration,
            }, TOKEN_SECRET);


            return response.json({
                token: token,
                expiration: expiration,
                user: user.toJSON()
            });
        });
    });

});

module.exports = router;
