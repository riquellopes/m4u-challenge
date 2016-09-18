var http_mocks = require("node-mocks-http");
var middleware = require("../middlewares/user");
var assert = require("assert");
var log4js = require('log4js');
var User = require("../models/user");

describe("Middleware validation", function(){

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
});
