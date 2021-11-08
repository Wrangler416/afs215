const assert = require('chai').assert
const returnOne = require('./fizzbuzzkata').returnOne
const returnTwo = require('./fizzbuzzkata').returnTwo

describe("returnOne", function(){
    it('gets one when one is passed in', function(){
        assert.equal(returnOne(), 1)
    })
})

describe("returnTwo", function(){
    it('gets two when two is passed in', function(){
        assert.equal(returnTwo(), 2)
    })
})

