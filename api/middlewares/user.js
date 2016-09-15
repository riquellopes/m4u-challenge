// User Middleware
var jwt = require('jwt-simple');
var log4js = require('log4js');

// Get logger
var logger = log4js.getLogger("booklog");

// Model
var User = require("../models/user");

// Get token secret
var TOKEN_SECRET = process.env.TOKEN_SECRET;

exports.UserMiddleware = function(request, response, next){
    var token = (request.body && request.body.access_token) ||
                (request.query && request.query.access_token) ||
                (request.headers['x-access-token']);

    if(token){
        logger.info("Token get - ", token);

        try{
            var decode = jwt.decode(token, TOKEN_SECRET);

            if(decode.exp <= Date.now()){
                logger.warn("Token expired", decode);
                response.json(400, {message: "Token expired."});
            }

            //  "-password -__v -create_at"
            User.findOne({_id: decode.iss}, function(error, user){
                if(error){
                    logger.warn("Uses does not exist.", error);
                    response.status(500);
                }

                logger.info("Middleware set user on request ", user);
                request.user = user;
                return next();
            });

        }catch(error){
            logger.error("User middleware error - ", error);
            return response.json(401, {message: "Token invalid."});
        }
    } else {
        logger.warn("Token not found - ", token);
        response.json(401, {message: "Toke not found."});
    }
}
