(()=> {
  class TestClass {
  
}
const var1 = 'string1'  
console.log(var1.__proto__)
  
const myArr = [1,2,3]
const findItem = find(myArr)
console.log(myArr.__proto__)
console.log('!' + findItem)
  
const x = function (a, b) {return sum = a * b};
console.log(x.__proto__);
  
})();