var request = require("supertest");
var assert = require("assert");
var app = require("../server").app;
var log4js = require('log4js');
var Bookmark = require("../models/bookmark");
var User = require("../models/user");


describe("create bookmark", function(){
    var token = null;

    // Create user to test processes.
    before(function(done){
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

    it("Should return status 201 when created a bookmark.", function(done){
        request(app)
            .post("/bookmark/")
            .set('x-access-token', token)
            .send({url: "http://m4u.com"})
            .expect(201)
            .end(function(err, res){
                if( err ) return done(err);

                assert.equal(res.body.message, "successfull created.");
                done();
            });
    });

    it("Should return status 500 when error", function(done){
        request(app)
            .post("/bookmark/")
            .set('x-access-token', token)
            .expect(500)
            .end(function(err, res){
                if( err ) return done(err);

                assert.equal(res.body.message, "Error ...");
                done();
            });
    });
});
