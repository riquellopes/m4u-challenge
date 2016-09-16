var request = require("supertest");
var assert = require("assert");
var app = require("../server").app;
var log4js = require('log4js');
var User = require("../models/user");

describe("created user", function(){
    before(function(){
        log4js.clearAppenders();
    });

    after(function(){
        User.remove({}, function(){});
    });

    it("should return status 200 and json when user was created.", function(done){
        request(app)
            .post("/user/")
            .send({email: "riquellopes@gmail.com", password: 12345})
            .expect(201)
            .end(function(err, res){
                if( err ) return done(err);

                assert.equal(res.body.msg, "User created");
                assert.equal(typeof(res.body.user), 'object');
                done();
            });
    });

    it("should return status 209 and msg, when user was not created.", function(done){
        request(app)
            .post("/user/")
            .send({email: "riquellopes@gmail.com", password: 12345})
            .expect(409)
            .end(function(err, res){
                if( err ) return done(err);

                assert.equal(res.body.msg, "User can't be created.");
                done();
            });
    });

});


describe("auth user", function(){
    before(function(){
        log4js.clearAppenders();
    });


    it("should user its ok, he can authenticate.", function(){
        request(app)
            .post("/user/auth/")
            .expect('Content-Type', /json/)
            .expect(401)
            .end(function(err, res){
                if( err ) return done(err);

                assert.equal(res.body.msg, "User or Password not set.");
                done();
            });
    });

});
