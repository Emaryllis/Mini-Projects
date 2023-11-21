function toCurr(str) { return str.toLocaleString('en-US', { style: 'currency', currency: 'USD' }) }
module.exports = toCurr;