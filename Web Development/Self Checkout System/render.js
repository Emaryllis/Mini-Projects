const toCurr = require("./utils");
function renderMains(mains) {
	let mainsMenu = '<div class="container text-center"><div class="row">';
	let mainsOption = {};
	let mainsCount = 0;
	const addMain = (name, price, options = false) => {
		function tOp(t, f) { return (options ? t : f); } // toggleOptions()
		mainsMenu += `<${tOp('button', 'div')} class="col m-2 p-3 rounded-4 ${tOp('btn btn-outline', 'border border')}-dark" ${tOp(`data-bs-target="#${name.replace(/ /g, '')}Options" data-bs-toggle="modal"`, `name="${name}"`)}>${name}<br>${toCurr(price)}${tOp('</button>','<br><div class="row position-relative"><div class="col"><div class="input-group d-flex justify-content-center mt-2"><button class="btn-subtract border btn btn-outline-dark p-3" id="quantity">-</button><input type="number" value="0" min= inputmode="numeric" id="quantity" class="quantity-field border text-center w-25"><button class="btn-add border btn btn-outline-dark p-3" id="quantity">+</button></div></div></div></div>')}`;
		mainsCount = (mainsCount + 1) % 4;
		mainsCount === 0 ? mainsMenu += '</div><div class="row">' : ''
	};
	Object.entries(mains).forEach(([nameKey, name]) => {
		if (name.price && name.enabled) { addMain(nameKey, name.price); } // If there are no options & is enabled
		else if (!name.price && !name.enabled) { // If there are options (!name.enabled to filter out those disabled mains with no options)
			const optionLst = Object.keys(name).filter(optionKey => name[optionKey].price);
			optionLst.slice(1).forEach(optionKey => name[optionKey].enabled ? addMain(nameKey, name[optionKey].price, true) : '');
			mainsOption[nameKey] = optionLst;
			mainsMenu += `<div class="modal fade" id="${nameKey.replace(/ /g, '')}Options" tabindex="-1"><div class="modal-dialog modal-dialog-centered"><div class="modal-content"><div class="modal-header"><div class="text">Options (${nameKey})</div><button type="button" class="btn-close" data-bs-dismiss="modal"></button></div><div class="modal-body text-center"><div class="row">${mainsOption[nameKey].map(option => `<button class="btn btn-outline-dark col m-2 col" data-bs-dismiss="modal" name="${nameKey} - ${option}">${option}<br>${toCurr(name[option]['price'])}</button>`).join('')}</div></div></div></div></div>`;
		}
	});
	mainsMenu += '</div></div>';
	return mainsMenu;
}
function renderDesserts(desserts) {
	let dessertsMenu = '<div class="container text-center"><div class="row">';
	let dessertsOption = {};
	let dessertsCount = 0;
	let cateCount = 0;
	const addDesserts = (name, price, options = false) => {
		const formattedPrice = (price.toString().includes(',') ? price.split(',').map(str => toCurr(parseFloat(str))).join('-') : toCurr(parseFloat(price))).replace('$NaN', 'TBD');
		function tOp(t, f) { return (options ? t : f); } // toggleOptions()
		dessertsMenu += `<${tOp('button', 'div')} class="col m-2 p-3 rounded-4 text-center ${tOp('btn btn-outline', 'border border')}-dark" ${tOp(`data-bs-target="#${name.replace(/ /g, '')}Options" data-bs-toggle="modal"`, `name="${name}"`)}>${name}<br>${formattedPrice}${tOp('</button>','<br><div class="row position-relative"><div class="col"><div class="input-group d-flex justify-content-center mt-2"><button class="btn-subtract border btn btn-outline-dark p-3" id="quantity">-</button><input type="number" value="0" min= inputmode="numeric" id="quantity" class="quantity-field border text-center w-25"><button class="btn-add border btn btn-outline-dark p-3" id="quantity">+</button></div></div></div></div>')}`;
		dessertsCount = (dessertsCount + 1) % Math.ceil(4 / Object.keys(desserts).length);
		dessertsCount === 0 ? dessertsMenu += '</div><div class="row">' : '';
	};
	Object.entries(desserts).forEach(([cateKey, cate]) => {
		dessertsMenu += `<div class="col${cateCount == 0 ? '' : ' hr'}"><h3 class="fw-medium">${cateKey}</h3><div class="row">`;
		cateCount++;
		dessertsCount = 0;
		Object.entries(cate).forEach(([nameKey, name]) => {
			if (name.price && name.enabled) {
				addDesserts(nameKey, name.price, name.price === 'TBD');
				if (name.price == 'TBD') {
					dessertsMenu += `<div class="modal fade" id="${nameKey.replace(/ /g, '')}Options" tabindex="-1"><div class="modal-dialog modal-dialog-centered"><div class="modal-content"><div class="modal-header"><div class="text">Options (${nameKey})</div><button type="button" class="btn-close" data-bs-dismiss="modal"></button></div><div class="modal-body"><div class="mb-3"><label for="priceInput" class="form-label">Price for ${nameKey}</label><div class="input-group"><span class="input-group-text">$</span><input type="text" class="form-control" id="priceInput"><button class="btn btn-outline-dark" data-bs-dismiss="modal">Submit</button></div></div></div></div></div></div>`;
				}
			} else if (!name.price && !name.enabled) {
				const prices = Object.values(name).map(item => item.price);
				const price = [...new Set([Math.min(...prices), Math.max(...prices)])].join(',');
				addDesserts(nameKey, price, true);
				const optionLst = Object.keys(name).filter(optionKey => name[optionKey].price);
				dessertsOption[nameKey] = optionLst;
				dessertsMenu += `<div class="modal fade" id="${nameKey.replace(/ /g, '')}Options" tabindex="-1"><div class="modal-dialog modal-dialog-centered"><div class="modal-content"><div class="modal-header"><div class="text">Options (${nameKey})</div><button type="button" class="btn-close" data-bs-dismiss="modal"></button></div><div class="modal-body text-center"><div class="row">${dessertsOption[nameKey].map(option => `<button class="btn btn-outline-dark col m-2 col" data-bs-dismiss="modal" name="${nameKey} - ${option}">${option}<br>${toCurr(name[option]['price'])}</button>`).join('')}</div></div></div></div></div>`;
			}
		});
		dessertsMenu += '</div></div>';
	});
	dessertsMenu += '</div></div>';
	return dessertsMenu;
}
function renderDrinks(drinks) {

}
function renderPanel() { }
module.exports = { renderMains, renderDesserts, renderDrinks, renderPanel };
