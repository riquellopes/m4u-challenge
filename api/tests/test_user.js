var request = require("supertest");
var assert = require("assert");
var app = require("../server").app;
var log4js = require('log4js');
var User = require("../models/user");

describe("created user jamelao", function(){
    before(function(){
        User.remove({username: "jamelao"}, function(){});
        log4js.clearAppenders();
    });

    it("should return status 201 and json.", function(done){
        request(app)
            .post("/user/")
            .send({username: "jamelao", password: 12345})
            .expect(201)
            .end(function(err, res){
                if( err ) return done(err);

                assert.equal(res.body.msg, "User created");
                assert.equal(typeof(res.body.user), 'object');
                done();
            });
    });

    it("should return status 409 and msg, when user was not created.", function(done){
        request(app)
            .post("/user/")
            .send({username: "jamelao", password: 12345})
            .expect(409)
            .end(function(err, res){
                if( err ) return done(err);

                assert.equal(res.body.msg, "User can't be created.");
                done();
            });
    });

});


describe("auth user kiko", function(){
    before(function(){
        var user = new User({
            username: "kiko",
            password: "12345"
        });

        user.save({}, function(){});

        log4js.clearAppenders();
    });

    after(function(){
        User.remove({username: "kiko"}, function(error, doc){});
    });

    it("should auth user with information ok.", function(){
        request(app)
            .post("/user/auth/")
            .send({username: "kiko", password: 12345})
            .expect('Content-Type', /json/)
            .expect(200)
            .end(function(err, res){
                if( err ) return done(err);

                assert.equal(res.body.user, "jamelao");
                done();
            });
    });

    // it("if username and password does not set.", function(done){
    //     request(app)
    //         .post("/user/auth/")
    //         .send({})
    //         .expect('Content-Type', /json/)
    //         .expect(401)
    //         .end(function(err, res){
    //             if( err ) return done(err);
    //
    //            assert.equal(res.body.msg, "Username or Password not set.");
    //             done();
    //         });
    // });

});
