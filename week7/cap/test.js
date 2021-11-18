import { assert} from 'chai'
import { Checkout, Item, Discounts } from './walmart.js'

describe("Testing", function(){
    let result

    it('can create checkout class', function() {
        result = new Checkout()
        assert.isDefined(result.items = [])
    })

    it('can add item and price', function(){
        assert.deepEqual(result.addItem(new Item("Trash bags", 5.50)), 
            [{item: "Trash bags", price: 5.50}])
    })

    it('can get total', function(){
        assert.equal(result.getTotal(), 5.50)
    })

    it('can add items and get total', function(){
        assert.deepEqual(result.addItem(new Item("Paper Towels", 3.00)), 
            [{item: "Trash bags", price: 5.50}, 
            {item: "Paper Towels", price: 3.00}])
        assert.equal(result.getTotal(), 8.50)
    })
    it('can add discount'),function(){
        assert.deepEqual(result.addDiscount(new Discounts("Trash bags", .50)),
        [{unit: "Trash bags", discount: .50}])
    }
})