var http_mocks = require("node-mocks-http");
var request = require("supertest");
var middleware = require("../middlewares/user");
var assert = require("assert");
var app = require("../server").app;
var log4js = require('log4js');
var User = require("../models/user");

describe("Middleware validation", function(){
    var token = null;

    before(function(done){
        User.remove({}, function(error){});

        var user = new User({
            username: "kikinho_tesouro",
            password: 12345
        });

        user.save({}, function(){});

        // Disabled log
        log4js.clearAppenders();

        // User authenticates
        request(app)
            .post("/user/auth")
            .send({username: "kikinho_tesouro", password: 12345})
            .end(function(err, res){
                token = res.body.token
                done();
            });
    });

    it("Blank token status should be 428", function(done){
        var request = http_mocks.createRequest();
        var response = http_mocks.createResponse();

        var m = middleware.UserMiddleware(request, response);

        var data = JSON.parse( response._getData() );

        assert.equal(response.statusCode, 428)
        assert.equal(data.message, "Token not found.");

        done();
    });


    it("Invalid token status should be 401", function(done){
        var request = http_mocks.createRequest({
            headers: {"x-access-token": "XXXXXX"}
        });

        var response = http_mocks.createResponse();

        var m = middleware.UserMiddleware(request, response);

        var data = JSON.parse( response._getData() );

        assert.equal(response.statusCode, 401)
        assert.equal(data.message, "Token invalid.");

        done();
    });

    it("Valid token request has user.", function(done){
        var request = http_mocks.createRequest({
            headers: {"x-access-token": token}
        });

        var response = http_mocks.createResponse();

        var m = middleware.UserMiddleware(request, response, function next(){
            assert.equal(request.user.username, "kikinho_tesouro");
            assert.equal(request.user.is_admin, false);
            done();
        });

    });

});
