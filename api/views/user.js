// User views
var router = require('express').Router();
var jwt = require('jwt-simple');
var moment = require('moment');
var log4js = require('log4js');

// Get logger
var logger = log4js.getLogger("booklog");

// Get token secret
var TOKEN_SECRET = process.env.TOKEN_SECRET;

// Model
var User = require("../models/user");

// Get middleware
var middleware = require("../middlewares/user");


router.post("/", function(request, response){
    var user = new User({
        username: request.body.username,
        password: request.body.password,
        is_admin: request.query.is_admin || false
    });

    user.save(function(error){
        if( error ){
            // console.log(error)
            logger.error(error);
            return response.status(409).json({msg: "User can't be created."});
        }

        logger.info("User created successfull - " + request.body.username);
        response.status(201).json({msg: "User created", user: user});
    });
});

router.get("/", middleware.UserMiddleware, function(request, response){
    var user = request.user;

    if(!user.is_admin){
        logger.warn("User is not an admin.", user);
        return response.status(401).json({msg: "User is not an admin"});
    }

    User.find({}, function(error, list){
        if(error){
            return response.send(500).json({msg: "Error."});
        }

        response.json(list);
    });
});

router.post("/auth", function(request, response){
    var username = request.body.username;
    var password = request.body.password;

    if( !username || !password ){
        logger.warn("blank username or password", request.body);
        return response.status(401).json({msg: "Username or Password not set."});
    }

    User.findOne({username: username}, function(error, user){
        if(error || !user){
            logger.error("Error at findOne user.", error);
            return response.status(401).json({msg: "Username or password is invalid."});
        }

        user.validation(password, function(isMatch){
            if(!isMatch){
                return response.status(401).json({msg: "Username or password is invalid."});
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
