const assert = require('chai').assert
const One = require('./fizzbuzz').One
const FizzBuzzTwo = require('./fizzbuzz').FizzBuzzTwo
const Fizz = require('./fizzbuzz').Fizz
const Buzz = require('./fizzbuzz').Buzz
const FizzBuzz = require('./fizzbuzz').FizzBuzz

describe("FizzBuzz", function(){
    it('gets one when one is passed', function(){
        let result = One()
        assert.equal(result, 1)
    })

    it('gets two when two passed',function(){
        let result = FizzBuzzTwo()
        assert.equal(result, 2)
    })

    it('gets fizz when 3 is passed', function(){
        let result = Fizz(3)
        assert.equal(result, "Fizz")
    })

    it('gets buzz when 5 is passed', function(){
        let result = Buzz(5)
        assert.equal(result, "Buzz")
    })

    it('gets fizz when 6 passed', function(){
        let result = Fizz(6)
        assert.equal(result, "Fizz")
    })

    it('gets fizz when 3 passed', function(){
        let result = Buzz(10)
        assert.equal(result, "Buzz")
    })

    it('gets FizzBuzz when multiple of 3 and 5', function(){
        let result = FizzBuzz(15)
        assert.equal(result, "FizzBuzz")
    })
})

