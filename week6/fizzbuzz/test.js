const assert = require('chai').assert
const FizzBuzz = require('./fizzbuzz').FizzBuzz
const FizzBuzzTwo = require('./fizzbuzz').FizzBuzzTwo
const Fizz = require('./fizzbuzz').Fizz


describe("FizzBuzz", function(){
    it('gets one when one is passed on and two if two is passed in', function(){
        assert.equal(FizzBuzz(), 1)
    })

    it('gets two when 2 passed in',function(){
        assert.equal(FizzBuzzTwo(), 2)
    })

    it('gets fizz when 3 passed', function(){
        assert.equal(Fizz(), 3)
    })
})


