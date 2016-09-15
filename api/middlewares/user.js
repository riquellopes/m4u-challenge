// User Middleware
var jwt = require('jwt-simple');

// Model
var User = require("../models/user");

// Get token secret
var TOKEN_SECRET = process.env.TOKEN_SECRET;

exports.UserMiddleware = function(request, response, next){
    var token = (request.body && request.body.access_token) ||
                (request.query && request.query.access_token) ||
                (request.headers['x-access-token']);

    if(token){

        try{
            var decode = jwt.decode(token, TOKEN_SECRET);

            if(decode.exp <= Date.now()){
                response.json(400, {message: "Token expired."});
            }

            User.findOne({_id: decode.iss}, function(error, user){
                if(error){
                    response.status(500);
                }

                request.user = user;
                return next();
            });

        }catch(error){
            return response.json(401, {message: "Token invalid."});
        }
    } else {
        response.json(401, {message: "Toke not found."});
    }
}
