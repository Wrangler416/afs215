import Checkout from '../walmart'
import Discount from './walmart'
import Item from './walmart'
const assert = require('chai').assert

describe("Tests", function(){

    it('can call instance of checkout class', function(){
        let result = new Checkout()
        assert.isDefined(result.items = [])
    })

    it('can add item', function(){
        assert.isFunction(result.addItem(new Item('Bread')))
    })

    it('can add price'), function(){
        assert.isFunction(result.addPrice(3))
    }

    it('can add discount'), function(){
        assert.deepEqual(result.addDiscount(new Discount('Bread', .40)))
    }
    it('can calculate total'), function(){
        assert.equal(result.calculateTotal(), 5)
    }
})

